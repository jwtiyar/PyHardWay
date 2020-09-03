people = 30
cars = 40
trucks = 15

if cars > people and trucks > cars:
    print(" We should take the cars")
#elif cars < pepole:
   # print("We should not take cars")

else:
    print("We cant decide")
    
if trucks > cars:
    print("THatis too many trucks")
elif trucks < cars:
    print("May be we take trucks")
else:
    print("We still cant decide")
    
if people > trucks:
    print("Alright, Let's just take trucks.")
else:
    print("Fine, Lets's stay home the.")