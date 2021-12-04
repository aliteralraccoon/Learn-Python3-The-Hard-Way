# Sets a string with 4 places for objects to be placed
formatter = "{} {} {} {}"
# Various tests of the formatter, all including 4 objects to be placed
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Oh no, what",
    "is going to happen",
    "when the formatter",
    "formats itself a",
))
