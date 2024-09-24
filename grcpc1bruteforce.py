from time import time

def parser(filename):
    f = open(filename, "r")
    n=f.readline()
    #print(n)
    points={}
    for i in range(int(n)):
        s=f.readline()
        x = s.split()
        point=x[0]
        cond=float(x[1])
        flex=float(x[2])
        points[point]=(flex,cond)
    return n,points
    #print(points)

def solution(filename):
    n, points = parser(filename)
    first_key = next(iter(points))
    output = {first_key: points[first_key]}  # key: A, value: (flex, cond)
    maxflex=points[first_key][1]
    maxcond=points[first_key][0]
    for key, value in points.items():
        point = key
        cond = value[0]
        flex = value[1]
        flag=0

        for keo, valo in list(output.items()):  # Iterate over a copy of the output dictionary
            condo = valo[0]
            flexo = valo[1]
            if condo < cond and flexo < flex: 
                output.pop(keo)
                output[point]=(cond,flex)
            if condo>cond and flexo>flex: flag=1
        if flag==0:
            output[point]=(cond,flex)
    return list(output.keys())

def checker():
    for i in range(24):
        filename=f"input_{i:02}_alloy.in"
        out = solution(filename)
        out.sort()
        s=''
        for element in out:
            s+=str(element)
            s+=' '
        sol=s.rstrip()
        f = open(f"input_{i:02}_alloy.ans", "r")
        ans=str(f.readline())
        ans=ans.rstrip()
        if sol != ans: print(f"porblem at {i}")

if __name__=="__main__":
    start=time()
    checker()
    stop=time()
    print(f"time: {stop-start}")