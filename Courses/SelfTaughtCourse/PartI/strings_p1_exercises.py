x = 'Camus'
for i in x:
    print(i)

thing = input("What is your thing? ")
who = input("Who did you send it to? ")
print(f"Yesterday I wrote a {thing}. I sent it to {who}!")

string_0 = "aldous Huxley was born in 1894."
string_0 = string_0[0].upper() + string_0[1:]
print(string_0)

string = "Where now? Who now? When now?".split('?')
for i in range(0, 3):
    string[i] = string[i] + '?'
string.pop()
print(string)

string_2 = "A screaming comes across the sky."
print(string_2.replace('s', '$'))

string_3 = "Hemingway"
print(string_3.index('m'))

string_4 = "three " + "three " + "three"
print(string_4)

string_5 = "three " * 3
print(string_5)
