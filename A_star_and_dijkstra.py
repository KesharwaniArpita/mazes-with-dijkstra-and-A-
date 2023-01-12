from pyamaze import maze,agent,textLabel,COLOR
from queue import PriorityQueue
import datetime

def dijkstra(m):
    count=0
    unvisited={n:float('inf') for n in m.grid}#storing the nodes in a dictionary with nodes as the keys and value to be infinity
    unvisited[(m.rows,m.cols)]=0# start node
    visited={}#this dictionary will store the shortest path 
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)# this will give the node with minimum edge weight
        visited[currCell]=unvisited[currCell]
        count+=1
        if currCell==(1,1):
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:# checking if their is a path in the following drection
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:# if the current cell is in visited dictionary , we continue the process with neighbour cells
                    continue
                tempDist= unvisited[currCell]+1
                if tempDist < unvisited[childCell]:#checking the new weight ,if it is lesser then it gets updated
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)#the node is then deleted from unvisited dictionary
    fwdPath={}
    cell=(1,1)
    while cell!=(m.rows,m.cols):
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    t2=datetime.datetime.now()
    textLabel(m,'Dijkstra loop count:',count)
    return fwdPath,visited[(1,1)]


def h(start,end):# to calculate mahhattan distance heuristic
    x1,y1=start
    x2,y2=end
    return abs(x1-x2) + abs(y1-y2)

def aStar(m):
    count=0
    t1=datetime.datetime.now()
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))
    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        count+=1
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))
                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    t2=datetime.datetime.now()
    textLabel(m,'A Star loop count: ',count)
    return fwdPath

m=maze(40,40)
m.CreateMaze(loopPercent=50)
t1=datetime.datetime.now()
path=aStar(m)
t2=datetime.datetime.now()
l=textLabel(m,'A Star Path Length: ',len(path)+1)
textLabel(m,'Time taken by A Star: ',t2-t1)
a=agent(m,filled=True,footprints=True)
m.tracePath({a:path})
t3=datetime.datetime.now()
path2=dijkstra(m)
t4=datetime.datetime.now()
c=textLabel(m,'Dijkstra path length:',len(path)+1)
textLabel(m,'Time taken by Dijkstra :',t4-t3)
a=agent(m,color=COLOR.red,filled=True,footprints=True)
m.tracePath({a:path})
m.run()
