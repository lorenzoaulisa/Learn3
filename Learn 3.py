# More strings and text

# Program will say, "There are 10 types of peoples."
x = "There are %d types of peoples." % 10
# Program defines binary
binary = "binary"
# Program defines doNot
doNot = "don't"
#Program will say, "Those who know binary and those who don't"
y = "Those who know %s and those who %s" % (binary, doNot)

#Program will print the variable x
print(x)
#Program will print the variable y
print(y)

#Program will say, "I said:'There are 10 types of peoples.'.:"
print("I said:%r.:" % x)
#Program will say, "I also said: 'Those who know binary and those who don't'."
print("I also said: '%s'." % y)

#Program will define hilarious as "True"
hilarious = True
#Program will define jokeEvaluation as "Isn't that joke so funny?! %r"
jokeEvaluation = "Isn't that joke so funny?! %r"

#Program will say, "Isn't that joke so funny?! True"
print(jokeEvaluation % hilarious)

#Program will define w as "This is the left side of..."
w = "This is the left side of..."
#Program will define e as "a string with a right side"
e = "a string with a right side"
#Program will print "This is the left side of...a string with a right side"
print(w+e)

# More printing fun
#Program will print "Mary had a little lamb"
print("Mary had a little lamb")
#Program will print "Its fleece was white as snow."
print("Its fleece was white as %s." % 'snow')
#Program will print "And everywhere that mary went."
print("And everywhere that mary went.")
#Program will print a peroid 10 time
print("." * 10)
#Program will define all the end variables as the letters in the word cheeseburger
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