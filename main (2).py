def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mult(a,b):
  return a*b

def div(a,b):
  if b == 0 :
    return "cannot divide by zero"
  else:
    return a/b

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice 1/2/3/4 : ")

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

if choice == "1":
  print(num1,"+",num2,"=",add(num1,num2))

elif choice == "2":
  print(num1,"-",num2,"=",sub(num1,num2))

elif choice == "3":
  print(num1,"*",num2,"=",mult(num1,num2))

elif choice == "4":
  print(num1,"/",num2,"=",div(num1,num2))

else:
  print("invalid syntax")


  











  
  


  
  


