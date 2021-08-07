#this code is about ifelse

age = int(input("what is your age? "))
if(age <=13):
    print("you are a kid!")
elif(age <=21):
    print("you are young!")
else:
    print("you are old!")

parity = "even" if age % 2 == 0 else "odd"
print(parity)

parity = "zero" if age==0 else ("even" if age %2 == 0 else "odd")
print(parity)