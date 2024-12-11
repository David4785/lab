def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    m1 = (y2 - y1) / (x2 - x1) if x2 != x1 else None
    m2 = (y4 - y3) / (x4 - x3) if x4 != x3 else None

    if m1 == m2:
        return None
    if m1 is not None and m2 is not None:
        c1 = y1 - m1 * x1
        c2 = y3 - m2 * x3
        x_intersection = (c2 - c1) / (m1 - m2)
        y_intersection = m1 * x_intersection + c1
        return (x_intersection, y_intersection)
    return None


x1, y1 = 2, 2
x2, y2 = 5, 5
x3, y3 = 2, 5
x4, y4 = 5, 2

intersection = line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
print("Intersection:", intersection)
