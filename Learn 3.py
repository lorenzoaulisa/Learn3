# More strings and text

# Program will say, "There are 10 types of peoples."
x = "There are %d types of peoples." % 10
# Program defines binary
binary = "binary"
# Program defines doNot
doNot = "don't"
# Program will say, "Those who know binary and those who don't"
y = "Those who know %s and those who %s" % (binary, doNot)

# Program will print the variable x
print(x)
# Program will print the variable y
print(y)

# Program will say, "I said:'There are 10 types of peoples.'.:"
print("I said:%r.:" % x)
# Program will say, "I also said: 'Those who know binary and those who don't'."
print("I also said: '%s'." % y)

# Program will define hilarious as "True"
hilarious = True
# Program will define jokeEvaluation as "Isn't that joke so funny?! %r"
jokeEvaluation = "Isn't that joke so funny?! %r"

# Program will say, "Isn't that joke so funny?! True"
print(jokeEvaluation % hilarious)

# Program will define w as "This is the left side of..."
w = "This is the left side of..."
# Program will define e as "a string with a right side"
e = "a string with a right side"
# Program will print "This is the left side of...a string with a right side"
print(w+e)

# More printing fun
# Program will print "Mary had a little lamb"
print("Mary had a little lamb")
# Program will print "Its fleece was white as snow."
print("Its fleece was white as %s." % 'snow')
# Program will print "And everywhere that mary went."
print("And everywhere that mary went.")
# Program will print a peroid 10 time
print("." * 10)
# Program will define all the end variables as the letters in the word cheeseburger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

# But wait theres more
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("Hecc", "Hicc", "Hacc", "Hucc"))
print(formatter % (True, False, True, True))
print(formatter % (formatter, formatter, formatter, formatter))

# Why do we use %r instead of %s in the above example?
# Because we want quotes around the string and also to eliminate special characters
# Which should I use on a regular basis?
# In my opinion I would say %s because I want to use special characters if I need them. I can always add quotes around!
# Why does %r sometimes give me quotes around the things?
# %r put quotes around things defined as strings

days = " Mon tue wed thu fri"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here:
With the three double quotes.
We'll be able to type as much as we want
Even 4 lines if we want, or 5, or 6.
""")

# examine closely the difference between the %r formatter and the %s formatter
print("Here are the months: %r" % months)
print("Here are the months: %s" % months)

# escape sequence redux
tabbyCat = "\tI'm tabbed in."
persianCat = "I'm the split\non a line"
backslashCat = "I'm \\ a \\ cat."
topCat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t*Grass
"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)

# Escape Seq              What it does?
print("\\")      # backslash
print("\'")      # quote
print("\"")      # double quote
print("\a ")     # ASCII BEL (?)
print("a\bb ")   # backspace
print("aa\fdd ") # down of one line, keep same column

x='\N{BLACK SPADE SUIT}'# \N{name} something to do with Unicode symbols
print(x)

print("aaaa\rddd") #move the character to the beginning of the line without erasing
print(" \ta  ")  #tab

x='\u0144'  # \uxxxx: something to do with unicode conversion
print(x)

x='\U0001f63f' #\Uxxxxxxxx" something to do with unicode conversion
print(x)


x='\o12' #\ooo" something that does not do nothing :-( ?????
print(x)

x='\xe2'  #\hxx something to do with hex conversion
print(x)

