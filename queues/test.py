from queue import LinearQueue, CircularQueue



# q=LinearQueue(5)
# print(q)

# val = q.dequeue()

# q.enqueue('A')
# print(q)
# q.enqueue('B')
# print(q)
# q.enqueue('C')
# print(q)

# #busqueda
# print('Searche A: ', q.search('A'))
# print('Searche F: ', q.search('F'))
# q.enqueue('D')
# print(q)
# q.enqueue('E')
# print(q)
# q.enqueue('EX')
# print(q)


# #Eliminar

# val = q.dequeue()
# print(q)
# print('Element dequeued: {}'.format(val))

# val = q.dequeue()
# print(q)
# print('Element dequeued: {}'.format(val))

# val = q.dequeue()
# print(q)
# print('Element dequeued: {}'.format(val))

# #peek
# print('Element peeked: ', q.peek())

# val = q.dequeue()
# print(q)
# print('Element dequeued: {}'.format(val))

# val = q.dequeue()
# print(q)
# print('Element dequeued: {}'.format(val))

# #Underflow 2 escenario
# val = q.dequeue()

##CircularQueue
#Iniciamos la circularQueue
w=CircularQueue(5)
print(w)
#llenamos la Queue
w.enqueue('A')
print(w)
w.enqueue('B')
print(w)
w.enqueue('C')
print(w)
w.enqueue('D')
print(w)
w.enqueue('E')
print(w)
#Queue OverFlow
w.enqueue('F')
print(w)
# Dequeue
w.dequeue()
print(w)
w.dequeue()
print(w)
w.dequeue()
print(w)
w.dequeue()
print(w)
w.dequeue()
print(w)
#Underflow
w.dequeue()
print(w)
#Search
print('Searche E: ', w.search('E'))
#Peek
print('Element peeked: ', w.peek())