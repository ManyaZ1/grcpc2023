from collections import deque
from time import time
class Points:
    def __init__(self, x, y,value):
        self.x = x
        self.y = y
        self.value=value
    def __repr__(self):  
        return f"x={self.x} y={self.y} value={self.value}\t" 
    def __str__(self):  
        return f"{self.x},{self.y}" 
    
def makinput(filename):
    N,M,photo=parser(filename)
    ls=[]
    for i in range(N):
        line=[]
        for j in range(M):
           p=Points(j,i,photo[i][j])
           line.append(p)
        ls.append(line)
        
    return N,M,ls

def parser(filename):
    f = open(filename, "r")
    l= list(map(int,f.readline().split()))     #l=[lines,cols]
    photo=[]
    while True:
        linex=f.readline().rstrip()
        if not linex:
            break
        line=list(map(int,linex))
        photo.append(line)
    f.close()
    return l[0],l[1],photo

def neighbors(N,M, row, col, photo):
    indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [photo[row][col] for row, col in indices if (isValid(N,M, row, col) and photo[row][col].value==1)]

def isValid(N,M,row, col):
    return row >= 0 and col >= 0 and row < N and col <M

def solution(filename):
    lake_counter=0
    areas=[]
    #lakes=[]
    N,M,photo=makinput(filename)
    visited=set()
    for row in range(N):
        for col in range(M):
            point=photo[row][col]
            if point not in visited and point.value==1: 
                lake_counter+=1
                area=0
                qu=deque()
                qu.append(point)
                #lake=[]
                while len(qu)>0:
                    v=qu.popleft()
                    if v not in visited:
                        visited.add(v)
                        area+=1
                    #lake.append(v)
                        for w in neighbors(N,M, v.y, v.x, photo):
                            if w not in visited:
                                qu.append(w)  
                                #visited.add(w)
                #lakes.append(lake)
                #area=len(set(lake))
                areas.append(area)
            else:continue            
    return lake_counter,areas
def solution2(filename):#THIS WORKS AS WELL a bit slower
    lake_counter=0
    areas=[]
    #lakes=[]
    N,M,photo=makinput(filename)
    visited=set()
    for row in range(N):
        for col in range(M):
            point=photo[row][col]
            if point not in visited and point.value==1: 
                lake_counter+=1
                area=0
                qu=deque()
                qu.append(point)
                #lake=[]
                while len(qu)>0:
                    v=qu.popleft()
                    
                    visited.add(v)
                    area+=1
                    #lake.append(v)
                    for w in neighbors(N,M, v.y, v.x, photo):
                        if w not in visited:
                            qu.append(w)  
                            visited.add(w)
                #lakes.append(lake)
                #area=len(set(lake))
                areas.append(area)
            else:continue            
    return lake_counter,areas    
'''
def bfs(visited,photo,N,M,start):
    qu=deque()
    qu.append(start)
    while len(qu)>0:
        v=qu.popleft()
        if v not in visited:
            #visit(v)
            visited.add(v)
            if v.value==1:
               for w in neighbors(N,M, v.y, v.x, photo):
                    if w not in visited:
                        qu.append(w)
                    if w.value==1:
                        if w in visited: newlake=False
               if newlake is True: 
                   lake_counter+=1
                   print(v)
    return 1
'''
'''
def bfs(G, v):
    queue = [v]
    while len(queue) > 0:
        v = queue.pop(0)
        if not marked[v]:
            visit(v)
            marked[v] = True
            if v.value==0:
                for w in G.neighbors(v):
                    if not marked[w]:
                        queue.append(w)
            if v.value==1:
               flag=uvisited
               for w in G.neighbors(v):
                    if not marked[w]:
                        queue.append(w) 
                    if w.value==1:
                        if w in visited: flag=visited
                if flag=unvisited:lake_counter++

'''  
def checker(filenamein,filenameans):
    number,areas=solution(filenamein)
    f=open(filenameans,'r')
    number_ans=int(f.readline())
    areas_ans=list(map(int,f.readline().split()))
    #print(areas_ans)
    if (number!=number_ans):
        print(f'{filenamein} number:{number} number_ans:{number_ans}')
        return False
    areas.sort()
    if areas != areas_ans:
        print("problem")
        return False
    #else:
    #    print("ALL CORRECT")
    return True

def main():
    i=5
    start=time()
    for i in range(1,21):
        checker(f'input_{i:02}.in',f'input_{i:02}.ans')
    end=time()
    print(f"time:{end-start}")
    #number,areas=solution(f"input_{i:02}.in")
    #print(number,areas)
    '''N,M,photo=makinput("input_01.in")
    row,col=1,2
    print(neighbors(6,13,row,col,photo))'''

if __name__=='__main__':main()
