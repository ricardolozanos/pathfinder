#!/usr/bin/env python
# coding: utf-8

from collections import deque
import heapq
import time
import sys

# Clase base para validar el mapa 
class MapError(Exception):
    """Clase base para excepciones relacionadas con el mapa."""
    pass

class Node:
    def __init__(self, position, cost, parent=None):
        self.position = position  
        self.cost = cost  # Costo de llegar desde el inicio a este nodo
        self.parent = parent  # Nodo padre (si existe alguno)
        
    # Comparar dos nodos (nodo1 == nodo2)
    def __eq__(self, other):
        return self.position == other.position
    
    # Asignar un ID único a cada nodo 
    def __hash__(self):
        return hash(self.position)
    
    # Comparar el costo de dos nodos. Necesario para esta función: heapq.heappush(open_priority_queue, start_node)
    def __lt__(self, other):
        return self.cost < other.cost

#Clase principal,
class PathFinder:
    #Inicializar con valores del map.txt, validar la forma del mapa, obtener los datos, y correr los algoritmos
    def __init__(self, map_text_file,algorithm_requested):
        self.map_dim, self.agent_start_pos, self.goal_pos, self.full_map = self.read_map_file(map_text_file)
        self.algorithm_requested=algorithm_requested
        self.map_validated = False
        self.results = {}
        try:
            self.validate_map()
            self.map_validated = True
            self.run_search_algorithms()
        except MapError as e:
            print(f"Map Error: {str(e)}")
        except FileNotFoundError:
            print(f"File not found: {self.map_name}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
    
    #Leer los datos del text file.
    def read_map_file(self, map_text_file):
        with open(map_text_file, 'r') as mapInfo:
            map_dimensions = list(map(int, mapInfo.readline().split()))
            agent_start_position = tuple(map(int, mapInfo.readline().split()))
            goal_position = tuple(map(int, mapInfo.readline().split()))
            full_map = []

            # Leer las líneas del mapa mientras se omiten las líneas vacías al final
            for mapLine in mapInfo:
                stripped_line = mapLine.strip()
                if stripped_line:
                    row = list(map(int, stripped_line.split()))
                    full_map.append(row)

        return map_dimensions, agent_start_position, goal_position, full_map

    #Verificar que el texto tenga la forma requerida para correr correctamente
    def validate_map(self):
        map_dim, agent_start_pos, goal_pos, full_map = self.map_dim, self.agent_start_pos, self.goal_pos, self.full_map
        if len(map_dim) != 2:
            raise MapError("Invalid map dimensions: must be a list of two integers")
        if len(agent_start_pos) != 2:
            raise MapError("Invalid agent start position: must be a list of two integers")
        if len(goal_pos) != 2:
            raise MapError("Invalid goal position: must be a list of two integers")
        if agent_start_pos[0] > map_dim[0] or agent_start_pos[1] > map_dim[1]:
            raise MapError("Agent start position is outside the map")
        if goal_pos[0] > map_dim[0] or goal_pos[1] > map_dim[1]:
            raise MapError("Goal position is outside the map")
        if len(full_map) != map_dim[0] or any(len(row) != map_dim[1] for row in full_map):
            raise MapError("Full map dimensions do not match given map dimensions")
            
    def change_map(self, map_text_file):
        # Volver a inicializar la clase con los nuevos datos del mapa
        self.map_dim, self.agent_start_pos, self.goal_pos, self.full_map = self.read_map_file(map_text_file)
        self.map_validated = False
        try:
            self.validate_map()
            self.map_validated = True
            self.results = {}
            self.run_search_algorithms()
        except MapError as e:
            print(f"Map Error: {str(e)}")
        except FileNotFoundError:
            print(f"File not found: {map_text_file}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            
    #Generar los succesores de cada nodo
    def generate_successors(self, node):
        successors = []
        row, col = node.position

        # Definir movimientos posibles (arriba, abajo, izquierda, derecha)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]

            # Verificar si la nueva posición está dentro de los límites del mapa
            if 0 <= new_row < len(self.full_map) and 0 <= new_col < len(self.full_map[0]):
                # Verificar si la nueva posición no es un terreno no transitable (0)
                if self.full_map[new_row][new_col] != 0:
                    # Calcular el costo para el nuevo nodo en función del valor del mapa
                    new_cost = node.cost + self.full_map[new_row][new_col]
                    new_node = Node((new_row, new_col), new_cost, node)
                    successors.append(new_node)

        return successors
    
    #Algoritmo BFS, Checar
    def bfs_search(self, cutoff_time=180):
        # Inicializar estructuras de datos
        queue = deque()  
        visited = set()  
        initial_node = Node(self.agent_start_pos, 0)
        queue.append(initial_node)

        # Inicializar métricas
        path_cost = -1
        nodes_expanded = 0
        max_nodes_in_memory = 0

        # Iniciar temporizador
        start_time = time.time()

        # Iniciar ruta como una lista vacía
        path = []

        # Bucle principal de BFS
        while queue:
            # Verificar el tiempo de corte
            if time.time() - start_time > cutoff_time:
                break
            current_node = queue.popleft()
            nodes_expanded += 1
            max_nodes_in_memory = max(max_nodes_in_memory, len(queue) + len(visited))
            if current_node.position == self.goal_pos:
                path_cost = current_node.cost
                
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                path.reverse()  # Revertir la ruta para obtenerla desde el inicio hasta el destino

                # Calcular el tiempo de ejecución
                runtime = (time.time() - start_time) * 1000  # Convertir a milisegundos
                return path, path_cost, nodes_expanded, max_nodes_in_memory, runtime

            else:
                visited.add(current_node)
                successors = self.generate_successors(current_node)
                for successor in successors:
                    if successor not in visited and successor not in queue:
                        queue.append(successor)
        runtime = (time.time() - start_time) * 1000  # Convertir a milisegundos
        return [], -1, nodes_expanded, max_nodes_in_memory, runtime
    
    
    
    
    def dls_search(self, depth_limit):
        # Inicializar estructuras de datos
        queue = deque()  # Cola para realizar la búsqueda en profundidad limitada
        visited = set()  # Conjunto para mantener un registro de los nodos visitados
        initial_node = Node(self.agent_start_pos, 0)
        queue.append(initial_node)

        # Inicializar métricas
        path_cost = -1
        nodes_expanded = 0
        max_nodes_in_memory = 0

        # Bucle principal de búsqueda en profundidad limitada
        while queue:
            current_node = queue.pop()
            nodes_expanded += 1
            max_nodes_in_memory = max(max_nodes_in_memory, len(queue) + len(visited))
            if current_node.position == self.goal_pos:
                # Reconstruir la ruta y calcular las métricas
                path_cost = current_node.cost
                
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                path.reverse()  # Revertir la ruta para obtenerla desde el inicio hasta el destino
                return path, path_cost, nodes_expanded, max_nodes_in_memory

            if current_node.cost < depth_limit:
                visited.add(current_node)

                successors = self.generate_successors(current_node)
                for successor in successors:
                    if successor not in visited:
                        queue.append(successor)

        # Si no se encuentra una solución dentro del límite de profundidad, devolver un fallo
        return [], -1, nodes_expanded, max_nodes_in_memory

    def ids_search(self, max_depth, cutoff_time=180):
        # Comenzar con un límite de profundidad de 1 e incrementarlo gradualmente
        start_time = time.time()  # Iniciar el temporizador aquí
        for depth_limit in range(1, max_depth + 1):
            # Realizar la búsqueda en profundidad limitada con el límite de profundidad actual
            path, path_cost, nodes_expanded, max_nodes_in_memory = self.dls_search(depth_limit)

            # Verificar si se encontró una solución
            if path:
                runtime = (time.time() - start_time) * 1000  # Calcular el tiempo de ejecución en milisegundos
                return path, path_cost, nodes_expanded, max_nodes_in_memory, runtime

            # Verificar el tiempo de corte
            if time.time() - start_time > cutoff_time:
                break

        runtime = (time.time() - start_time) * 1000  # Convertir a milisegundos
        return [], -1, nodes_expanded, max_nodes_in_memory, runtime

    def a_star_search(self, cutoff_time=180):
        # Inicializar estructuras de datos
        open_priority_queue = []  # Cola de prioridad para realizar la búsqueda A*
        visited = set()  
        start_node = Node(self.agent_start_pos, 0)
        heapq.heappush(open_priority_queue, start_node)

        # Inicializar métricas
        nodes_expanded = 0
        max_nodes_in_memory = 0

        # Iniciar el temporizador
        start_time = time.time()

        # Bucle principal de búsqueda A*
        while open_priority_queue:
            # Verificar el tiempo de corte
            if time.time() - start_time > cutoff_time:
                break

            current_node = heapq.heappop(open_priority_queue)

            if current_node.position == self.goal_pos:
                # Reconstruir la ruta y calcular el costo de la ruta
                path = []
                path_cost = current_node.cost
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                path.reverse()  # Revertir la ruta para obtenerla desde el inicio hasta el destino

                # Calcular el tiempo de ejecución
                runtime = (time.time() - start_time) * 1000  # Convertir a milisegundos

                return path, path_cost, nodes_expanded, max_nodes_in_memory, runtime

            visited.add(current_node.position)

            successors = self.generate_successors(current_node)
            for successor in successors:
                if successor.position not in visited:
                    heapq.heappush(open_priority_queue, successor)
                    max_nodes_in_memory = max(max_nodes_in_memory, len(open_priority_queue) + len(visited))

            nodes_expanded += 1

        runtime = (time.time() - start_time) * 1000  # Convertir a milisegundos
        return [], -1, nodes_expanded, max_nodes_in_memory, runtime


    def run_search_algorithms(self):
        # Verificar si el mapa ha sido validado
        if self.map_validated:
            # Ejecutar la búsqueda BFS
            print(self.algorithm_requested.upper())
            if self.algorithm_requested.upper() == 'BFS':
                bfs_path, bfs_path_cost, bfs_nodes_expanded, bfs_max_nodes, bfs_runtime = self.bfs_search()

                # Almacenar los resultados de BFS
                self.results['BFS'] = {
                    'Path': bfs_path,
                    'Path Cost': bfs_path_cost,
                    'Nodes Expanded': bfs_nodes_expanded,
                    'Max Nodes in Memory': bfs_max_nodes,
                    'Runtime (ms)': bfs_runtime
                }

            # Ejecutar la búsqueda IDS
            if self.algorithm_requested.upper() == 'IDS':
                max_depth = 1000 
                ids_path, ids_path_cost, ids_nodes_expanded, ids_max_nodes, ids_runtime = self.ids_search(max_depth)

                # Almacenar los resultados de IDS
                self.results['IDS'] = {
                    'Path': ids_path,
                    'Path Cost': ids_path_cost,
                    'Nodes Expanded': ids_nodes_expanded,
                    'Max Nodes in Memory': ids_max_nodes,
                    'Runtime (ms)': ids_runtime
                }
            if self.algorithm_requested.upper() == 'A*' or self.algorithm_requested.upper() == 'A':
                # Ejecutar la búsqueda A*
                a_star_path, a_star_path_cost, a_star_nodes_expanded, a_star_max_nodes, a_star_runtime = self.a_star_search()

                # Almacenar los resultados de A*
                self.results['A*'] = {
                    'Path': a_star_path,
                    'Path Cost': a_star_path_cost,
                    'Nodes Expanded': a_star_nodes_expanded,
                    'Max Nodes in Memory': a_star_max_nodes,
                    'Runtime (ms)': a_star_runtime
                }
    

    def visualize_path(self, algorithm, view=None):
        #View (Dar GUI para visualizar datos)
        if view:
            # Preparar datos para visualización
            data = {
                'results': self.results[algorithm],
                'algorithm': algorithm,
                'start_pos': self.agent_start_pos,
                'map': self.full_map,
                'goal': self.goal_pos
            }
            return data
        else:
            #Si no existe GUI mandar datos a terminal
            if algorithm not in self.results:
                print(f"No results available for {algorithm}. Run the search algorithm first.")
                return

            path_info = self.results[algorithm]
            path = path_info['Path']
            grid = self.full_map
            agent_position = self.agent_start_pos
            print(path)

            for position in path:
                if position != agent_position:
                    print(f"Move to {position} (Cost: {grid[position[0]][position[1]]})")
                    agent_position = position
                else:
                    print(f"Stay at {position} (Cost: 0)")

                self.display_map_with_costs(grid, agent_position)
                self.display_info(agent_position, grid)
            self.display_final_info(self.results[algorithm],algorithm)

        
        
        
    #Mostrar el reporte final, algoritmo, resultados y detalles.
    def display_final_info(self, results, algorithm):
        print()
        print("Final report")
        print()
        print(f"The algorithm used was: {algorithm}")
        print(f"The path followed was: {results['Path']}")
        print(f"The path cost was: {results['Path Cost']}")
        print(f"Nodes Expanded: {results['Nodes Expanded']}")
        print(f"Max Nodes: {results['Max Nodes in Memory']}")
        print(f"Total Run time (ms) : {results['Runtime (ms)']}")

    
    #Mostrar el mapa final con los costos, y posicion del agente.
    def display_map_with_costs(self, grid, agent_position):
        print()
        print("Current Map")
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) == agent_position:
                    print("X", end=" ")
                elif grid[i][j] == 0:
                    print("#", end=" ")
                else:
                    print(grid[i][j], end=" ")
            print()
    
    #Mostrar datos despues de cada movimiento del agente
    def display_info(self, agent_position, grid):
        print()
        print("Information Table:")
        print(f"Agent's Position: {agent_position}")
        print("Possible Moves:")
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (agent_position[0] + move[0], agent_position[1] + move[1])
            if (
                0 <= new_position[0] < len(grid) and
                0 <= new_position[1] < len(grid[0]) and
                grid[new_position[0]][new_position[1]] != 0
            ):
                cost = grid[new_position[0]][new_position[1]]
                print(f"Move to {new_position} (Cost: {cost})")
                