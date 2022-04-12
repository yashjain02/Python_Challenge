import os
import time
import P2DC_Team_10 as file

'''
-------------------------------------
Team name: Driven By Data
Team Id: 10

Yash Kumar Jain
Mohamad Serhan
Julian esteban Oliveros forero
Qinghua Ye
-------------------------------------
'''

def readFile(filePath):

    with open(filePath, 'r') as f:
        listl = []
        for line in f:
            strip_lines = line.strip()
            listli = strip_lines.split()
            listl.append(listli)
    del listl[0]
    return listl



def startRun():

    start_time = time.time()
    GlobalRoboticSatisfaction=0
    writePathStart ="output"
    directory = 'data/'

    dictWithSubgroups = {
        "data/1_binary_landscapes.txt": 9000,
        "data/11_randomizing_paintings.txt": 12000,
        "data/110_oily_portraits.txt": 10000,
        "data/0_example.txt": 10,
        "data/10_computable_moments.txt": 2000
    }

    dictWithSubgroups2 = {
        "data/1_binary_landscapes.txt": 20,
        "data/11_randomizing_paintings.txt": 20,
        "data/110_oily_portraits.txt": 20,
        "data/0_example.txt": 20,
        "data/10_computable_moments.txt": 20
    }


    # iterate over files in
    # that directory
    for filename in os.scandir(directory):
        if filename.is_file():

            compare = filename.path

            if compare in dictWithSubgroups:
                GlobalRoboticSatisfaction = GlobalRoboticSatisfaction + file.runScript(filename.path,writePathStart+filename.path,dictWithSubgroups2[compare])

    print("--------------------------------------")
    print("GLOBAL ROBOT SATISFACTION IS: ",GlobalRoboticSatisfaction)
    print("--- %s minutes ---" % ((time.time() - start_time)/60))
    print("--------------------------------------")


startRun()