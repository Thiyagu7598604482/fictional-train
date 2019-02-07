yeart=int(input("Enter yeart to be checked:"))
if(yeart%4==0 and yeart%100!=0 or yeart%400==0):
    print("The yeart is a leap year!)
else:
    print("The yeart isn't a leap year!)
