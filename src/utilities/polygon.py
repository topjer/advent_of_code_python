from collections import defaultdict, Counter


def draw_region(current_region: set[tuple[int,int]]):
    """ Draw a polygon of grid aligned squares.

    The points are automatically offset to only draw the rectangular region containing them.

    Produces outputs like this:
        ..X..
        ..XXX
        ..XXX
        XXXX.

    """
    min_y = min(point[0] for point in current_region)
    max_y = max(point[0] for point in current_region)
    min_x= min(point[1] for point in current_region)
    max_x = max(point[1] for point in current_region)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y,x) in current_region:
                print("X", end="")
            else:
                print(".", end="")
        print("")


def find_edges(points: set[ tuple[ int, int ] ]):
    """ Find edges in a set of points

    This function finds edges in a set of points in the plane. It is assumed that the set
    represents a polygon consisting of edge aligned squares which are touching horizontally and
    vertically. So something like this (where 'X' represents a point of the set):

        ..X..
        ..XXX
        ..XXX
        XXXX.
    """

    print(points)
    draw_region(points)
    edges = Counter()
    for point in points:
        N = (point[0] - 1, point[1])
        NE = (point[0] - 1, point[1] + 1)
        E = (point[0], point[1] + 1)
        SE = (point[0] + 1, point[1] + 1)
        S = (point[0] + 1, point[1])
        SW = (point[0] + 1, point[1] -1 )
        W = (point[0], point[1] - 1)
        NW = (point[0] - 1 , point[1] - 1)

        if (N not in points) and (W not in points):
            edges.update( [ point ] )

        if (N in points) and (W in points) and (NW not in points):
            edges.update( [ point ] )

        if (W not in points) and (S not in points):
            edges.update( [ point ] )

        if (W in points) and (S in points) and (SW not in points):
            edges.update( [ point ] )

        if (E not in points) and (S not in points):
            edges.update( [ point ] )

        if (E in points) and (S in points) and (SE not in points):
            edges.update( [ point ] )

        if (E not in points) and (N not in points):
            edges.update( [ point ] )

        if (E in points) and (N in points) and (NE not in points):
            edges.update( [ point ] )

    print(edges)
    return edges
