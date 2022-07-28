"""
This programme will demo how to copy and optionally filter
collections  str/tuple/list/dict/sets using iterator
for loops user functions lambda functions, built-in filter function
and comprehensions
"""

students = ['bilal', 'isaac', 'ragini', 'leo', 'christian', 'harry', 'sam', 'cristian', 'sam']
wee_names = []
for name in students:
    if len(name) <= 5:
        wee_names.append(name.upper())
print(f"1.Shortnames = {wee_names}")


def filter_names(name_var):
    """Return True if String parameter is less than equal 5 Characters length"""
    if len(name_var) <= 5:
        return True
    else:
        return False


wee_names = []
for name in students:
    if filter_names(name):
        wee_names.append(name.upper())

print(f"2.Shortnames = {wee_names}")

wee_names = list(filter(filter_names, students))

print(f"3.Shortnames = {wee_names}")

wee_names = list(filter(lambda name_lambda: len(name_lambda) <= 5, students))
print(f"4.Shortnames = {wee_names}")

# list comprehension as list with duplication
wee_names = [(name.upper(), len(name)) for name in students if len(name) <= 5]
print(f"5.1 Shortnames = {wee_names}")

# list comprehension as dictionary(no elements' duplication)
wee_names = {name.upper(): len(name) for name in students if len(name) <= 5}
print(f"5.2 Shortnames = {wee_names}")

# list comprehension as dictionary(no elements' duplication and new order)
wee_names = {name.upper() for name in students if len(name) <= 5}
print(f"5.3 Shortnames = {wee_names}")
