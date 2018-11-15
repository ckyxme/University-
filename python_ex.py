def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(str(item))
    print()


fruits = ["Banana","Orange","Apple","Mango"]

print_list(fruits, "FRUITS")

fruits.append("Banana") # again!

print_list(fruits, "FRUITS with an extra Banana")

favourite = input("What is your favourite fruit? ")
fruits.insert(0, favourite)

print_list(fruits, "FRUITS, favourite first")

favourite = input("What is your least favourite fruit? ")
fruits.insert(6, favourite)

print_list(fruits, "FRUITS, least favourite last")

print("The list contains " + str(fruits.count("Banana")) + " Bananas")
print()

while "Banana" in fruits:
    fruits.remove("Banana")
print_list(fruits, "FRUITS with no Bananas")

print("The list contains " + str(fruits.count("Banana")) + " Bananas")

print()
input("Press return to continue ...")