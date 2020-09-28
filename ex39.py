# Create mapping of states with abbrevation
states = { 'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}
# Create a basic set of states and some cities in them

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

# Add More cities
cities['NY'] = 'New York'
cities["OR"] = 'Portland'

# print out some cities
print('-' * 10) # Eme 10 car - print dekat
print("NY states has:", cities['NY'])
print("OR states has:", cities['OR'])

# print some states
print('-' * 10)
print("Michigan states abbrevation is", states['Michigan'] )
print("Florida's abbrevations is:", states['Florida'])

# Do it by using states then cities dict
print('-' * 10)
print('Michigan has:', cities[states['Michigan']])
print('Michigan has:', cities['MI']) # Eme wekw ewey serewe be rregey tr.

# Print every states abbrevations
print('-' * 10)
for state, abbrev in list(states.items()): # lera boman dyary krd states, abbrev chwnke listeke xoy pek hatwe le state, abbrevations..
    # bekardet bas bo away bmanewe list ekebe reky dabnret w eger btawe be jmare peyandabchet.
    print("{} abbrevation is {}".format(state, abbrev))

# Print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(" {} has the city {}".format(abbrev, city))

# Now print both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print("{} abbrevation is {}".format(state, abbrev))
    print("{} has the city {}".format(abbrev, cities[abbrev]))


print('-' * 10)

# Safely get abbrevation by state that moght not be there
state = states.get('Texas')
if not state:
    print("SORRY, No Texas")

print('-' * 10)
city = cities.get('TX', 'Does Not Exist')
print(f"The city for state 'TX' is : {city}")

# List bekardet bo listy chend shtek be ryzkrawy bellam dict bo yakxstny yan le yekchwny chend brrgeyeke
# ke pey dewtret keys legell values.
# Dict katek bekardet ke btewe nrxek hellgryt w bedway nrxeky tr bgerreyt wate be dwa gerran ya shwenkewtn.
# list bo gerran be dway listek degerre ke ryzkraw bn w be jmareyy boyan bchyn wate be pey jmare bangyan bkey.