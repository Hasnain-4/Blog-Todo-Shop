# x= int(input('enter number : '))

# if x>1:

#     for i in range(2, x):

#         if x%i == 0:
#             print('Not Prime')
#             break
#     else:
#         print('Prime')

# else:
#     print('not prime')

# ...........Leap yr.........................

# year = int(input('Enter Year to check whether it is Leap or not : '))

# if year % 4 == 0:
    
#     if year % 100 == 0:
        
#         if year % 400 == 0:
#             print('Leap year')
#         else:
#             print('Not Leap')
    
#     else:
#         print('Leap year')

# else:
#     print('Not Leap year')

# min Max ++++++++++++++++++

# li = [1,3,4,7,2,5,8,3,5,9]

# # print(max(li))
# print(min(li))


# Fibonacci ............

# n = int(input('enter length'))
# x,y=0,1
# i=0

# while(i<n):
#     if n<=1:
#         print(x,y)
#     else:

#         next = x+y
#         x=y
#         y=next
#         print(next, end=' ')
#         i+=1


#list to str.........

# list1 = ['1', '2', '3']
# str1 = ''.join(list1)

# print(str1)

#............string to list........

# str = "hi there"

# st = str.split()
# print(st)

#........... factorial ............

# def fact(num):

#     if num == 1:
#         return num
#     else:
#         return num * fact(num-1)

# x= int(input('enter number : '))
# print(fact(x))
# # fact(5)

# def factorial(num):
#     """This is a recursive function that calls
#    itself to find the factorial of given number"""
#     if num == 1:
#         return num
#     else:
#         return num * factorial(num - 1)


# # We will find the factorial of this number
# num = int(input("Enter a Number: "))

# # if input number is negative then return an error message
# # elif the input number is 0 then display 1 as output
# # else calculate the factorial by calling the user defined function
# if num < 0:
#     print("Factorial cannot be found for negative numbers")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     print("Factorial of", num, "is: ", factorial(num))

# concatinate 2 string...............

# a="hi there"
# b = "kaise ho"

# print(a+ ", " +b)

# Armstrong Number ........

# num = int(input("Enter a number: "))  
# sum = 0  
# temp = num  
  
# while temp > 0:  
#    digit = temp % 10  
#    sum += digit ** 3  
#    temp //= 10  
  
# if num == sum:  
#    print(num,"is an Armstrong number")  
# else:  
#    print(num,"is not an Armstrong number")  

#.............Swap two numbers ..........

# a=10
# b=20
# print(a,b)

# b,a=10,20

# print(a,b)

#average

# a=int(input("Enter first no.:: "))
# a3=int(input("Enter first no.:: "))
# a2=int(input("Enter first no.:: "))
# a1=int(input("Enter first no.:: "))

# av = sum(a+a1+a2+a3)/2

# print('Average is :', av)

# lst = [] 
# a = int (input("enter numbers : "))

# for i in range(a):
#     ele = int(input()) 
#     lst.append(ele)
# print(lst)
#     av = sum(lst)/len(lst)

# print(av)

#sum of numbers......

# lst =[]

# num = int(input('enter range : '))

# for i in range(num):
#     ele = int(input())
#     lst.append(ele)
#     s = sum(lst)
# print(s)
