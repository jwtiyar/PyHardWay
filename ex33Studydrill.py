#Study Drill 3
# Lere dellet function ek drwt bke bellam xoman btwanyn jmarekan zyad bkeyn be dw draw
numbers = [] 
jalo = 0
def zyadkrdn2(r, jelo):
    i = 0
    while i < r:
        numbers.append(i) 
        i += jelo 
        print("Study Drills 3: ", numbers)
        
zyadkrdn2(6, 2) # Lere pey delleyn 6 dane brro be 2.

# Study drills 5
#Lere dellet range bekarbene bellam drawy dwem xot boy bnere be function.
numbers = [] 
def forloop(r):
    i = 0
    for i in range(0,6):
        
        numbers.append(i)
        i = i + 1
        print("Study Drills 5{}".format(numbers))

forloop(5)

#Study Drill 1
# Lere dellet xoman ba function draweky bo bneryn
def befankshon(draw):
    i = 0
    while i < draw:
        numbers.append(draw)
        i = i + 1
        print("Study drills 1", numbers)  
        
befankshon(9)  