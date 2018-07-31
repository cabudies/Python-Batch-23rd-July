class SampleData:
    name = ""
    age = 0
    phone = 0

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def displayData(self):
        print("Name is: ", self.name)
        print("Age is: ", self.age)
        print("Phone is: ", self.phone)

objList = []

obj = SampleData("Ankit", 21, 123)
obj1 = SampleData("Ranu", 21, 123)
obj2 = SampleData("Vijay", 21, 123)

objList.append(obj)
objList.append(obj1)
objList.append(obj2)

# obj.displayData()
# print("Name is: ", obj.name)
# print("Age is: ", obj.age)
# print("Phone is: ", obj.phone)

for item in objList:
    print("Name is: ", item.name)
    print("Age is: ", item.age)
    print("Phone is: ", item.phone)














