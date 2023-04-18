from memory_profiler import profile
import random
import sys
import time
from data_persistence import pickle, pickle_object


class Node:
    '''
    Node object.
    Args:
        data (str): string value to store in node
    Attributes:
        data (str): value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__(self, data: str):
        self.data = data
        self.next = None


    def __repr__(self):
        return '| Data: {} |'.format(self.data)


class LinkedList:
    '''
    Linked List object.
    Args:
        None
    Attributes:
        start (Node): pointer to first node in list
    '''

    def __init__(self):
        self.start = None


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.data)

        nodes.append("NIL")
        return " --> ".join(nodes)


    def traverse(self):
        '''
        Navigates every node in the list.
        Args:
            None
        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.
        Args:
            None
        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.
        Args:
            new_node (Node): node to be inserted
        Returns:
            None
        '''

        new_node.next = self.start
        self.start = new_node


    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.
        Args:
            new_node (Node): node to be inserted
        Returns:
            None
        '''

        if self.start is None:
            self.start = new_node

        else:
            for current_node in self:
                pass

            current_node.next = new_node


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.
        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                return
            
            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.
        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))
    
    def search(self, value: str):

        current_node = self.start
        pos = 0

        while current_node is not None:
            if current_node.data == value:
                return pos

            current_node = current_node.next
            pos += 1

        return None

class Cancion:


    def __init__(self, ID, Name, Artist, Album):
        self.ID = ID
        self.Name = Name
        self.Artist = Artist
        self.Album = Album
        self.next = None
        self.prev = None

class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None
        self.length = 0
    
    def __iter__(self):

        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next
    
    def insert_song (self, ID, Name, Artist, Album):

        new_song = Cancion(ID, Name, Artist, Album)
        if self.head is None:
            self.head = new_song
            self.tail = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song
        self.length +=1

    def play(self):

        if self.current_node is None:
            self.current_node = self.head
        print("Ahora suena: {} de {} " .format(self.current_node.Name, self.current_node.Artist))
    
    def Next(self):

        if self.current_node is None:
            self.current_node = self.head
        else:
            if self.current_node.next is not None:
                self.current_node = self.current_node.next
        print("Ahora suena: {} de {} " .format(self.current_node.Name, self.current_node.Artist))

    def previous(self):

        if self.current_node is None:
            self.current_node = self.head
        else:
            if self.current_node.prev is not None:
                self.current_node = self.current_node.prev
        print("Ahora suena: {} de {} " .format(self.current_node.Name, self.current_node.Artist))

    def search_by_name(self, Name):

        for cancion in self:
            if cancion.Name == Name:
                print("Cancion {} encontrada, autor: {} " .format(self.current_node.Name, self.current_node.Artist))

    def search_by_artist(self, Artist):

        encontradas = []
        for cancion in self:
            if cancion.Artist == Artist:
                encontradas.append(cancion.Name)
        print('Canciones de {} encontradas: '.format(self.current_node.Artist), encontradas)
    
    def playlistlen(self):

        print('La playlist tiene {} canciones :)'.format(self.length))
    
    def show_details(self):

        if self.current_node is not None:
            cancion = self.current_node
            print('Los detalles de la cancion son: ')
            print('Nombre: {} | Artista: {} | Album: {}'.format(cancion.Name, cancion.Artist, cancion.Album))

    def shuffle(self):

        import random
        canciones = [cancion for cancion in self]
        random.shuffle(canciones)
        self.head = canciones [0]
        self.tail = canciones [-1]
        for i in range(len(canciones)-1):
            canciones[i].next = canciones[i+1]
            canciones[i+1].prev = canciones[i]
        self.current_node = self.head
        print("Ahora suena: {} de {} " .format(self.current_node.Name, self.current_node.Artist))

    

