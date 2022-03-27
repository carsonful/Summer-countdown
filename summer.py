# gets the amount of days for until summer 
from datetime import date

currentdate = date.today()

def getsummerdays():

    summer = date(2022, 5, 26)
    delta = summer - currentdate
    return str(delta.days)



def getseniordays():

    summer = date(2022, 5, 15)
    delta = summer - currentdate
    return str(delta.days)


