### Comprehension error -> SyntaxError: Generator Expression error

## 3.9
# Highlights start of generator expression

## 3.10
# Highlights all of generator expression

# print('Count:', x for x in range(10))

### Missmatched tuples in generators

## 3.9
# invalid syntax, points to for in generator

## 3.10
# highlights error, with suggested fix

# print({x, y for x, y in zip('abcd', '1234')})

### Missing comma in collection

## 3.9
# points to line after error

## 3.10
# points to error line with suggested fix

# months = {
#     1: "January", 
#     2: "Febuary"
#     3: "March"
# }

### Missing Values in dict

## 3.9
# points to line after error

## 3.10
# points to colon, expected expression after key

# months = {
#     1: "January",
#     2:
# }

### Missing bracket

## 3.9
# points to line after error

## 3.10
# points to first bracket, never closed

# months = {
#     1: "January",
#     2: "Febuary",
#     3: "March"

# print(len(months))

### Missing bracket in try/except block

## 3.9
# raised except errors

## 3.10
# SyntaxError, multiple exception types must be parenthesised

# try:
#     print()
# except ValueError, AttributeError:
#     print("Error Occured")

### Missing Except block

## 3.9
# highlights error as SyntaxError

## 3.10
# highlights error, suggests fix with except or finally block

# try:
#     print()
# print("Got here")

### Missing Colons

## 3.9
# SyntaxError

## 3.10
# SyntaxError, expected ':'

# if x > 0

### Assignments instead of Comparisons

## 3.9
# SyntaxError

## 3.10
# SyntaxError, suggests use of '==' or ':=' instead of '='

# if x = 3:

### Using a * in f-strings

## 3.9
# SyntaxError, can't use starred expression here

## 3.10
# SyntaxError, f-string: cannot use starred expression here

# q1 = ['January', 'Febuary', 'March']
# print(f"Months of from quarter 1 are {*q1}")

### Indent Errors

## 3.9
# Expected an indented block

## 3.10
# Expected an indented block after [statement] on line [num]

# if 3 > 2:
# print('Bigger')

### AttributeErrors and NameErrors available in REPL

## 3.9
# Module has no attribute named _
# name _ not defined

## 3.10
# Module has no attribute name _ did you mean _
# name _ not defined, did you mean _

# import collections
# collections.namedtopl

# fool = 3
# print(foo)
