#Actividad 1
#Josue Ruiz-20210418
class LinearQueue:

    def __init__(self, size: int) -> None:
        self.elements = [None]*size
        self.max =size
        self.front= -1
        self.rear= -1

    def __repr__(self):
        return 'Queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear) 

    def enqueue(self, value: str) -> None:

        if self.rear == self.max -1:
            print('Queue Overflow...') 
            return None
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0

        else: 
            self.rear += 1
        self.elements[self.rear] = value 

    def dequeue(self)-> str:
        if self.front == -1 or self.front > self.rear:
            print('Queue Underflow...')
            return None
        value = self.elements[self.front]
        self.elements[self.front] = None 
        self.front += 1
        return value  

    def search(self, key: str) -> int:
        for i in range(self.front, self.rear+1):

            if self.elements[i]==key:
                return i
        return -1    

    def peek(self) -> str:

        if self.front == -1 or self.front > self.rear:
            print('Queue Underflow...')
            return None

        return self.elements[self.front]



class CircularQueue:
    def __init__(self, size: int) -> None:
        self.elements = [None]*size
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max = size

    def __repr__(self):
        return 'Circular Queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear) 

    def enqueue(self, value:str):
        if self.size == self.max:
            print("La queue esta llena")
            return False
        else:
            self.elements[self.rear] = value
            self.rear = (self.rear + 1)% self.max   
            self.size += 1
            return True

    def dequeue(self):
        if self.size == 0:
            print("La cola esta vacia")
            return None
        else:
            value = self.elements[self.front]
            self.elements[self.front] = None
            self.front = (self.front +1) % self.max
            self.size -= 1
            return value      

    def search(self, key: str) -> int:
        if self.size == 0:
            print("La cola esta vacia")
            return None
        for i in range(self.size):
            y = (self.front + i) % self.max
            if self.elements[y] == key:
                return y
        print("Busqueda Fallida, elemento no fue encontrado")                  
        return None

    def peek(self):
        if self.size == 0:
            print("La cola esta vacia")
            return None 
        return self.elements[self.front]  

                