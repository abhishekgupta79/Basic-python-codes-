
# Print hello world 
print("hellloo world ")
# print hello with user name
name = input("enter yuor name")
print("hello," + name + "!")

# AGE calculator
Birth_year = int(input("Enter youur birth year"))
current_year = 2025
age = current_year - Birth_year
print("you are", age, "year old.")

# finding odd and even number
num = int(input("Enter a number"))
if num % 2 == 0 :
    print("even")
else:
    print("odd")

#simple calculator
a = float(input("Enter first number :")) 
b = float(input("Enter second number :"))
print("sum:", a + b )
print("subtraction:", a - b )
print("multiplicatin:", a * b )

# print 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1 

# Password checker 
correct_password = "abhishek gupta"
entered_password = input("enter your password")
if entered_password == correct_password:
    print("access granted")  
else:
    print("access enabled") 

#celcicus to fehrenheit
celcius = float(input("enter temperature in celcius"))
fahrenheit = (celcius * 9/5) + 32
print("temprature in fahrenheit", fahrenheit)

#print fruits help of liist and loop

fruits = [" apple\n banana\n mango"]
for fruit in fruits:
    print (fruit)


