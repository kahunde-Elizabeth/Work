#pwd = 500
#user_pwd = int(input("enter password:"))
#if (user_pwd == 500):
   # secret = "today is payday"
  #  print(f"{secret}")
#else:
    #print(f"you entered a wrong password")
    ## we use two equal signs when we are comparing
voting_age = 18
age = int(input("How old are you:"))
if(age>=voting_age):
   print("You are eligible to vote")
else:
   print("You are too young")

#number=int(input('Enter the number:'))
#if number >=10:
 #   print('number is greater than 10')
#else:
 #   print('Number is less than 10') 
#is_logged_in= False
#if is_logged_in:
 #  print("Welcome")
#else:
 #  print('You are logged out')    
#Day=input("What is the day of the week?")
#if Day in['Monday','Tuesday','Wednesday','Thursday','Friday']:
 #  print("This is the day of the week")
#else:
 #  print('Not a day of the week')
#Correct_Password='Cookie'
#user_password=(input("Enter Pasword"))
#if user_password==Correct_Password:
 #  print("Access Granted")
#else:
 #  print("Access Denied")
#number= int(input("Enter even number"))
#if number%2==0:
 #  print("The number is an even number:")
#else:
 #  print("The number is not even")
  
#year_of_birth = int(input("when were you born"))
#current_year = int(input("what is the year now"))
#age = current_year-year_of_birth
#print(f"I am {age} years old")

#num_1=float(input("What is the first number A:"))
#num_2=float(input("what is the second number B:"))
#sum= num_1+num_2
#product= num_1*num_2
#print(f"the sum is {sum} and the product is {product}")

#N= float(input("what is the square of the value"))
#square= N**2
#print(f"the square of the number {N} is {square}")

#l=float(input("what is the number L:"))
#B=float(input("what is the number is B:"))
#area= B*l
#perimeter_of_the_rectangle=B+l
#print(f"the perimeter is {perimeter_of_the_rectangle} and the area of the rectangle is {area}")

#C=float(input("what is the temperature in Celcius"))
#fahrenheit=1.8*C+32
#print(f"The temperature {C} is {fahrenheit}")

#R=float(input("what is the radius of the circle"))
#diameter= R*2
#area= 3.144*R
#circumference=2*3.144*R
#print(f"the diameter of the circle is{diameter} and the circumference of the circle is {area} and the circumference of the circle is {circumference}")

#intial=float(input("what is the intial of the water"))
#final=float(input("what is the final value of the water"))
#consumption=final-intial
#cost=consumption*1500
#print(f"the cost of the litres is {cost}")
'''
popn=43000000
growth=0.123
for year in range(1,4):
    popn*=(1+growth)
    print(f"Year{year}:{popn:2f}million")'''
'''
for i in range(5):
  print("Hello world")'''

#loops
'''fruits=["apple","banana","grapes"]
for i in fruits:
    print(i)'''''
#i represents printing the letter individually
'''for char in 'Kahunde':
    print(char)'''''
'''num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)'''''
#instead of saying 1to 10 you can use range but doesnt print the last element
'''for i in range(1,11):
    print(i)'''''
# put in number but not 0
'''number= None
while number!=0:
    number=int(input("Please enter a number"))

print("loop ended")'''''

'''sum=0
number=1
while number<=100:
    sum+=number
    number+=1
print("the sum is",sum)'''
## IF PRACTICE
'''num=int(input("What is the number"))
if (num>=10):
  print("the number is greater than 10")
else:
  print (' the number is less than 10')'''

'''age=int(input("What is your age."))
if(age>=18):
    print("You are eligible to vote.")'''

'''is_logged_in=True
if is_logged_in:
    print("Welcome")'''

'''num=int(input('What is your number?'))
if (num%2==0):
    print("Even")
else:
    print("Odd")'''

'''correct_password=20456
pwd=int(input('Enter your password.'))
if (pwd==correct_password):
    print('Access Granted')
else:
    print('Access Denied')'''

'''num=int(input('Enter the number'))
if (num%5==0):
    print("Divisible by 5")
else:
    print('Not divisible by 5')'''

