def suffix(num):
    num = str(num)
    if num[-2:] in ["11","12","13"]:
        print(num+"th")
    elif num[-1] == "1":
        print(num+"st")
    elif num[-1] == "2":
        print(num+"nd")
    elif num[-1] == "3":
        print(num+"rd")
    else:
        print(num+"th")
while True:
    num = int(input("Enter the number : "))
    suffix(num)