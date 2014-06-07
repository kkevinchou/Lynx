from lib.vec2d import Vec2d
from collections import defaultdict
from Queue import PriorityQueue
from heapq import heappush, heappop, heapify
from lib.geometry.util import (
    distance_between,
    intersect_polygons,
)

class AStarPlanner(object):
    def __init__(self):
        self.polygons = []
        self.nodes = []
        self.neighbors = defaultdict(list)

    def add_polygon(self, polygon):
        self.polygons.append(polygon)
        self.nodes.extend(polygon.get_points())

    def add_polygons(self, polygons):
        for polygon in polygons:
            self.add_polygon(polygon)

    def init(self):
        self.compute_neighbours()

    def compute_neighbours(self):
        for node_a in self.nodes:
            for node_b in self.nodes:
                if node_a == node_b:
                    continue

                if not intersect_polygons([node_a, node_b], self.polygons):
                    self.neighbors[node_a].append(node_b)

    def init_start_goal(self, start_node, goal_node):
        self.clean_start_node = True
        self.clean_goal_node = True

        for start_goal_node in [start_node, goal_node]:
            for node in self.nodes:
                if start_goal_node == node:
                    if start_goal_node == start_node:
                        self.clean_start_node = False
                    elif start_goal_node == goal_node:
                        self.clean_goal_node = False
                elif not intersect_polygons([start_goal_node, node], self.polygons):
                    if node not in self.neighbors[start_goal_node]:
                        self.neighbors[start_goal_node].append(node)

                    if start_goal_node not in self.neighbors[node]:
                        self.neighbors[node].append(start_goal_node)

    def cleanup_start_goal(self, start_node, goal_node):
        if self.clean_start_node:
            self.remove_node(start_node)

        if self.clean_goal_node:
            self.remove_node(goal_node)

    def remove_node(self, r_node):
        try:
            self.nodes.remove(r_node)
        except ValueError:
            pass

        self.neighbors.pop(r_node)

        for node, neighbors in self.neighbors.iteritems():
            try:
                neighbors.remove(r_node)
            except ValueError:
                pass

    def draw_neighbors(self, renderer, color=(0, 0, 0)):
        for node, neighbors in self.neighbors.iteritems():
            for neighbor in neighbors:
                renderer.draw_lines([node, neighbor], color)

    def find_path(self, x1, y1, x2, y2):
        start_node = Vec2d(x1, y1)
        goal_node = Vec2d(x2, y2)

        if not intersect_polygons([start_node, goal_node], self.polygons):
            return [goal_node]

        self.init_start_goal(start_node, goal_node)

        closed_set = set()
        open_queue = [(0, start_node)]

        path_map = {}
        gx_map = { start_node: 0 }

        while len(open_queue) > 0:
            current_node_cost, current_node = heappop(open_queue)
            if current_node == goal_node:
                break

            neighbors = self.neighbors[current_node]

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
            path.append(path_node.copy())
            path_node = path_map.get(path_node)

        # Remove the starting node
        path.pop()
        path.reverse()

        self.cleanup_start_goal(start_node, goal_node)

        return path
        

