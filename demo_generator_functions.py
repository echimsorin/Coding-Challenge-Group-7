"""
This programm will demo how to yield one object at a time using generator
function(lazy list).
"""


def get_numbers():
    """test"""
    numbers = []
    for x in range(0, 100):
        numbers.append(x)
    return numbers


def generate_number():
    """Yield one object at time of collection"""
    for x in range(0, 10):
        yield x


for z in generate_number():
    print(z)

gen = generate_number()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break
