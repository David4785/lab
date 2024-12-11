def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
def graham_scan(points):
    points.sort()
    hull = []
    for point in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    return hull
points = [(1, 2), (3, 1), (5, 4), (7, 6), (6, 8), (8, 7), (2, 3), (4, 5), (0, 0)]
result = graham_scan(points)
print("Convex Hull:", result)