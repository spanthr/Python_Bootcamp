from Chef import Chef
myChef=Chef()
myChef.make_kabab()


print("now chinese chef")

class ChineseChef(Chef):                        # inherit all functions


    def make_noodles(self):
        print("Chef makes noodles")
    def make_kabab(self):
        print("Chef makes kabab But they are chinese type")

myChineseChef=ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_noodles()
myChineseChef.make_kabab()