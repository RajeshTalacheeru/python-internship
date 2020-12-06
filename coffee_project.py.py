#!/usr/bin/env python
# coding: utf-8

# In[12]:


n=input("DO you want a drink:")
class coffee():
    def __init__(self,water,milk,coffeepowder):
        self.water=water
        self.milk=milk
        self.coffeepowder=coffeepowder
    def requirements(self):
        if (self.water==200):
            if (self.milk==100):
                if (self.coffeepowder==10):
                    print("requirements are present")
                else:
                    print("Sorry there is not enough coffeepowder")
            else:
                print("sorry there is not enough milk")
        else:
            print("sorry  there is not enough water")
    
    def coins(self,quarter,dimes,nickels,pennies):
        self.quarter=quarter
        self.dimes=dimes
        self.nickels=nickels
        self.pennies=pennies
        print("inserted the coins")
        if(quarter==0.25 and dimes==0.1 and nickels==0.05 and pennies==0.01):
            count=self.quarter+ self.dimes*20+self.nickels+self.pennies*200
        else:
            print("printed the other coins")
        if (count == 2.50):
            print("sufficient payment ,transaction successfull")
        elif (count > 2.50):
                print("too much money payed .take the change",count-2.5)
        else:
            print("Sorry that's not enough money. Money refunded.")
    def report(self,water,milk,coffeepowder,count):
        self.count=count
        print(self.water)
        print(self.milk)
        print(self.coffeepowder)
        print(self.count)
    def turnoff(self,turnoff):
        self.turnoff=turnoff
        print("turn off the coffee machine if no one  needs coffee")
while(n=="yes" or n=="YES"):
    drink=input("choose a drink:")
    obj=coffee(200,100,10)
    obj.requirements()
    obj.coins(0.25,0.1,0.05,0.01)
    print( "Here is your latte. Enjoy!")
    obj.report(200,100,10,2.50)
    print("action is completed")
    obj.turnoff("off")
    n=input("Do you want a drink")
    if (n=="no" or n=="NO"):
        print("exit")
        break


# In[ ]:




