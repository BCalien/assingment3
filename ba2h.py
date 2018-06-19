

def DistancePatternString (pattern, dna):
    k=len(pattern)
    result=0
    for text in dna: #Schleife für Strings in Liste
        Distance= float("inf") #initialisiere "Anfangsdistanz", damit die erste Distanz kleiner ist als "Voreinstellung"
        for i in range(len(text)-len(pattern)+1): #Länge der Schleife endet so, dass kmerlänge exakt noch darin liegt
            temp=0
            Sequenz= text[i:i+3]
            for x,y in zip(pattern, Sequenz):
                if x != y:
                    temp=temp+1 #wenn pattern und Sequenz unterschiedlich sind dann muss temp an dieser Stelle um eins erhöht werden
            if temp<Distance:
                Distance=temp #wenn temp kleiner als die Distance ist, dann ist die Distance ab hier das neue temp
        result= result+Distance #addiere Distance zu result
    return result

def Zusammenf():
    pattern="AAA"
    dna=["TTACCTTAAC","GATATCTGTC","ACGGCGTTCG","CCCTAAAGAG","CGTCAGAGGT"]
    Distance=DistancePatternString (pattern, dna) #Speicher Ergebniss der Funktion in Distance
    print(Distance)

Zusammenf() #Rufe die Zusammenfassungsfunktion auf