#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
"""
import math

class Calc:
    
    principal = 0
    rate = 0
    nPeriods = 0

    def __init__(self,P=0,r=0,n=0):
        #more input parameters needed
        self.principal=P
        self.rate=r*0.01
        self.nPeriods=n

        return

    def interest(self,t):
        return round(self.amount(t)-self.principal,2)
    
    def amount(self,t):
        return round(self.principal*((1+(self.rate/self.nPeriods))**(self.nPeriods*t)),2)

    def setYearAmount(self,t):
        if t!=str(t):
            self.amount(t)
        else:
            t1 = [int(i) for i in t.split() if i.isdigit()]
            if 'days' in t:
                t2=t1[0]/365
                self.amount(t2)
            elif 'months' in t:
                t2=t1[0]/12
                self.amount(t2)
            elif 'weeks' in t:
                t2=t1[0]/52
                self.amount(t2)

    def setYearInterest(self,t):
        t1 = [int(i) for i in t.split() if i.isdigit()]
        if 'days' in t:
            t2=t1[0]/365
            self.interest(t2)
        elif 'months' in t:
            t2=t1[0]/12
            self.interest(t2)
        elif 'weeks' in t:
            t2=t1[0]/52
            self.interest(t2)
        



a = Calc(P=1000,r=4,n=2)
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62

c = Calc(P=5000,r=5.25,n=12)
assert c.setYearAmount(10) == 5007.18


"""return round(self.principal*((1+(self.rate/self.nPeriods))**(self.nPeriods*t)),2)"""

print(c.setYearInterest('10 days'))