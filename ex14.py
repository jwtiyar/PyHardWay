from sys import argv
script, user_name = argv
prompt = " > "
print(f"HI {user_name}, iam the {script} script.")
print(f"i'd like to ask you a few questions: ")
print(f"do you like {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}")
lives = input(prompt)
print(f"what kind of computer do you have?")
computer = input(prompt)
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sire where that is.
And you have {computer} computer\nnice.""")