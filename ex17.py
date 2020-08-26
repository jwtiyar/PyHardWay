from sys import argv
from os.path import exists
# exists eshy eweye bzane fllan sht heye yan na (True or False)
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")
print(f"does the file exust? {exists(to_file)}")
print("Ready hit enter or ctrl + c to cancel")
input()
out_file = open(to_file, 'a')
out_file.write(indata)
print("Bashe, Tewaw")
out_file.close()
in_file.close()