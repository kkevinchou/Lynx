from astarplanner import AStarPlanner_Grid

def test():
    a = AStarPlanner_Grid(10, 10)

tests = [
    test,
]

for test in tests:
    test()