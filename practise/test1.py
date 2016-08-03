# print((5>=10) or(1<2))



"""
2.
my_list=[0]*6                                          [0, 0, 0, 0, 0, 0]
print(my_list)
"""

"""
my_list=[1,2,3,4,5,6]
A=[my_list]*3               [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
print A


my_list[2]=45              [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
                        [[1, 2, 45, 4, 5, 6], [1, 2, 45, 4, 5, 6], [1, 2, 45, 4, 5, 6]]
print A
"""

"""
#!usr/bin/python
import time
ticks = time.time()          1470205101.91
print ticks
"""

"""
my_list=[2,6,7.89,True,5]
my_list.append(False)
print my_list
my_list.insert(58,56.78)
print my_list
"""
"""
def Hello(name,x):
    if x <= 0:
        print "Exiting..."
    else:
        print "hello"+name
        Hello(name,x-1)

Hello("Jeff",2)
        """
