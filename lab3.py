#Задача 1 номер 9

arr = ["asd","rgrg","xcvxc","qw","efef","ffff","vcbvb","asas","ikii","iii",]

print(arr[3], arr[5])

arr_chet = [arr[i*2] for i in range(len(arr)//2)]
print("".join([arr_chet[i] for i in range(len(arr_chet)-1,0,-1)]))

print(arr[-2],arr[-1])

print(arr.count(arr[0]))

print("Словосочетание \"найди меня\" " + "найдено" * ("найди меня" in arr) + "не найдено" * (not ("найди меня" in arr)))


#Задача 2 номер 12


A = {1,4, "Ababa", "UHUHU", "TEXt"}
lis_chet = [i for i in range(0,10,2)]
B = set(lis_chet)

print(A|B, A&B, A-B)


C = {"adada", "TEXt","aerear", "ewwewewe", "rrrrrr"}

print(A|B|C, len(A|B|C))

print("All A elements are in C" * A.issubset(C) + "Not all A elements are in C" * (not A.issubset(C)))




#Задача 3 номер 13

s = "Hello World!"
A = {}
for d in s:
    A[d] = s.count(d) 
    

ch = input("Enter a char ")
if ch in A:
    print(A[ch])
else:
    print(None)

A.clear()
