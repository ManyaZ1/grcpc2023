from time import time
def parenthesis(ls):
    stack=[]
    for element in ls:
        if element=='(':
            stack.append(element)
        if element==')':
            if not len(stack):return 0
            else:stack.pop()
    if len(stack)==0:return 1
    return 0
def parser(i):
    f=open(f'input_{i:02}_containterlogs.in','r')
    length=f.readline()
    s=f.readline().rstrip() #sos exei eof sto telos
    f.close()
    ls=[]
    for letter in s: 
        if letter.isupper():
            ls.append(')')
        else: ls.append('(')
    return ls
def solution(i):
    ls=parser(i)
    val=parenthesis(ls)
    return val
def checker(i):
    f=open(f'input_{i:02}_containterlogs.ans','r')
    value=int(f.readline().rstrip())
    #print(value)
    return value
def main():
    for i in range(10):
        val=solution(i)
        ans=checker(i)
        if val!=ans:print(f"problem at {i}")
    return
if __name__=="__main__":
    start=time()
    main()
    end=time()
    print(f"t={end-start}")
    print(solution(7))
    #print(ls)
    #if parenthesis(ls):print("valid")
    #else:print("invalid")