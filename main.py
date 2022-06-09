import os
from time import process_time_ns
#String in Python
greetings = "Assalam o Alaikum from  "
name = "Muhammad Shariq Shafiq"
c = greetings + name
print(c)

story = '''the dog lost the bone because of his greediness and had to go back home hungry The greedy dog had learned a lesson! You may also like to read, The Dog Who Went Abroad. MORAL: WE SHOULD NOT BE GREEDY.'''

print("The Story is :")


print(story)

print("The no. of characters of the story are : ")

print(len(story))

print(story.endswith("."))
print(story.count("Abroad"))
print(story.capitalize())
print(story.find("MORAL"))
print(story.replace("dog" , "Cat"))
print(name[-6:-1])#this works same as name[0:6]

print(name[4:6])

#Creating a tuple using ()
t = (1 , 2 , 34 ,43 , 1 , 1,  1)
print(t[1])
#We cannot update the value of tuple just like we did in lists

#t[0] = 44

#print(t) #Show Error that it can't be updated

#Empty tuple
t1 = ()
print(t1)

#Tuple with one value
t2 = (1,)
print(t2)

#Methods of tuple

print(t.index(43))


'''
Important Points about Lists:
List are used to display the values in ordered paired
like in same sequence the are written in [ ].
'''
a = [1 , 2 , 3, 4, 5]
print(a)
'''If you want to display some unique value of the list
put the index number same as we did in c++ . ":" in python is iused to show the 
range till the lists, strings etc has to display the message or value.
'''
print(a[0:5])

'''If you want to replace the value of list with your desire value you have to just
take the index of that value and replace it by putting the value in that place'''

a[1] = 6
a[4] = "Shariq's List"
print(a)

'''
We can create list of different items as we said in starting'''
b = [546 , "M. Shariq"  , True, 4.0]
print(b)

'''We can sort the list by using .sort() function'''
'''
In  python we have to just declare the function to be performed on the list , tuple , dictionaroes 
sets etc and call the function by original varoable name'''
c = [1 , 8, 2 , 4, 7, 11]
c.sort()
print(c)
c.reverse()
print(c)
c.append(2) #append means to add value at the end of updated list or document
print(c)
c.insert(1 , 546)
print(c)
c.pop(2)
print(c)

#Dictionary In Python
mydict = {
    "Shariq" :  "Nice",
    "Moeez" : "parhna wala" ,
    "Shariq" : "Bright",
    "Mujtaba" : "Gussa Wala Larka"
}
mydict1 = {"Shariq" : "Good Boy"}
print(mydict1["Shariq"])

print(mydict["Mujtaba"])

#for more methods of dictionaries 
#Please visit 
#https://docs.python.org/3/tutorial/datastructures.html

mydict.clear = ["Shariq" , "Bright"]

print(mydict)

#Sets in Python
a = ( 1, 2 , 3 , 4 , 2 , 3)
b = { 1, 2 , 3 , 4 , 2 , 3}

print(set(a))
print(type(b))
print(type(a))

#for more methods of Lists 
#Please visit 
#https://docs.python.org/3/tutorial/datastructures.html