'''Name=input("State Your name")
age=int(input("Please enter your age"))
if (age>=18 and Name.upper().startswith('A')):
    print('Welcome, VIP!')
else:
    print('Welcome')'''

'''num=int(input('What is your number?'))
if(1<=num <=100 and num%2==0):
    print('Valid number')
else:
    print('invalid number')'''

'''year=int(input("Please enter the Year"))
if(year%4==0 and year%100!=0)or (year%400==0):
    print(f'{year}is a leap year.')
else:
    print(f'{year}is not a leap year.')'''

###FUNCTIONS
'''def calc_area(l,w):
    area_rec=l*w
    return area_rec
length=float(input("Enter the length:"))
width=float(input("Enter the width:"))
the_area=calc_area(length,width)
print(f"the area of the rectangle is {the_area}")'''
'''num=6
if(num%2==0):
    print('even')'''
  

'''def process_text(text):
    #convert to lower case
    text=text.lower()
    print("text after converting to lower case:",text)
    # Removing the trailing and leading whitespace
    text=text.strip()
    print(f"text after removing leading and trailing whitespace:", text)
    #replace space with hyphens
    text=text.replace(" ","-")
    print(f"text after replacing spaces with hyphens:{text}")
    #replace python with PYTHON
    text=text.replace("python","PYTHON")
    print(f"text after replacing python with PYTHON:{text}")
    #reverse the entire string
    text=text[::-1]
    print(f"text after reversing it:{text}")
    return text

process_text('  Welcome to the Python Progamming Language')'''


'''def modify_list(numbers):
    numbers=list(set(numbers))
    print ("after removing duplicates", numbers)
   
#sort list in ascending order
    numbers=sorted(numbers)
    print("after sorting numbers",numbers)
#replace each even number with its square
    numbers =[x**2 if x%2==0 else x for x in numbers] 
    print(" after squaring numbers", numbers)

    return numbers
modify_list([5,3,2,8,3,5,7,2])'''

'''list= [2,4,5,6,7]
number_of_values= len (list)
print(number_of_values)'''

'''greeting='Hello'
name='Micheal'
print(dir(name))
print(help(str))'''
#name='Hello, world'
#print (name[::-1])

# practice in functions
'''def maximum_number(a,b,c,d):
    return max(a,b,c,d)
print(maximum_number(1,2,3,4))'''

'''def sum_num(numbers):
    return sum(numbers)
sample_list=[8,9,7,2,3]
print(sum_num(sample_list))'''

'''def multiply_no(numbers):
    result=1
    for num in numbers:
        result*=num
    return result
sample_list=(1,3,4,5)
print(multiply_no(sample_list)) '''


'''def reverse_string(s):
    return s[::-1]
sample_string='1234rdf566'
print(reverse_string(sample_string))'''

'''def factorial(n):
    if n<0:
        raise ValueError('factorial is not defined for negative')
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
num=5
print(f'Factorial is {num}')'''

'''def check_range(num,lower,upper):
    return lower<=num<= upper
num=7
lower=90
upper=10
print(check_range(num, lower, upper))'''

'''def count_case(s):
    upper= sum(1 for c in s if c.isupper())
    lower= sum(1 for c in s if c.islower())
    return upper,lower

sample_string="The quick Brow Fox"
upper, lower= count_case(sample_string)
print (f'No. of Uppercase Characters: {upper}')
print(f' No. of lower case characters: {lower}')'''

'''def unique_elements(lst):
    return list(set(lst))
sample_list=[1,2,3,4,5,3,3,6]

unique_list=unique_elements(sample_list)
print(unique_list)'''

'''def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=11
print(is_prime(num))'''

'''def check_even(lst):
    if even_number%2==0
    return even_number
sample_list=[1,2,3,4,5,6]
print(check_even(sample_list))'''

'''def is_palindrome(s):
    s=''.join(c for c in s if c.isalnum()).lower()
    return s== s[::-1]

word=input("enter the word")
if is_palindrome(word):
    print("it is a palindrome")
else:
    print("it is a palindrome")'''

