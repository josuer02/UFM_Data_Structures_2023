from Act2 import Playlist, Cancion
from data_persistence import pickle_object, unpickle_object
from memory_profiler import profile
import time, sys


#Creamos la playlist


@profile
def tenMB(playlist):
    for i in range(1450): #Aca deberia de ir 10400 pero peta el pickle
        playlist.insert_song('BD01', 'Agosto', 'Bad bunny', 'Un Verano Sin Ti')
        playlist.insert_song('BD02', 'Otro Atardecer', 'Bad bunny', 'Un Verano Sin Ti')
        playlist.insert_song('BD03', 'Moscow Mule', 'Bad bunny', 'Un Verano Sin Ti')
        playlist.insert_song('RW01', 'Old Skull', 'Rauw Alejandro', 'Viceversa')
        playlist.insert_song('RW02', 'Desenfocao', 'Rauw Alejandro', 'Viceversa')
        playlist.insert_song('FD01', 'CHORRITO PA LAS ANIMAS', 'FEID', 'SIXDO')
        playlist.insert_song('FD02', 'Belixe', 'FEID', 'Feliz Cumpleaños FERXXO')

    return playlist     

@profile
def traverse(playlist):
    tiempo0 = time.time()
    for node in playlist:
        pass
    tiempo1 = time.time()
    total = tiempo1-tiempo0
    print('-------------------------------------------------')
    print("El tiempo que tardo normal fue de: ", total ,'s')
    print('-------------------------------------------------')

@profile
def traverse_pickle(playlist):
    file_path='./saved_ll'
    print(sys.getrecursionlimit()) # Prints 1000
    print(sys.setrecursionlimit(1000)) # Set the limit to 2000
    sys.setrecursionlimit(100000)
    print(sys.getrecursionlimit())
    pickle_object(playlist, file_path)
    unpickle_playlist = unpickle_object(file_path)
    tiempo0 = time.time()
    for node in unpickle_playlist:
        pass
    tiempo1 = time.time()
    total = tiempo1-tiempo0
    print('-------------------------------------------------')
    print("El tiempo que tardo con data_persistance fue de: ", total ,'s')
    print('-------------------------------------------------')





@profile
def main():
    playlist = Playlist()
    tenMB(playlist)
    traverse(playlist)
    print(sys.getrecursionlimit()) # Prints 1000
    print(sys.setrecursionlimit(1000)) # Set the limit to 2000
    sys.setrecursionlimit(100000)
    print(sys.getrecursionlimit())
    traverse_pickle(playlist)
    
    


main()