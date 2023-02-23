def check(num):
    if (num % 2) == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd ")
while True:      
    num = int(input("Enter the number: \n"))
    check(num)