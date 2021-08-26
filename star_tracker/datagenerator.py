import random
import csv

def creteRandomStarData(outputFile, minMag, maxMag, starNumbers):
    file=open(outputFile,"w")
    fieldnames = ['Numero de catalogacao', 'phi', 'theta', 'Magnitude visual']
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    for x in range(starNumbers):
        writer.writerow({'Numero de catalogacao':x, 'phi':random.uniform(0,360), 'theta':random.uniform(0,180),'Magnitude visual':random.uniform(minMag,maxMag)})