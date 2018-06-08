import random
from threading import Thread
from multiprocessing import Process
import time

"""
Auteur: Jalil Dear Muesli 2018
Description: Test des differents technologies permettant de paraleliser
les traitements afin de gagner du temps d'execution
"""

size = 20000000   # Nbr de nombre aleatoire a rajouter a la liste
threads = 6 # Nbr de threads a creer
my_list = []
for i in xrange(0,threads):
    my_list.append([])

# Fonction affichant le temps d'execution du programme
def giveMeTime(message):
    interval = time.time() - start_time
    print(message + ' : Total time in seconds: ' + str(interval))
    return

def func(count, mylist):
    for i in range(count):
        mylist.append(random.random())

# Fct pour gerer les Threads
def multithreaded():
    jobs = []
    for i in xrange(0, threads):
        thread = Thread(target=func,args=(size,my_list[i]))
        jobs.append(thread)
    # On lance nos threads
    for j in jobs:
        j.start() 
    # On attend que tout nos threads ont termine avant de continuer
    for j in jobs:
        j.join()

# On n'utilise qu'un process et aucun threads
def simple():
    for i in xrange(0, threads):
        func(size,my_list[i])

# Fct pour gerer les process que l'on a ajoute
def multiprocessed():
    processes = []
    for i in xrange(0, threads):
        p = Process(target=func,args=(size,my_list[i]))
        processes.append(p)
    # On lance les processus
    for p in processes:
        p.start()
    # On attend que tous les processus ont finis leur execution
    # avant de continuer
    for p in processes:
        p.join()


if __name__ == "__main__":

    start_time = time.time()
    multithreaded()
    giveMeTime("multithreaded")
    start_time = time.time()
    simple()
    giveMeTime("simple")
    start_time = time.time()
    multiprocessed()
    giveMeTime("multiprocessed")