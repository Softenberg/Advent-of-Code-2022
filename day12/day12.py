#procedure BFS(G, root) is
#    let Q be a queue
#    label root as explored
#    Q.enqueue(root)
#    while Q is not empty do
#        v := Q.dequeue()
#        if v is the goal then
#            return v
#        for all edges from v to w in G.adjacentEdges(v) do
#            if w is not labeled as explored then
#                label w as explored
#                w.parent := v
#                Q.enqueue(w)

from pprint import pprint as pp
import numpy as np

with open("day12/day12.txt", "r") as file:
    lines_in = [line.rstrip() for line in file]


alpha = "SabcdefghijklmnopqrstuvwxyzE"


grid = []
vis = []
dist = []
for i in lines_in:
    grid.append([alpha.index(x) for x in i])  
    vis.append([False for x in i])
    dist.append([20000000 for x in i])
grid2 = grid 
vis2 = vis 
dist2 = dist 



def is_vis(vis, x, y):
    
    if (x < 0 or y < 0 or x >= len(vis) or y >= len(vis[0])):
        return False
    #print(x, y)
    if vis[x][y]:
        return False
    
    
    return True


dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

def BFS(G, vis, x, y):
    q = []
    vis[x][y] = True 
    dist[x][y] = 0
    q.append([x, y])
    prev = []
    while len(q) > 0:
        cell = q.pop(0)
        xn = cell[0]
        yn = cell[1]
        prev.append(cell)
        #print(G[xn][yn])
        for i in range(4):
            adjx = xn + dRow[i]
            adjy = yn + dCol[i]
            #print("before vis: ", adjx, adjy)
            if is_vis(vis, adjx, adjy) and (grid[adjx][adjy] == grid[xn][yn]+1 or grid[adjx][adjy] <= grid[xn][yn]):
                  
                dist[adjx][adjy] = dist[xn][yn]+1                  
                q.append([adjx, adjy])
                vis[adjx][adjy] = True
                #pp(G[adjx][adjy])
                if G[adjx][adjy] >= 27:
                    return(dist[adjx][adjy])
                #print(adjx, adjy, grid[adjx][adjy], vis[adjx][adjy], dist[adjx][adjy])
    #pp(G[adjx][adjy])

distances = []
start_poses= []
for i, iv in enumerate(grid):
    for j, jv in enumerate(iv):
        if jv == 1:
            grid = []
            vis = []
            dist = []
            for k in lines_in:
                grid.append([alpha.index(x) for x in k])  
                vis.append([False for x in k])
                dist.append([20000000 for x in k])
            #print(i, j)
            start_poses.append([i, j])
            
            distances.append(BFS(grid, vis, i, j))

d2 =[]
for i in distances:
    if i != None:
        d2.append(i)
        
pp(min(d2))        
