print ("Hw #10 Matthew Volner") #Hw #10 Matthew Volner
import random
random.seed()
#Build a list of random names in KeyList.
KeyList = []
DataList = []
for j in range(random.randint(5,8)):
    #Create one random name.
    Name = chr(random.randint(65,90))
    for i in range(1,random.randint(2,3)):
        Name = Name + chr(random.randint(97,122))
    #print(Name)
    KeyList.append(Name+"::")
    DataList.append(chr(random.randint(97,122))+"-"+Name)
print(KeyList)
print(DataList)

#**********************************************************************
# The preceding code generates 2 parallel arrays:  KeyList and DataList.
# Your assignment is to sort them based on the values in KeyList.
#
# Below these comments write code to do the following:
#
# 1) Define a Selection sort function to sort 2 parallel arrays that will
#    be passed to them by reference. The sort routine should keep the items
#    in both arrays in sync.  Your sort function should not print out anything--
#    however, you can have it printing information while you are debugging your
#    program.
# 2) Add code to pass the arrays KeyList and DataList to your sort function.
#    After returning from your sort function, print out the KeyList and
#    DataList on 2 lines.  You can do this using the following code:
#    print(KeyList)
#    print(DataList)
#
# ** Special Instructions: You have 2 choices for doing the swaps. **
#    Method #1: 
#    Use the Data[k] = tmp type of notation that we have been using for
#    our sort operations.
#    Method #2: (Probably the harder method)
#    Use the lst.insert() and lst.pop() functions when swapping values.
#    See the online help or your Python reference sheet for help with these
#    functions.
#
# Here's some example output:
#
# HW #10: Ken Pottebaum Solution
# ['Fm::', 'Gbk::', 'Jxv::', 'Qku::', 'Viv::', 'Yi::']
# ['r-Fm', 'v-Gbk', 's-Jxv', 'n-Qku', 'w-Viv', 'b-Yi']
#
#**********************************************************************
                
            
            
    

    
