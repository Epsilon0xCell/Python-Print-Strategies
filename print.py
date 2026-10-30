# A sequence of small, independent print demonstrations. The order is the
# lesson: each block shows one behaviour, and the blocks that print on the
# same line only make sense read against the default they override, which
# is that print() ends the line with a newline.
data = "Fun secret variable"
print(data)
print("Hello World")
print(50)
print(1000)
print(3.142)
print(50, 1000, 3.142, "Hello World") # Comma separation

# printing on same line
# end="" replaces the newline, so the next print continues right where
# this one stopped; end=" " leaves exactly one space instead.
print("Hello", end="")
print("World")

print("Hello", end=" ")
print("World")

print(50)  # This line prints 50
print("Hello World")  # This line prints Hello World

# This is just a comment hanging out on its own!

# For multi-line comments, we must
# add the hashtag symbol
# each time

"""Docstrings are pretty cool
for writing longer comments
or notes about the code"""
