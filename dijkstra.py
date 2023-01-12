from pyamaze import maze,agent,COLOR,textLabel
import datetime
def dijkstra(m):
    count=0
    t1=datetime.datetime.now()
    unvisited={n:float('inf') for n in m.grid}
    unvisited[(m.rows,m.cols)]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        count+=1
        if currCell==(1,1):
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=(1,1)
    while cell!=(m.rows,m.cols):
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    t2=datetime.datetime.now()
    textLabel(myMaze,'Dijkstra loop count:',count)
    textLabel(myMaze,'Time taken by Dijkstra :',t2-t1)
    return fwdPath,visited[(1,1)]
            



if __name__=='__main__':
    myMaze=maze(25,30)
    myMaze.CreateMaze(loopPercent=100)
    

    

    
    path,c=dijkstra(myMaze)
    textLabel(myMaze,'Dijkstra path length:',c)

    
    a=agent(myMaze,color=COLOR.cyan,footprints=True)
    myMaze.tracePath({a:path})


    myMaze.run()
