from sys import argv
script, input_file = argv
def print_all(f): #Lera her shtek dabney abe, yan pesh ewe penasey value ka bkay ba variable ka ch file e werdegret.
    print(f.read())

def rewind(f):
    print(f.seek(0))

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)
print("Lets print whole file")
print_all(current_file)

print("Let's Rewind, kind of liek a tape")

rewind(current_file)

print("Lets print three line")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

x= open(input_file)
print(x.readline())