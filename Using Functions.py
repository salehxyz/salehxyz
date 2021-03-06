# This code will creat and then use some fuctions:

import math

# Function 1:
def pythagoreanTheorem (length_a, length_b):
    return math.sqrt(length_a**2 + length_b ** 2)


# Function 2:
def listmagler(list_in):
    if len(list_in)%2==0:
        for i in range(len(list_in)):
            list_in[i]=list_in[i]*2
    else:
        for i in range(len(list_in)):
            list_in[i]=list_in[i]*3

    return list_in




# Function 3:
def grad_calc(grads_in,to_drop):
    grads_in.sort()
    revised_grades = grads_in[to_drop:len(grads_in)+1]
    average = sum(revised_grades)/len(revised_grades)
    Grade_List = {
        0:"F",
        60:"D",
        70:"C",
        80:"B",
        90:"A",
        100:"A"
    }
    grade = math.floor(average/10)*10
    if grade <60: grade = 0
    print(average)
    return Grade_List.get(grade)



# ---------------------------------------------------- #
#Testing Function 1:
print("Test part 1:")
print(pythagoreanTheorem(2,2))

# Testing Function 2:
print("\n Test part 2:")
a = [2,5,6,9]
print(a)
print(listmagler(a))

# Testing Function 3:
print("\n test part 3:")
aa = [55,68,75,85,94,100,87]
print("the intial grades are: " + str(aa))

print(grad_calc(aa,0))

