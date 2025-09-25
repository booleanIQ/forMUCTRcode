#Task Z1 ( number 16)

stri = "D:\\MAs\\Videos\\ph\\Tosortphotos\\photo.jpeg"
print("Корневая папка — " + stri.split("\\")[0]+"\\")


#Task Z2 ( number 12)

stra = "IwISH"
strb = "IWasAnHappyPerson"

lena = len(stra)
lenb = len(strb)


strsum = stra + strb
print(strsum)
strsum = "".join([stra,strb])
print(strsum)



strb_twice = strb*2
print(strb_twice)


stralower = stra.lower()
strbupper = strb.upper()
print(stralower)
print(strbupper)

print("Строка содержит только цифры " * stra.isdigit() + "Строка содержит только буквы" * stra.isalpha())

#TASK Z3 (number 2)

s = "Lost where the forest would grow"
s_test = "Эту строку нужно обработать при помощи срезов"

s_new = s[-5:] + s[7:0:-3]
print(s_new)

s_new = s_test[-5:] + s_test[7:0:-3]
print(s_new)


#TASK Z4 (number 5)

s = "Кажется это длинная строка"

print("{:*^20.7}".format(s))

print(f"{s:*^20.7}")
