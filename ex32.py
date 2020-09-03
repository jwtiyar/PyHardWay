the_count = [1, 2, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'peenies', 2, 'dimes', 3, 'quartesrs']

#The first kind of for-loops goes through a list
for number in the_count:
    print(f'This count {the_count}')
    
# Same as above
for fruit in fruits:
    print("a fruit of type: {}".format(fruits))
    
#We can go throught mixed lists too
#Notice we have to use {} since we dont know whats in it
for i in change:
    print("I got {}".format(i))

#we can also build lists, first start with an emply on
for i in range(0,6):
    print(i)
    
elements = []
#elements[:] = range(5)
#then use the range function to do 0 to 5 counts.
elements.append(1)
#elements.insert(3,8)
#elements.extend([87,34,65])
print("This is new elemtns: {}".format(elements))
    

#We can print them too
for i in elements:
    print("elemetns become: {}".format(i))
    
