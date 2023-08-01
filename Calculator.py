import math
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def convert_num(num):
    help_dict= {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
    res1=''.join(help_dict[ele1] for ele1 in num.split())
    return res1
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n " \
        "5. Sine\n" \
        "6. Cosine\n" \
        "7. Tangent\n"\
        "8. Exponent\n" \
        "9. Logarithm\n" \
        "10. Modular\n" \
        "11. factorial\n")

select = int(input("Enter your choice: "))

if select < 5 or select==10:
   number_1 = input("Enter first number: ")
   number_2 = input("Enter second number: ")
else:
    number_1 = input("Enter the number: ")

print('Please select type: \n' \
      "1. String\n" \
      "2. Float\n")
t = int(input('Enter your choice: '))
if t == 1:
    number_1=float(convert_num(number_1))
    number_2=float(convert_num(number_2))
else:
    number_1=float(number_1)
    number_2=float(number_2)

if select == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))
elif select==5:
    print("sin(",number_1,") = ",math.sin(number_1))
elif select==6:
    print("Cosine(",number_1,") = ",math.cos(number_1))
elif select==7:
    print("Tangent(",number_1,") = ",math.tan(number_1))
elif select==8:
    print("Exponent(",number_1,") = ",math.exp(number_1))
elif select==9:
    print("Logarithm of",number_1,"=",math.log(number_1))
elif select==10:
    print("Modular of",number_1,"=",math.fmod(number_1,number_2))
elif select==11:
    print("Factorial of",number_1,"=",math.factorial(number_1))
else:
    print("Invalid input")
