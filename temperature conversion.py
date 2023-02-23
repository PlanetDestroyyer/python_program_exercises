def convert_to_Celsius(number):
    return number*(9/5)+32
def convert_to_fahrenheit(number):
    return (number-32)*(5/9)
while True:
 number = int(input("Enter a number : "))
 comand = int(input("Select which to convert :1)Celsuis or 2)Farenheits : \n"))

 if comand == 1:
     print(convert_to_Celsius(number))
 elif comand == 2:
     print(convert_to_fahrenheit(number))
 else:
     print("error")
