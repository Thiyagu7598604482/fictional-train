a = int(input("num 1 : "))
b = int(input("num 2 : "))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.divide")
choice = input("choice : ")
if choice == '1':
     c = a + b
     print (c)
elif choice == '2':
     c = a - b
     print (c)
elif choice == '3':
     c = a * b
     print (c)
elif choice == '4':
    if b == 0:
        print ("infinty")
    else:
     c = a / b
     print (c)
else:
    print("Invalid input")
print("round value")
print(round(c))
