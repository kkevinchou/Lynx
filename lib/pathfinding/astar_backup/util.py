import numpy

def line_segment_equal(line_segment_a, line_segment_b):
    return (
        numpy.array_equal(line_segment_a[0], line_segment_b[0]) and numpy.array_equal(line_segment_a[1], line_segment_b[1])
    ) or (
        numpy.array_equal(line_segment_a[0], line_segment_b[1]) and numpy.array_equal(line_segment_a[1], line_segment_b[0])
    )

def create_line_segment(node_a, node_b):
    return [node_a.point(), node_b.point()]

def distance_between(node_a, node_b):
    point_a = node_a.point()
    point_b = node_b.point()

    return numpy.linalg.norm(point_a - point_b)

def intersect_multi(line_segment, polygons):
    for polygon in polygons:
        if intersect_single(line_segment, polygon):
            return True
    return False

def intersect_single(line_segment, polygon):
    for edge in polygon.get_edges():
        if line_intersect(line_segment, edge):
            return True
        elif line_segment_equal(line_segment, edge):
            return True

    return False

def line_intersect(line_segment_a, line_segment_b):
    t_value = _compute_t_value(line_segment_a, line_segment_b)
    return t_value >= 0 and t_value <= 1

def _compute_t_value(intersector, intersectee):
    intersectee_dir = intersectee[1] - intersectee[0]
    normal = numpy.array([intersectee_dir[1], -intersectee_dir[0]])

    A = intersector[0]
    B = intersector[1]
    P = intersectee[0]

    denominator = (A - B).dot(normal)
    if denominator == 0:
        return None

    return (A - P).dot(normal) / denominator