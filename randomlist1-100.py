#This generates a list of numbers from 1 to 100 without using a loop, and then it shuffles up the list. 
import random
l = list(range(1,101))
random.shuffle(l,random.random)
print(l)

