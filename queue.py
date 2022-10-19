#queue implementation
global queue
queue=[]

"""Queue Functionality"""
def enqueue(item):
    queue.append(item)

def dequeue():
    temp=queue[0]
    del queue[0]
    return temp

def isempty():
    if len(queue)==0:
        return True
    else:
        return False     

enqueue(2)
enqueue(9)
enqueue(4)
dequeue()
print(queue)