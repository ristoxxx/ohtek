import datetime
from datetime import date
import
date1 = "2020-11-19"
date2 = "2020-11-18"
    
def compare_date(a,b):
    date1 = date.fromisoformat(a)
    date2 = date.fromisoformat(b)
    return date1 < date2
print (compare_date(date1,date2))
    
    

"""date1 = datetime.date(2014, 3, 2)
date2 = datetime.date(2013, 8, 1)
date3 = date.fromisoformat("2020-11-19")

print(was_date1_before)"""

def guru(a,b):
    return (a+b)
print(guru(1,2))
date1 = datetime.date(2014, 3, 2)
date2 = datetime.date(2013, 8, 1)
date3 = date.fromisoformat("2020-11-19")