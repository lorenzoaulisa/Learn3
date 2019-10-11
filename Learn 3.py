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
jokeEvaluation = "Isn't that joke so funny?! You have entered the comedy area! %r"

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
print("So the duck walked up to the lemonade stand.")
print("And he said to the man, running the stand.")
print("Hey, bom, bom, bom, got any grapes?")
# Program will print a peroid 10 time
print("." * 10)
# Program will define all the end variables as the letters in the phrase "cheeseburger R KOOL!"
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
end13 = "R"
end14 = "K"
end15 = "O"
end16 = "O"
end17 = "L"
end18 = "!"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)
print(end13 + end14 + end15 + end16 + end17 + end18)

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

# Program will print all the end variables as the letters in the word cheeseburger
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


# Program will define the days
days = " Mon tue wed thu fri"
# Program will define the months
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Program will print the days
print("Here are the days: ", days)
# Program will print the months
print("Here are the months: ", months)

# Program will print There's something going on here:
# With the three double quotes.
# We'll be able to type as much as we want
# Even 4 lines if we want, or 5, or 6.
print("""
There's something going on here:
With the three double quotes.
We'll be able to type as much as we want
Even 4 lines if we want, or 5, or 6.
""")

# examine closely the difference between the %r formatter and the %s formatter
# Program will print Here are the months: 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'
print("Here are the months: %r" % months)
# Program will print Here are the months: Jan
# Feb
# Mar
# Apr
# May
# Jun
# Jul
# Aug
print("Here are the months: %s" % months)

# escape sequence redux
# Program will define tabbyCat as I'm tabbed in (So original).
tabbyCat = "\tI'm tabbed in (So original)."
# Program will define EbicCat as I'm the split\non a line
EbicCat = "I'm the split\non a line"
# Program will define backslashcat as I'm \\ a \\ cat. That likes to divide my words
backslashCat = "I'm \\ a \\ cat. That likes to divide my words"
# Program will define NaeNaeCat as a list of items it will monch apon
NaeNaeCat = """
I'll do a list:
\t* Yarn balls
\t* Aquatic Creatures
\t* Catnip\n\t*Grassy bois
"""

#Program will print these variables to come up with the result of:
#    I'm tabbed in (So original).
# I'm the split
# on a line
# I'm \ a \ cat. That likes to divide my words

# I'll do a list:
# 	* Yarn balls
# 	* Aquatic Creatures
# 	* Catnip
# 	*Grassy bois
print(tabbyCat)
print(EbicCat)
print(backslashCat)
print(NaeNaeCat)

# Escape Seq              What it does?
print("\\")      # Backslash
print("\'")      # Quote
print("\"")      # Double quote
print("\a ")     # ASCII BEL (?)
print("a\bb ")   # Backspace
print("aa\fdd ") # Down of one line, keep same column

x='\N{BLACK SPADE SUIT}'# \N{name} something to do with Unicode symbols to make special characters
print(x)

print("\r") # Move the character to the beginning of the line without erasing
print("\t")  # Tab

x='\u0144'  # \ Uxxxx: unicode with hexidecimals
print(x)

x='\U0001f63f' #\ Uxxxxxxxx" unicode with hexidecimals
print(x)

x='\o12' #\ ooo" unicode with octaldecimals
print(x)

x='\xe2'  #\ Hxx something to do with hex conversion
print(x)

# What does the following code do:
#   While true:
#       for i in ["/", "-", "|", "//", "|"]:
#            print("s\r" % i, end='')
#   Can you use ''' instead of """ ?

# Program will define fingers as How many fingers do you have?
fingers = input("How many fingers do you have?")
# Program will define thickness as How thick are you?
thickness = input("How thick are you?")

# Program will print So, you have '999999' amount of fingers and '99999999999999999' units of
# Thickness after the programer enters the answers that the program will use to write the sentence
print("So, you have %r amount of fingers and %r units of thickness" % (fingers, thickness))

# Ask 4 or more questions and handle those responses
# q: When were hexadecimals invented?
# a: Hex, short for "hexadecimal base counting", was invented in France in the year 770 AD
# q: When were octodecimals invented?
# a: Octal number system was being used in papers as far as 1668, so it must have already been invented at least
# By the beginning of the seventeeth century
# q: Why do we use hexidecimals in programming?
# a: The main reason why we use hexadecimal numbers is because it is much easier to express binary number
# representations in hex than it is in any other base number system.
# q: What is the octal numeral system?
# a: It is the base-8 number system, and uses the digits 0 to 7. ... In the octal system each place is a power of eight.
# q: What does \a ASCII BEL do?\
# a: Apparently, the Bell character is the control code used to sound an audible bell or tone in order to alert the user.

