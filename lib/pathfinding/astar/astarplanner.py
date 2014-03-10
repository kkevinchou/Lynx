from node import Node
from Queue import PriorityQueue
from heapq import heappush, heappop
from util import (
    distance_between,
    intersect_polygons,
    create_line_segment,
)

class AStarPlanner(object):
    def __init__(self):
        self.polygons = []
        self.nodes = []

        self.gx_map = {}
        self.hx_map = {}

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
        open_queue = []

        # key: node, value: previous_node_in_path
        path_map = {}
        heappush(open_queue, (0, start_node))

        while len(open_queue) > 0:
            current_node_cost, current_node = heappop(open_queue)

            if current_node == goal_node:
                break

            neighbors = current_node.neighbors

            print '-------------------'
            print current_node, neighbors
            import pprint
            pp = pprint.PrettyPrinter()
            pp.pprint(path_map)

            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue

                if neighbor.x == -2:
                    print closed_set

                gx = distance_between(current_node, neighbor) + current_node_cost
                hx = distance_between(neighbor, goal_node)
                neighbor_cost = gx + hx

                if neighbor in open_queue:
                    if neighbor.x == -2:
                        print '1'
                    if gx < self.gx_map[neighbor]:
                        self.gx_map[neighbor] = gx
                        path_map[neighbor] = current_node
                else:
                    if neighbor.x == -2:
                        print '2'
                    self.gx_map[neighbor] = gx
                    self.hx_map[neighbor] = hx
                    path_map[neighbor] = current_node

                heappush(open_queue, (gx + hx, neighbor))

            closed_set.add(current_node)

        path_node = goal_node
        path = []

        while path_node is not None:
            path.append(path_node)
            path_node = path_map.get(path_node)

        return path
        

