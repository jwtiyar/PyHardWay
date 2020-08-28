print("Lets practice everything")
print("you\'d need to know \'bout escapes with \\ that do:")
print('\nnelines and \t tabs')

poem="""
\t دۆزه‌خ له‌ عیشقه‌ خاڵی و جه‌ننه‌ت له‌ ده‌ردو داغ
عاشق له‌ حه‌شریشا نیه‌تی جێ دڵێ فه‌راغ
گه‌ر عازیمی زیاره‌تی كه‌عبه‌ی مه‌حه‌ببه‌تی
رێ : چاكی دڵ ، عه‌لامه‌تی رێ : داغ و شوێنی داغ """
print("=" * 10)
print(poem)
print('-' * 10)

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(hi):
    jelly_beans = hi * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("with starting point of {}".format(start_point))

# Above one statments is same as below one to print value.

print(f"we have {beans} beans, {jars} jars, and {crates} crates.")
start_point = start_point / 10

print("We can also do it this way")
formula = secret_formula(start_point)

#this is an easy way to apply a list to format string
print("we have {} benas, {} jars, and {} crates".format(*formula))