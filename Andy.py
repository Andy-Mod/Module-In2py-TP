Andy = {'SDA':[17, 18, 15],
        'Python':[16, 15, 19],
        'Anglais':[14, 15, 18],
        'LTP':[12, 12, 16],
        'Calcul Matriciel':[14, 8, 17],
        'SE':[12, 12, 12],
        'Services Réseaux':[15, 15, 12]}
moyenne = []
moy = (Andy['SDA'][1] + Andy['SDA'][2] + Andy['SDA'][2])/3
moyenne.append(moy)

moy = (Andy['Python'][1] + Andy['SDA'][2] + Andy['SDA'][2])/3
moyenne.append(moy)

moy = (Andy['Anglais'][1] + Andy['SDA'][2] + Andy['SDA'][2])/3
moyenne.append(moy)

moy = (Andy['LTP'][1] + Andy['SDA'][2] + Andy['SDA'][2])/3
moyenne.append(moy)

moy = (Andy['Calcul Matriciel'][1] + Andy['SDA'][2] + Andy['SDA'][2])/3
moyenne.append(moy)

moy = (Andy['SE'][1] + Andy['SDA'][2] + Andy['SDA'][2])/3
moyenne.append(moy)

moy = (Andy['Services Réseaux'][1] + Andy['SDA'][2] + Andy['SDA'][2])/3
moyenne.append(moy)


Moy = (moyenne[0]+moyenne[1]+moyenne[2]+moyenne[3]+moyenne[4]+moyenne[5]+moyenne[6])/7


print(Moy)

#EO
L = list(range(1, 11))
print(L)

L[0]+=11
L[1]+=11
L[2]+=11
L[3]+=11
L[4]+=11
L[5]+=11
L[6]+=11
L[7]+=11
L[8]+=11
L[9]+=11
print(L)

L.append(22)
impair = L[1::2]
pair =  L[0::2]
print(pair, impair)
L.extend([23, 24])
L.pop(3)

#E1
d = {'nom':'Dupuis', 'prenom':'Jacque', 'age':30}
d['prenom'] = 'Jacques'
print(d.keys())
print(d.values())
print(d)
phrase = d['prenom']+' '+d['nom']+' a '+ str(d['age'])+' ans.'
print(phrase)
