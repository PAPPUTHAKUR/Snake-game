"""def abc(x,n):
    if x == 0 and n == 0:
        print("Ans :1")
    elif n == 0:
        print("Ans:1")
    else:
        print("Ans :", x**n)





x = int(input())
n = int(input())
abc(x,n)

def abc(n):
    for i in range(65 , 65 + n):
        for j in range(65, i + 1):
            print(chr(i),end="")
        print()



N = int(input())
abc(N)


def abc(n):
    num = 1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num = num +1
        print()

N = int(input())
abc(N)
#Amul is the student of the class 12 .today his result is out.
marks_math = int(input())
marks_english = int(input())
marks_science = int(input())
avg = (marks_science + marks_math + marks_english) / 3
print(avg)
n = int(input("ENTER THE CHOICE FOR THE CALCULATION:--"))
if n == 1:
    a = int(input("value1:"))
    b = int(input("value2:"))
    print(f"the sum is :{a + b}")
elif n == 2:
    a = int(input("value1:"))
    b = int(input("value2:"))
    print(f"the difference is :{a - b}")
elif n == 3:
    a = int(input("value1:"))
    b = int(input("value2:"))
    print(f"the multipication is :{a * b}")
elif n == 4:
    a = int(input("value1:"))
    b = int(input("value2:"))
    print(f"the quoitent is :{a / b}")
elif n == 5:
    a = int(input("value1:"))
    b = int(input("value2:"))
    print(f"the  remainder is :{a % b}")
elif n == 6:
    print("exits")
else:
    print("Invalid Operation")
N = input()
a = len(N)
while a > 0:
    b = int(N) % 10
    print(b,end="")
    N = int(N) /10
    a = a-1
N = int(input())
sum_even = 0
sum_odd = 0
while N >0:
    last = N % 10
    if last %2 == 0:
        sum_even += last
    else:
        sum_odd += last

    N = N // 10
print(sum_even,sum_odd)
def abc(n):
    if n == 0 or n == 1:
        return n
    else:
        return abc(n-1) + abc(n-2)
N =int(input())
x = abc(N)
print(x)
****
****
****
****

n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
1111
2222
3333
4444
n = int(input())
for i in range(1,n+1):
    for j in  range(1,n+1):
        print(i, end="")
    print()
1234
1234
1234
1234

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
4321
4321
4321
4321

n= int(input())
for i in range(1,n+1):
    for j in  range(n):
        print(n - j, end="")
    print()
1
12
123
1234
n= int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
1
23
345
4567
n = int(input())
for i in range(1 ,n+1):
    p = i
    for j in range(1,i+1):
        print(p,end="")
        p = p + 1
    print()
1
21
321
4321

n = int(input())
p = 1
while p <= n:
    q = p
    while q >=1:
        print(q,end="")
        q -= 1
    print()
    p = p + 1

1
11
111
1111

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("1",end="")
    print()
1234
123
12
1
n = int(input())
for i in range(n+1):
    for j in range(1,(n+1)-i):
        print(j,end="")
    print()
****
***
**
*
n = int(input())
for i in range(1,n+1 ):
    for j in range(i,n+1):
        print("*",end="")
    print()
n = int(input())
for i in range(1,n+1):
    space = 1
    for j in range(space,n-i):
        print(" ",end="")
        space = space + 1
    star = 1
    for k in range(star,i):
        print(k,end="")
        star = star + 1
    print()

n = int(input())
i = 1
while i <= n:
    space = 1
    while space <= n-i:
        print(" ",end="")
        space = space + 1
    p = 1
    j = 1
    while j <= i:
        print(p,end="")
        j = j + 1
        p = p + 1
    print()
    i = i + 1
#take item in list and search in the kist
n = int(input("ENTER NO OF ELEMENT IN THE LIST"))

list_1 = []
for i in  range(n):
    x = int(input("eNTER ITEM IN LIST"))
    list_1.append(x)
print(f"The list is {list_1}.")
a = int(input("ENTER ITEM TO BE SEARCH"))
for y in list_1:
    if y == a:
        print(f"Yes,{a} is in the list at {y} position.")
        break
else:
    print(f"No,{a} is not in the list .")
list_1 = [2,6,8,5,4,3]
list_2 = [2,3,4,7]
list_3 = []
for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)
        else:
            pass
print(list_1)
print(list_2)
print(list_3)
list_1 = [2,8,10,5,-2,5]
len_1 = int(len(list_1))
n = int(input())
sum = 0
for i in list_1:
    for j in list_1:
        add = i + j
        if add == n:
            sum = sum + 1
        else:
            pass

print(sum)
list_1 = [1,2,3,4,5,6,7]
len_1 = int(len(list_1))
n = int(input())
sum = 0
for i in list_1:
    for j in list_1:
        for k in  list_1:
            add = i + j + k
            if add == n:
                sum = sum + 1
            else:
                pass
print(sum)
#binay search.
def binary_search(arr,element):
    start = 0
    end = len(list_1) - 1
    while start <= end:
        mid = (start + end)//2
        if list_1[mid] == element:
            return mid
        elif list_1[mid] < element:
            start = mid + 1

        else:
            end = mid - 1




    return -1


list_1 = [1, 3, 7, 18, 20, 26, 21, 28, 22, 32]
list_1.sort()
print(list_1)
index = binary_search(list_1,90)
print(index)
def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        minindex = i
        for j in  range(i+1,length):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i],arr[minindex] = arr[minindex],arr[i]



list_1 = [1,5,3,7,2,6,0]
selection_sort(list_1)
print(list_1)


def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


list_1 = [1, 8, 9, 0, 15, 2, 3, 9, 4, 8]
bubble_sort(list_1)
print(list_1)
def insertion_sort(arr):
    length = len(arr)
    for i in range(1,length):
        j = i - 1
        temp = arr[i]
        while j >=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp

list_1 = [9,8,5,6,7,1]
insertion_sort(list_1)
print(list_1)


def merge_sort(arr_1, arr_2, arr_3):
    i = 0
    j = 0
    while i < len(arr_1) and j < len(arr_2):

        if arr_1[i] < arr_2[j]:
            arr_3.append(arr_1[i])
            i = i + 1
        else:
            arr_3.append(arr_2[j])
            j = j + 1

    while i< len(arr_1):
        arr_3.append(arr_1[i])
        i = i + 1
    while j < len(arr_2):
        arr_3.append(arr_1[j])
        j = j + 1


list_1 = [1, 4, 9, 10]
list_2 = [2, 3, 6, 7, 8]
list_3 = []
merge_sort(list_1, list_2, list_3)
print(list_3)
#all zero at the end
def sort_list(list_1,list_2,list_3):
    for i in range(len(list_1)):
        if list_1[i] == 0:
            list_3.append(list_1[i])
        else:
            list_2.append(list_1[i])


list_1 = [2,0,0,1,3,0,0]
list_2 = []
list_3 = []
sort_list(list_1,list_2,list_3)
print(list_1)
print(list_2)
print(list_3)
print(list_2 + list_3)



def sort_left(list_1,n,list_2,list_3):
    for i in range(n,len(list_1)):
        list_2.append(list_1[i])


    for j in range(n):
        list_3.append(list_1[j])


list_1 = [1,2,3,4,5,6,7]
list_2 = []
list_3 = []
n = int(input("Entr the index where we want to break and join from left:"))
sort_left(list_1,n,list_2,list_3)
print(list_1)
print(list_2)
print(list_3)
print(list_2 + list_3)
#find the second largest in the array  or list.
list_1 = [2,13,4,1,3,6,28]
list_1.sort()
print(list_1[-2])
def check_rotation(list_1):
    x = 0
    length = len(list_1)
    for i in range(length):
        if list_1[i] < list_1[i+1]:
            pass
        else:
            print(i + 1)


list_1 = [3,6,8,9,10]
p = check_rotation(list_1)
print(p)
def dutch_national_flag(list_1,list_2,list_3,list_4):
    for i  in range(len(list_1)):
        if list_1[i] == 0:
            list_2.append(list_1[i])
        elif list_1[i] == 1:
            list_3.append(list_1[i])
        else:
            list_4.append(list_1[i])


list_1 = [0,1,2,0,2,0,1]
list_2 = []
list_3 = []
list_4 = []
dutch_national_flag(list_1,list_2,list_3,list_4)
print(list_1)
print(list_2 + list_3 + list_4)
#sr_1 = 'abcda'
#a1 = sr_1.replace("a","T")
#print(a1)
def replace(str,char1,char2):
    new_str = " "
    for char in str:
        if char == char1:
            new_str = new_str + char2
        else:
            new_str = new_str + char
str_1 = 'fsafsavxz'
a = replace(str_1,"s","d")
print(a)
def arepermu(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(b)
    for i in range(0,l1,1):
        if str1[i] != str2[i]:
            return False
    return True
if __name__ == '__main__':
    str1 = input()
    str2 = input()
    if(arepermu(str1,str2)):
        print("YES")
    else:
        print("NO")

#remove consecutive duplicate
def rem_con(str1):
    seen = str1[0]
    ans = str1[0]
    for i in str1[1:]:
        if i != seen:
            ans = ans + i
            seen = i
    return ans
str1 = 'aabccbaa'

a = rem_con(str1)
print(a)


#reverse each word
str1 = 'Welcome to Coding Ninjas'
b =''
list1 = str1.split(" ")
print(list1)

for i in range(len(list1)):
    a = list1[i]
    lenght = len(a)
    while lenght>0:
        b = b + a[lenght-1]
        lenght = lenght - 1
print(b)

#Remove character
str1 = input()
n = input()
for i in str1:
    if i == n:
        str1 = str1.replace(n,"")

    else:
        pass
print(str1)
#taking two input at a time
str = input("enter:").split()
n,m = int(str[0]),int(str[1])
print(n)
print(m)
li = [[int(j) for j in input().split()] for i in range(n)]
print(li)
str = input().split()
n,m = int(str[0]),int(str[1])
b = input().split()
arr = [[int(b[m * i + j]) for j in range(m)]for i in range(n)]
print(arr)
def lar_col_sum(li):
     row_len = len(li)
     col_len = len(li[0])
     max_sum = -1
     max_colindex = -1
     for j in range(m):
          sum = 0
          for i in range(n):
               sum = sum + li[i][j]
          if sum > max_sum:
               max_colindex = j
     return max_sum,max_colindex

str = input("enter:").split()
n,m = int(str[0]),int(str[1])
print(n)
print(m)
li = [[int(j) for j in input().split()] for i in range(n)]
print(li)
a = lar_col_sum(li)
print(a)
#print first nonreapt letter
str1 = 'aDcadhc'
length = len(str1)
m = {}
for i in str1:
     if i in m:
          m[i]= m[i] + 1
     else:
          m[i] = 1
for i in str1:
     if m[i] == 1:
          print(i)
          break
str1 = 'Abhishek harshit Ayush harshit Ayush Iti Deepak Ayush Iti'
list1 = str1.split()
length = len(str1)
m = {}
for i in list1:
     if i in m:
          m[i] += 1
     else:
          m[i] = 1
print(m)
def sum_natu(n):
     if n == 0:
          return 0
     else:
          a = n + sum_natu(n-1)
          return a



n = int(input("Enter the value of n:"))
b = sum_natu(n)
print(b)


def pow(a, b):
    if a == 0 or b == 0:
        return 1
    else:
        x = a * pow(a, b - 1)
        return x


a = int(input())
b = int(input())
y = pow(a, b)
print(y)


def issorted(list):
    l = len(list)
    if l == 0 or l == 1:
        return True
    if list[0] > list[1]:
        return False
    small_list = list[1:]
    x = issorted(small_list)
    if x:
         return True
    else:
         return False


list = [1,4,6,8,2,3]
w = issorted(list)
print(w)
def sum_array(arr,sum):
     for i in arr:
          sum = sum + i
     return sum
array = [7, 4, 9, 11, -3]
sum = 0
a = sum_array(array,sum)
print(a)


class Fraction:
    def __init__(self, num = 0, den = 1):
        if den == 0:
            den = 1
        self.num = num
        self.den = den

    def print(self):
        if self.num == 0:
            print(0)
        elif self.den == 1:
            print(self.num)
        else:
            print(self.num, '/', self.den)

    def simply(self):
        current = min(self.num,self.den)
        while current > 1:
            if self.num % current == 0 and self.den % current == 0:
                break
            current -= 1
        self.num = self.num//current
        self.den = self.den // current



f = Fraction(14, 6)

f.simply()
f.print()"""


def maxxx(a,b,c):
    if a > b and a > c:
        print("a is greatest")
    elif b > a and b > c:
        print("b is greatest")
    else:
        print("c is greatest")


a = int(input())
b = int(input())
c = int(input())
maxxx(a,b,c)

