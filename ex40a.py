# Dict & Modules & Clas
# Em 3 Shte zor le yek dechn bo chonyety eshkrdn legellyan
#Dict
mystuffi = {'apple': "Iam Apples2"}
print(mystuffi['apple'])
#Module brytye le perrgey .py ke code m teda nwsywe ke brytyn le function w variable,
#Detwanm import yan bkem w bangyhsyan bkem be hoy .dot
#perrgeyekm drwst krd be nmawy mystuff.py Detwanm importy mystuff.py bkem
import mystuff
print(mystuff.apple())  #Lerewe detwanm be .dot bangybkem eme encamekey None chnwke variable m nedawe pey 
print(mystuff.tangerine) # Detwanm bangy variables kesh bkem

# Wek debynyt katek peydadechtewe ke modules wek dict waye shewazy eshkrdn legelly.
# wek ewey daway tangerine eman krdwe le file tr be nawy mystuff.py
#Wek chon le dict bangy x dekeyn le y , mebestm wtman le nawy mystuffi bangy key apple bke w value ekey
#pyshan bde ke Iam Apples2 e .
# Detwany wa byrbkeytewe ke modules shewazeky taybety dictionarye ke detwany\
# code w function w variable ..etc teda hallbgryt w be .dot bangy bkeyt.

#Enca Deyn basy class dekeyn ke ewysh le mini-module ek dechet. w be .dot bangdekret.

class MyStuff(object):
    def __init__(self): # Lera __init__ degerret bo ewey object eket bxwenetewe.
        self.tangerine = "And now A thosands years between "
        #le naw function __init__ variable eky betally tr werdegryt ke brytye le self.
        #ke detwanyt variableky drwst krawy xoty tebleyt wek tangerine.
    def apple(self):
        print("Iam CLASSSY APPLES!")
# TO class ekt instantiate krd wshey instantiate be many (create) wate drwstkrd det.
#MyStuff t instantiate krd shtekt dest kewt be nawy (object)

thing = MyStuff() # Lera bangy class ekeyt bo thing
thing.apple() # wtman le classy MyStuff function apple bena.
print(thing.tangerine) # Lere pey delleyn bo thing variabley tangerine werbgre ke string y tedaye. printy dekat.

#Hemw em Shtane ke rwnkrawetewe bo eweye to btwany Shtekan tehallkesh bkeyt w leyan tebgeyt boye hemw qsekan wekw berd damekwte lesery xot, swdyan le werbgre bo ferbwn w dway xot legell berepesh chwn hemwy cya dekeytewe 
#Leyan tedegeyt.
