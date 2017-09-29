
data = {}
index = 4
f = open("test.txt", "w")


while index >= 1:

    name = input("Whats your name son? ")

    surname = input("that's cool and all but what is your surname? ")

    TA = input("ok so Tits or Ass? ")

    data["name"] = name
    data["surname"] = surname
    data["TA"] =TA

    print (data)
    print(index)
    f.write(str(data))
    index = index-1

f.close()
print("EXIT TIME")
