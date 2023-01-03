value = 5
print(value)

print(type(value))

listTest = {1,3,4}

print(listTest)

a,b = divmod(9,4)

print(a,b)

marxes = ['Groucho']

print(marxes.index('Groucho'))

stringy = "hello there"

listy = ['one','two']

print(listy)

del listy[0]

print(listy)

# Let's create a list of even numbers from 1-10
a_list = [number for number in range(1,10) if number % 2 == 0]

print(a_list)

years = [year for year in range(1900,1905)]

print(years)

surprise = ["Groucho", "Chico", "Harpo"]

surprise[2] = surprise[2].lower()
surprise[2] = surprise[2][::-1]
surprise[2] = surprise[2].capitalize()
print(surprise)

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope")
]

start2 = "Someone better"
output = ""

for word in start1:
    output += word+"! "

for first, second in rhymes:
        print(f"{output}{first}!")
        print(f"{start2} {second}.")


def testing_closures(start_point):

    def adder():
        print(start_point)

    return adder

a = testing_closures(5)

a()

b = testing_closures(2)
a()
b()
b()

def testing_generators(first, last):
    print("in function")
    number = first
    while number < last:
        print(f"before yield {number}")
        yield number
        print (f"after yield {number}")
        number += 1

for x in testing_generators(1,5):
    print(x)


for x in testing_generators(1,2):
    print(x)

print(type(testing_generators(1,3)))


def improve(func):
    def new_func(*args, **kwargs):
        print("new and improved!")
        func(*args, **kwargs)

    return new_func

@improve
def add_stuff(a,b):
    print(a+b)

improved_add_stuff = improve(add_stuff)

add_stuff(3,6)

print("pause for effect")

improved_add_stuff(5,4)


