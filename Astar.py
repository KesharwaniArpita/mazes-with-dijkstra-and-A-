from pyamaze import maze,agent,textLabel,COLOR
from queue import PriorityQueue
import datetime

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
m.run()
