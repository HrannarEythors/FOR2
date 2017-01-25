#Hrannar Örn Eyþórsonn

#Dæmi 1
print("<-----DÆMI 1----->")
#Beðið er um tölur
tala = int(input("Sláðu inn eina tölu "))
tala2 = int(input("Sláðu inn aðra tölu "))
#Reiknað margfeldi og summu
margfeldi = tala*tala2
suma = tala+tala2
#Sýnt notanda niðurstöður
print("\nSumma",tala,"og",tala2,"er =",suma)
print("Margfeldi",tala,"og",tala2,"er =",margfeldi)
print()

#Dæmi 2
print("<-----Dæmi 2----->")
#Beðið er um nafn og spurt hvort hann sé með milli þafn strax á eftir
fornafn = input("Hverrt er fornafn þitt? ")
spurning = input("Ertu með millinafn? j fyrir já ").lower()
#Ef svarað er já
if spurning == "j":
    #Beðið er um milli og eftir nafn
    millinafn = input("Hverrt er millinafn þitt? ")
    eftirnafn = input("Hvert er eftirnafn þitt? ")
    print("Halló",fornafn,millinafn,eftirnafn)
    print()
#Ef ekki er svarað já
else:
    #Beðið er um eftirnafn
    eftirnafn = input("Hvert er eftirnafn þitt? ")
    print("Halló",fornafn,eftirnafn)
    print()

#Dæmi 3
print("<-----DÆMI 3----->")
#Bið um texta
texti = input("Skrifaðu texta ")
#Bý til lista
hastafur = []
lagstafur = []
lageftirha = []
teljari = 0
#Keyri þeta jafnt oft og lengd textans
for x in range(len(texti)):
    teljari+=1
    #Gá hvort stafurinn sé stór
    if texti[x].isupper():
        x2 = x-x+1
        hastafur.append(x2)
        #Gá hvort stafurinn á eftir sé lágr
        if texti[teljari].islower():
            teljari2 = teljari-teljari+1
            lageftirha.append(teljari2)
    #Gá hvort stafurinn sé lágr
    if texti[x].islower():
        x2 = x-x+1
        lagstafur.append(x2)
print("Það eru",sum(hastafur),"hástafir og",sum(lagstafur),"lágstafir og koma",sum(lageftirha),"lágstafir eftir hástafi")