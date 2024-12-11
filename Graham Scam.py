def graham_scan(points):
    points.sort()
    hull = []
    for p in points:
        while len(hull) >= 2 and (hull[-2][0] - p[0]) * (hull[-1][1] - p[1]) - (hull[-2][1] - p[1]) * (hull[-1][0] - p[0]) <= 0:
            hull.pop()
        hull.append(p)
    return hull
points = [(2, 4), (1, 1), (4, 2), (6, 5), (7, 7), (3, 3), (5, 6), (0, 0)]
print("Convex Hull:", graham_scan(points))