class Knihovna:
    def __init__(self):
        self.knihy = {}

    def pridej_knihu(self, kniha):

        if kniha not in self.knihy:
            self.knihy[kniha] = 1
        else:
            self.knihy[kniha] += 1
      
    def vypujc_knihu(self, kniha):
        
        if kniha in self.knihy:
            if self.knihy[kniha] > 0:
                self.knihy[kniha] -= 1
                return True

        return False


    def vrat_pocet_kopii(self):
        count = 0
        for i in self.knihy:
            count += self.knihy[i]
        return count


    def vrat_nejcetnejsi_knihu(self):
        temp = 0
        book = ""
        for i in self.knihy:
            if self.knihy[i] > temp:
                temp = self.knihy[i]
                book = i

        if temp == 0:
            return None
        else:
            return book




knihovna = Knihovna()

knihovna.vypujc_knihu("Gang of Four")
print(knihovna.vrat_pocet_kopii())

knihovna.pridej_knihu("Gang of Four")
knihovna.pridej_knihu("Compilers")
print(knihovna.vrat_pocet_kopii())

knihovna.vypujc_knihu("Gang of Four")
knihovna.vypujc_knihu("Gang of Four")
print(knihovna.vrat_pocet_kopii())
print(knihovna.vrat_nejcetnejsi_knihu())

knihovna.pridej_knihu("Compilers")
print(knihovna.vrat_pocet_kopii())

knihovna.vypujc_knihu("Compilers")
knihovna.vypujc_knihu("Compilers")
knihovna.vypujc_knihu("Compilers")
print(knihovna.vrat_pocet_kopii())

knihovna.pridej_knihu("Python for beginners")
knihovna.pridej_knihu("Operating systems")
knihovna.pridej_knihu("Python for beginners")
knihovna.pridej_knihu("Computer architecture")
knihovna.pridej_knihu("Python for beginners")
print(knihovna.vrat_nejcetnejsi_knihu())


import csv

with open('predmety.csv') as csv_file:
    dict = {}
    count = 0
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[1] not in dict:  
            dict[row[1]] = [int(row[2]), 1]
        else:
            dict[row[1]][0] += int(row[2])
            dict[row[1]][1] += 1


    avg_dict = {}
    for i in dict:
        avg_dict[i] = dict[i][0] / dict[i][1]

    print(dict)
    print(count)     
    print(avg_dict) 


def je_palindrom(slovo):
    if slovo == slovo[::-1]:
        return True
    return False

print(je_palindrom('a')) # True
print(je_palindrom('aaa')) # True
print(je_palindrom('aba')) # True
print(je_palindrom('abc')) # False


