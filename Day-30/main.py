fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
try:
    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")
except IndexError:
    fruits.append("a")
    fruits.append("Fruit")
else:
    print(None)


make_pie(4)