'''def sort_words(s):
    words=s.split('-')
    words.sort()
    return'-'.join(words)

sample='green-red-yellow-black-white'
print(sort_words(sample))'''

'''def squares_list():
    return[i**2 for i in range(1,31)]
print(squares_list())'''

'''def outer():
    def inner():
      return "Hello from inner!"
    return inner()
print(outer())'''

##lists
'''def sum_list(smple):
    return sum(smple)

sample=[1,2,3,4]

print(sum_list(sample))'''

'''def prodct_lst(lst):
    product=1
    for num in lst:
        product*=num
    return product
number=[3,4,6,7,8,9,1]
print(prodct_lst(number))'''

'''def largest_num(lst):
    return max(lst)
lt=(1,2,3,4,5,10)
print(largest_num(lt))'''

'''def smallest_num(lst):
    return min(lst)
lt=(1,2,3,4,5,6,8)
print(smallest_num(lt))'''

'''sample_list=['abc','xyz','aba', '1221']
count=0
for s in sample_list:
    if len(s) >=2 and s[0] == s[-1]:
        count+=1
        print(count)'''

'''sample_list= [(2,5),(1,2),(4,4,),(2,3),(2,1)]
sorted_list= sorted(sample_list, key=lambda x: x[-1])
print(sorted_list)'''

'''sample_list=[1,3,4,5,6,6,1,3,9,9]
unique_list=list(set(sample_list))
print(unique_list)'''

'''sample=[]
if len(sample)==0:
    print("Empty set")
else:
    print("Not empty")'''

'''sample=[1,2,3,4,5]
cloned=sample.copy()
print(cloned)'''

'''list=['apple', 'banana', 'cherry', 'date', 'elderberry']
n=5
longer_word=[word for word in list if len(word)> n]
print(longer_word)'''

'''lt1=[1,2,3,4,5]
lt2=[24,15,7,8,9]
if len (set(lt1)& set(lt2)) >0:
    print('The lists have common memebers')
else:
    print("The lists donot have common members")'''

'''sample=[1,2,3,4,5,6,7,8]
indices=[0, 4, 5]
for i in sorted(indices, reverse=True):
    del sample[i]
print(sample)'''
'''import numpy as np
array=np.full((3,4,6), '*')
print(array)'''

'''def remove_even(lst):
    return [num for num in lst if num%2==0]
number=[1,2,3,4,5,6,7,8]
print(remove_even(number))'''

'''import random
def shuffle_lst(lt):
    random.shuffle(lt)
    return lt
numbers= [1,2,3,4,5]
print(shuffle_lst(numbers))'''

'''def generate_square(n):
    return [i**2 for i in range (1, n+1)]
numbers=generate_square(30)
print(numbers[::-5])'''

'''def is_prime(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def all_prime(lst):
    return all(is_prime(num)for num in lst)
numbers1=[0,3,4,7,9]
numbers2=[3,5,7,13]
numbers3=[1,5,3]
print(all_prime(numbers3))'''

'''for i in range(1,4,2): # same as the square brackets
      print(i)'''


''''ourses=["compsci", "art", "commerce"]
new_courses=courses.pop()
print(new_courses)'''
'''from functools import reduce
from operator import mul
num=[1,3,6,9,8,7]
product=reduce(mul,num)
print(f"the product of all numbers in the list {product}")'''

'''def even_numbers(lst):
      return[num for num in lst if num%2==0]
gnlist=[1,2,3,4,5,6,7,8,9]
print(even_numbers(gnlist))'''

'''smple="1234abcd"'''
'''sample=smple[::-1]
print(sample)'''

'''print(len(smple))'''

'''mylist=[1,2,"carry"]
print(mylist)'''

'''num=input("Enter a number")
if num.isdigit(): # this is for the fools that put in silly responses
    num=int(num)
    if num%2==0:
     print('even')
else:
    print('odd')'''

'''def sum(name):
    print(f"Hello ,{name}")
sum(1)'''

'''def greet(name: str)->str:
    return f'Hello, {name}'''