from commonFunctions import commonFunction as cF

class Phone:
    """
    phone's class
    """
    amount = 0
    list_name = []

    def __init__(self, name, battery, price, ram, rom, password):
        self.name = name
        self.battery = battery
        self.price = price
        self.ram = ram
        self.rom = rom
        self.password = password
        Phone.amount += 1
        Phone.list_name.append("phone_" + name)

    def phoneCheck(self):
        input_password = input("password:")
        percent = 0
        t = 0
        cF.fake_process(percent,t)
        if input_password == self.password:
            cF.printwithcol("\nAllowed to check", 1)
            print(self.battery, self.price, self.ram, self.rom)
        else:
            cF.printwithcol("Wrong password", 1)


# noinspection PyShadowingNames
#变量隐藏检查禁止
def in_phoneCheck():
    input_name = input("name:")
    try:
        eval("phone_" + input_name).phoneCheck()
    except NameError:
        cF.printwithcol(f"No {input_name}", 0)


def phoneAppend(name, battery, price, ram, rom, password):

    phone_in_name = "phone_" + name
    globals()[phone_in_name] = Phone(name, battery, price, ram, rom, password)




if __name__ == '__main__':
    phone_phone1 = Phone("phone1", "4800mAh", "6999RMB", "10GB", "128GB", "216108")
    print(Phone.__doc__)




    in_phoneCheck()
