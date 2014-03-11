from lib.pathfinding.astar.node import Node
from Queue import PriorityQueue
from heapq import heappush, heappop, heapify
from util import (
    distance_between,
    intersect_polygons,
    create_line_segment,
)

class AStarPlanner(object):
    def __init__(self):
        self.polygons = []
        self.nodes = []

    def add_polygon(self, polygon):
        self.polygons.append(polygon)
        
        polygon_points = polygon.get_points()
        for point in polygon_points:
            self.nodes.append(Node(point))

    def compute_neighbours(self):
        for node_a in self.nodes:
            for node_b in self.nodes:
                if node_a == node_b:
                    continue

                if not intersect_polygons(create_line_segment(node_a, node_b), self.polygons):
                    node_a.neighbors.append(node_b)

    def get_closest_node(self, node):
        min_dist = distance_between(node, self.nodes[0])
        min_node = self.nodes[0]

        for current_node in self.nodes:
            dist = distance_between(node, current_node)
            if dist < min_dist:
                min_dist = dist
                min_node = node

        return min_node

    def remove_node(self, node):
        self.nodes.remove(node)

    def add_node(self, node):
        self.nodes.append(node)

    def find_path(self, x1, y1, x2, y2):
        start_node = Node(x1, y1)
        goal_node = Node(x2, y2)

        self.add_node(start_node)
        self.add_node(goal_node)
        self.compute_neighbours()

        # check for direct los from start_node to goal_node
        # if not intersect_polygons([start_node, goal_node], self.polygons):
        #     return [start_node, goal_node]

        # closest_node = self.get_closest_node(start_node)

        closed_set = set()
        open_queue = [(0, start_node)]

        path_map = {}
        gx_map = { start_node: 0 }

        while len(open_queue) > 0:
            current_node_cost, current_node = heappop(open_queue)
            if current_node == goal_node:
                break

            neighbors = current_node.neighbors

            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue

                gx = distance_between(neighbor, current_node) + gx_map[current_node]
                hx = distance_between(neighbor, goal_node)

                neighbor_in_open_queue = False

                for cost, node in open_queue:
                    if node == neighbor:
                        neighbor_in_open_queue = True

                if neighbor_in_open_queue:
                    if gx < gx_map[neighbor]:
                        open_queue.remove((gx_map[neighbor] + hx, neighbor))
                        gx_map[neighbor] = gx
                        path_map[neighbor] = current_node

                        # Update priority
                        # Note, this runs in linear time, we could probably do something more efficient here

                        heappush(open_queue, (gx + hx, neighbor))
                        heapify(open_queue)
                else:
                    gx_map[neighbor] = gx
                    path_map[neighbor] = current_node
                    heappush(open_queue, (gx + hx, neighbor))

            closed_set.add(current_node)

        if current_node != goal_node:
            return None

        path = []
        path_node = goal_node
        while path_node is not None:
            path.append(path_node)
            path_node = path_map.get(path_node)

        return path
        

