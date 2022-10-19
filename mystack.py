#stack implementation
global stack
stack=[]

""""stack functionality"""
def push(num):
    stack.append(num)

def pop():
    temp=stack[-1]
    del stack[-1]
    return temp

def isempty():
    if len(stack)==0:
        return True
    else:
        return False

def peak():
    return stack[-1]

