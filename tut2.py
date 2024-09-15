# -*- coding: utf-8 -*-
"""tut2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NtbAMhrNM-I3gySXlupm8MZZtdg3vriy
"""

L=[11,12,13,14]
print(f"Original list is as follows :{L}")
L.append(50)
L.append(60)
print(f"1(i) list is as follows :{L}")
print("\n")

L=[11,12,13,14]
print(f"Original list is as follows :{L}")
L.remove(11)
L.remove(13)
print(f"1(ii) list is as follows :{L}")
print("\n")

L=[12,11,14,13]
print(f"Original list is as follows :{L}")
L.sort()
print(f"1(iii) list is as follows :{L}")
print("\n")

print(f"Original list is as follows :{L}")
L.reverse()
print(f"1(iv) list is as follows :{L}")
print("\n")

L=[11,12,13,14]
print(f"Original list is as follows :{L}")
i=12
if i in L:
    print(f"{i} is present in 1(v) list")
else:
    print(f"{i} is not present in 1(v) list")
print("\n")

L=[11,12,13,14]
print(f"Original list is as follows :{L}")
print(f"length of 1(vi) list is {len(L)}")
print("\n")

L=[11,12,13,14]
print(f"Original list is as follows :{L}")
total=0
for num in L:
    total+=num
print("The sum of numbers in L list is :",total)
print("\n")

L=[11,12,13,14]
print(f"Original list is as follows :{L}")
total=0
for num in L:
    if num%2!=0:
        total+=num
print("Sum of odd number :",total)
print("\n")

L=[11,12,13,14]
print(L)
print("Orginal sum of the list is 50")
total=0
for num in L:
    if num%2!=0:
        total+=num
print(f"The sum of even numbers in list in 1(ix) is {total}")
print("\n")

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(lst):
    """Sum all prime numbers in the list."""
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    return prime_sum

L=[11,12,13,14]
print(f"Orginal list is as follows : {L}")
L.clear()
print(f"1(xi) list is as follows :{L}")
print("\n")

L=[11,12,13,14]
print(f"Orginal list is as follows : {L}")
del L
print("No L list exists after deletion of that list")

l=[11,12,13,14]
total=0
for num in l:
    total+=num
print(f"The sum of numbers in L list is: {total}")

l=[13,15,14,16]
total=1
for num in l:
    total*=num
print(f"The multiplication of all the elements in the list is :{total}")

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
#Q5(i)
D[8]=8.8
print(f"Updated dictionary for 5(i) is as follows :{D}")
print("\n")

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D.pop(2)
print(f"Updated dictionaryv for 5(ii) is as follows :{D}")
print('\n')

print("Previous disctionary is : ",D)
key=6
if key in D:
    print(f"6{key} is present in the dictionary")
else:
    print("6 key is not present in the dictionary")
print("\n")

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
len(D)
print("Length of the dictionary is :",len(D))
print("\n")

#Q5(vi)
D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[3]=7.1
print("Updated value of key 3 is : ",D)
print("\n")

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print("Original dictionary is :",D)
D.clear()
print("After clearing the dictionary :",D)

S1= [10, 20, 30, 40, 50, 60]
S2= [40, 50, 60, 70, 80,90]

S1.append(55)
S1.append(66)
print("(i) Updated S1 list in 6(i) is :0",S1)
print("\n")

S1= [10, 20, 30, 40, 50, 60]
S2= [40, 50, 60, 70, 80,90]
S1.remove(10)
S1.remove(30)
print("(ii) Updated S1 list in 6(ii) is :",S1)
print("\n")

S1= [10, 20, 30, 40, 50, 60]
S2= [40, 50, 60, 70, 80,90]
NUM=40
if NUM in S1:
    print(f"(iii) {NUM} is present in List S1 of Q6(iii)")
else:
    print(f"(iii) {NUM} is not present in List S1 Of Q6(iii)")
print("\n")

union_list=list(set(S1)|set(S2))
print("(iv) Union of S1 and S2 :",union_list)
print("\n")

intersection_list=list(set(S1)&set(S2))
print("(v) Intersection of S1 and S2 :",intersection_list)
print("\n")

difference_list=list(set(S1)-set(S2))
print("(vi) Difference of S1 and S2 :",difference_list)
print("\n")

for num in range(600,801):
    if num>1:
        for i in range(2,int(num**0.5)+1):
          if num%i==0:
              break
        else:
            print(num,end=",")
print("\n")

for num in range(100,1001):
    if num%7==0 and num%9==0:

        print(num,end=" ")

exam_date = (23, 9, 2024)

print(f"The examination will start from: {exam_date[0]}/{exam_date[1]}/{exam_date[2]}")

numbers = [6, 10, 45, 60, 75, 3, 55, 715, 10090]
for number in numbers:
    if number % 5 == 0:
        print(number,end=" ")

a=int(input("Enter a number : "))
even=a%2==0
if (even==True):
    print("{a} is even")
else:
    print("{a} is odd")

string = "Thapar is one of the worst university.Thapar has a bad infrastructure"
count = string.count("Thapar")

print("The substring 'Thapar' appears {count} times in t")