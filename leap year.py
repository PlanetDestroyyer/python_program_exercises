def check(year):
    if year % 400 == 0 and year%100 ==0:
        print(f"{year} is a leap year")
    elif year%4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year")
    else:
        print(F"{year} is not a leap year")

while True:
    year = int(input("Enter the Year : "))
    check(year)