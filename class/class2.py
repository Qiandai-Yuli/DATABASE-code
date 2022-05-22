import class1 as c1
from commonFunctions import commonFunction as cF


class Bag:
    """
       bag's class
       name is substance's name (self.name)
       'bag_' + self.name is class example's name
       class function needs class example's name

    """
    sum_sort = 0
    list_name = []

    def __init__(self, name, amount, quality):
        self.name = name
        self.amount = amount
        self.quality = quality
        Bag.sum_sort += 1
        Bag.list_name.append("bag_" + name)


    def bagCheck(self):
        if "bag_" + self.name in Bag.list_name:
            cF.printwithcol(f"{self.name}: {self.amount} {self.quality}", 0)



def bagAppend(name, amount, quality):
    bag_in_name = "bag_" + name
    globals()[bag_in_name] = Bag(name, amount, quality)


# noinspection PyShadowingNames
#变量隐藏检查禁止
def in_bagCheck():
    input_name = input("name:")
    try:
        eval("bag_" + input_name).bagCheck()
    except NameError:
        cF.printwithcol(f"No {input_name}", 0)


if __name__ == '__main__':
    print(Bag.__doc__)
    bag_phone = Bag("phone", 3, "perfect")
    phone_phone_x = c1.Phone("phone_x", "4500mAh", "4600RMB", "8GB", "128GB", "123456")
    bag_phone_x = Bag("phone_x", 1, "excellent")

    bagAppend(input("name:"), input("amount:"), input("quality:"))

    in_bagCheck()


    c1.in_phoneCheck()

