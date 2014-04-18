from lib.vec2d import Vec2d
import pygame

red = (255, 0, 0)

def get_bottom_right_most_point(points):
    lowest_point = points[0]

    for point in points:
        if point.y > lowest_point.y:
            lowest_point = point
        elif point.y == lowest_point.y:
            if point.x > lowest_point.x:
                lowest_point = point

    return lowest_point

def generate_convex_hull(points, screen=None):
    # Note, this algorithm requires that we select the bottom most point.
    # Otherwise, we could potentially get negative angles from `get_angle_between()`
    # which throws off the angle sorting

    if len(points) < 3:
        raise Exception('Cannot generate convex hull for fewer than three points')

    lines_to_draw = []
    
    pivot_point = get_bottom_right_most_point(points)
    point_to_angle_map = {}
    for point in points:
        if point == pivot_point:
            continue

        angle = Vec2d(pivot_point.x + 1, pivot_point.y).get_angle_between(point - pivot_point)
        if angle < 0:
            angle += 360

        point_to_angle_map[point] = angle

    sorted_points = sorted(point_to_angle_map, key=point_to_angle_map.get, reverse=True)
    sorted_points.append(pivot_point)

    hull_points = [pivot_point, sorted_points[0], sorted_points[1]]

    for point in sorted_points[2:]:
        next_hull_point_found = False
        while not next_hull_point_found:
            previous, current, next = hull_points[-3:]
            vec2 = next - current
            vec1 = current - previous

            if vec2.cross(vec1) > 0:
                hull_points.append(point)
                next_hull_point_found = True
            elif vec2.cross(vec1) < 0:
                hull_points.pop(-2)
            else:
                next_dist = (next - previous).get_length()
                current_dist = (current - previous).get_length()

                # Keep the point that's further away for our convex hull
                if next_dist > current_dist:
                    hull_points.pop(-2)
                else:
                    hull_points.pop()
                
                hull_points.append(point)
                next_hull_point_found = True

    # The last point equals the first one, pop it off
    hull_points.pop()

    return hull_points
