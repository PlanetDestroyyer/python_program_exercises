num = int(input("Enter the number: "))
for i in range(1,num+1):
    if i%3 == 0 and i%5 ==0:
        print("Fuzz & Buzz")
    elif i%3 == 0:
        print("Fuzz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
