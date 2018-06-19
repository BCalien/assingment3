

def NumberToSymbol(number):
    switch={ #Umwandlung von Zahl zu Buchstabe
        0:"A",
        1:"c",
        2:"G",
        3:"T"}
    return switch.get(number)

def NumberToPattern(number, kmer):
    patternsymbol= ""
    for i in range(kmer, 0, -1): #Schleife von kmer bis 0
        temp= int(number/4) #Variable gespeichert als Dezimahlzahl
        if(number>3):
            symbol=NumberToSymbol(number%4) #wenn number größer als drei ist dann Modula von number mit kmer/4 und auf den Rest NumberToSymbol-Funktion anwenden
        else: #ansonsten:
            symbol=NumberToSymbol(number) #keine Umrechnung nötigt, einfach Funktion NumberToSymbol anwenden genügt
        patternsymbol += symbol #Patternsymbol um symbol ergänzen
        number = temp #Aktualisierung von number für den nächsten Schleifendurchlauf
    return patternsymbol[::-1]

def medianstring (k,seqs):
    geskmers=[0]*(4**k) #array mit definierter Größe
    for i in range (0, 4**k): #Schleife von  0 bis 4^k
        geskmers[i]=NumberToPattern(i, k) #Ergebnis von NumberToPattern in geskmers speichern
    minDistance=float("inf") #minDistance zuerst auf unendlich setzen damit Ergebnis auf jeden Fall kleiner ist
    Dist={}#Dictonairy
    for kmer in geskmers: #Schleife für kmere in geskmers
        result=0
        for sequence in seqs: #Schleife für alle kmere in seqs (Sequences)
            distance= float("inf")
            for i in range (len(sequence)-k+1): #Überprüfung der kmere innerhalb der sequence
                temp=0
                spezkmer=sequence[i:i+k] #kmer in sequence ist spezkmer
                for x,y in zip(kmer, spezkmer):
                    if x != y:
                        temp=temp+1 #wenn x ungleich y muss temp um eins erhöht werden
                if temp< distance:
                    distance=temp #wenn temp kleiner als distnace, dann ist der Wert von distance absofort neues temp
            result= result+distance
        if result<minDistance:
            minDistance=result #für die minimale Distance result nur als neue minDistance, wenn es kleiner als bisheriges minDistance ist
        Dist[kmer]=result

    return min(Dist, key=Dist.get) #return kleinsten Wert aus Liste

k=3 #gegebene Kmerlänge
seqs=["AAATTGACGCAT","GACGACCACGTT","CGTCAGCGCCTG","GCTGAGCACCGG","AGTACGGGACAG"] #gegebene Strings
result=medianstring(k, seqs)
print(result) #Ausgabe des Ergebnisses

k=6 #zweites Beispiel von Rosalind
seqs=["TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT","CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA","TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT","TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA","ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG","TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA","TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC","GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA","CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG","CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"]
result=medianstring(k, seqs)
print(result)


