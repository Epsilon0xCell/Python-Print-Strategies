# I wrote this file as a sequence of small, independent demonstrations,
# and I keep the order fixed because the order is the lesson. Each block
# shows one behaviour on its own. The same-line blocks in the middle only
# make sense against the default they override: print() ends the line
# with a newline unless I tell it not to.
#
# I start with a variable on purpose. Printing the variable prints the
# value it holds, not the name I gave it, and that difference is the
# first thing a new reader trips on.
data = "Fun secret variable"
print(data)
print("Hello World")
print(50)
print(1000)
print(3.142)
# I pass these four values in one call and let the commas do the work:
# print puts exactly one space between values on its own, so I do not
# need to add spaces inside the strings myself.
print(50, 1000, 3.142, "Hello World") # Comma separation

# printing on same line
# I use end="" here to replace the newline entirely, so the next print
# continues right where this one stopped and the two words run together.
# With end=" " I leave exactly one space instead, which is the only
# difference between the pair above and the pair below.
print("Hello", end="")
print("World")

print("Hello", end=" ")
print("World")

print(50)  # This line prints 50
print("Hello World")  # This line prints Hello World

# The rest of this file is about comments themselves, so here the
# comments are the content I am demonstrating, not notes about the
# printing above. Everything on a line after the hashtag is ignored
# when the file runs.

# This is just a comment hanging out on its own!

# For multi-line comments, we must
# add the hashtag symbol
# each time

# I need to be careful with the block below: it looks like a comment,
# but it is really a string. It only reads as documentation because it
# sits here as a bare expression that nothing uses. If I moved it, it
# would still be a string value, not a comment the interpreter skips
# by rule the way it skips hashtag lines.
"""Docstrings are pretty cool
for writing longer comments
or notes about the code"""
