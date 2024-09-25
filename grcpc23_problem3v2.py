from time import time

def parser(filename):
    completed=set()
    prereq=[]
    f=open(filename,'r')
    compNum=int(f.readline())
    for course in f.readline().split():
        completed.add(course)
    reqNum=int(f.readline())
    for course in f.readline().split():
        prereq.append(course)
    f.close()
    return completed,prereq,compNum,reqNum

def sol(filename):
    completed,prereq,compNum,reqNum=parser(filename)
    if reqNum>compNum:return 0
    for course in prereq:
        if course not in completed:return 0
    return 1

def checker(s,filename):
    f=open(s+'ans','r')
    ans=int(f.readline())
    prediction=sol(filename)
    if prediction!=ans:
        print(f"wrong: {filename}")

if __name__=="__main__":
    start=time()
    for i in range(19):
        if i==2:continue
        checker(f'input_{i:02}_courses.',f'input_{i:02}_courses.in')
    end=time()
    print(f't={end-start}')
