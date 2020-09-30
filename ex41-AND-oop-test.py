import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDs = []

PHRASES = {"class %%%(%%%)": "make class named %%% that is-a %%% , "," class %%%(object):\n\tdef __init__(self,***)": "class %%% has-a __init__ which takes (self,***)",
"class %%%(object):\n\t def ***(self, @@@) ": "class %%% has-a function **** that takes self and @@@", "*** = %%%()": "set *** to an instance of class %%%", "***.***(@@@)":" from *** get the function *** and call it with @@@ ",
"***.***='***": "from *** get the *** atribute and set it to '***'"}

#do they want to drill phrases first

if len(sys.argv) == 2 and sys.argv[1] == "english":
    phrase_first = True
else:
    phrase_first = False

#load up the words from the website

for word in urlopen(WORD_URL).readlines():
    WORDs.append(str(word.strip(), encoding="utf-8"))
#strip bekardet bo labrdny hemw boshayyyek le pesh w dway string eke.
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDs, snippet.count("%%%"))]
    other_names = random.sample(WORDs, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        #count jmarey ew carane dedat ke wshekey tya baskrawa yan drawa
        param_count = random.randint(1,3)
        # bekardet bo pyshandany jmareyeky random ke dekret herdwkyany tya bet we etwany dyraybkey chon destpebkat (start, stop) yan step.
        param_names.append(', '.join(random.sample(WORDs, param_count)))
    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake paerameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)
    return results

#keep going untill they hit CTRL+D

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if phrase_first:
                question, answer = answer, question
            print(question)

            input("< ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
#tEWAW