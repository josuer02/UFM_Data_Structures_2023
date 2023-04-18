from stack import Stack
from data_persistence import pickle_object, unpickle_object
from memory_profiler import profile
import time, sys


#Creamos la playlist


@profile
def tenMB(stacki):
    for i in range(10000): #Aca deberia de ir 10400 pero peta el pickle
        stacki.push('BD')
        stacki.push('Bb')
        stacki.push('Bd')
        stacki.push('RW')
        # playlist.insert_song('RW02', 'Desenfocao', 'Rauw Alejandro', 'Viceversa')
        # playlist.insert_song('FD01', 'CHORRITO PA LAS ANIMAS', 'FEID', 'SIXDO')
        # playlist.insert_song('FD02', 'Belixe', 'FEID', 'Feliz Cumpleaños FERXXO')

    return stacki     

#@profile
def traverse(playlist):
    tiempo0 = time.time()
    for node in playlist:
        pass
    tiempo1 = time.time()
    total = tiempo1-tiempo0
    print('-------------------------------------------------')
    print("El tiempo que tardo normal fue de: ", total ,'s')
    print('-------------------------------------------------')

#@profile
def traverse_pickle(stack):
    file_path='./Ejercicio en clase/saved_stack'
    sys.setrecursionlimit(1000000)
    pickle_object(stack, file_path)




@profile
def main():
    stacki = Stack(13099000)
    tenMB(stacki)
    #traverse(stacki)
    sys.setrecursionlimit(100000000)
    print(sys.getrecursionlimit())
    traverse_pickle(stacki)
    
    


main()