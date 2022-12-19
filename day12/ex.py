import sys
from pathlib import Path


################################################################################


def debug(chart, visited):
    for y in chart:
        print("".join(y))

    visited_chart = [["." for n in line] for line in chart]

    for y in range(len(visited_chart)):
        for x in range(len(visited_chart[0])):
            if (x, y) in visited:
                visited_chart[y][x] = chart[y][x]

    for y in visited_chart:
        print("".join(y))

    pass


def dijkstra(graph, chart, start):
    dist = {}
    prev = {}
    Q = set()

    for v in graph:
        dist[v] = sys.maxsize
        prev[v] = None
        Q.add(v)

    dist[start] = 0

    while Q:
        min_dist = sys.maxsize
        u = None

        for v in Q:
            if dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        if u is None:
            u = Q.pop()
        else:
            Q.remove(u)

        u_x, u_y = u

        neighbors = []
        neighbors.append((u_x + 1, u_y))
        neighbors.append((u_x, u_y + 1))
        neighbors.append((u_x - 1, u_y))
        neighbors.append((u_x, u_y - 1))

        neighbors = [n for n in neighbors if n in Q]

        for v in neighbors:
            alt = dist[u]

            v_x, v_y = v

            current_elevation = ord(chart[v_y][v_x])
            if chart[v_y][v_x] == "E":
                current_elevation = ord("z") + 1

            if chart[u_y][u_x] not in ["S", "E"]:
                if current_elevation > ord(chart[u_y][u_x]) + 1:
                    alt = sys.maxsize
                else:
                    alt += 1

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def get_graph_start_goal(data):
    graph = set()
    start = None
    goal = None

    for y in range(len(data)):
        for x in range(len(data[0])):
            graph.add((x, y))
            if data[y][x] == "S":
                start = (x, y)
            if data[y][x] == "E":
                goal = (x, y)

    return graph, start, goal


def get_path(prev, start, goal):
    path = []
    current = goal

    while True:
        if current == start:
            break
        path.append(current)
        current = prev[current]
    return path


def part1(data):
    graph, start, goal = get_graph_start_goal(data)
    dist, prev = dijkstra(graph, data, start)
    path = get_path(prev, start, goal)
    print(len(path))
    
    
def parse(path):
    data = Path(path).read_text().splitlines()
    data = [[n for n in line] for line in data]
    return data

part1(parse("day12/day12.txt"))