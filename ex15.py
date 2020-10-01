

txt = open(test.txt)

print(f"here is your file {filename}")
print(txt.read())

print("Type name of file: ")
file_again = input()

txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()

#Eme xom nwsywme be bekarhenany tenha input bo testy xom:
print("Type file name: ")
nawyfile = input()
text = open(nawyfile)
print(text.read())
print(text.readline()) #readline tanha yak ryz axwenetewe.

text.close