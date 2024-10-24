
#printer ut noen tall som er lagt sammen
x = 5
y = 11
z = 8
print (x + y + z)

#lagde en verdi som inneholder et navn
my_name = "Lars"
print(my_name)

#legger sammen x, y, z til en verdi
my_age = (x + y + z)
print (my_age)


#lagd en list som printer ut "banana"
my_list = ["apple", "banana", "orange"]
print (my_list[1])
#printer ut hvor mange "ting" som er i listen
print (len(my_list))
#ser om "apple" er i listen, og gir en melding hvis den er.
if "apple" in my_list:
    print ("apple in this list")


#byttet ut "volvo" til "mercedez"
new_list = ["bmw", "volvo", "audi"]
new_list[1] = "mercedez"
print (new_list)

#bytter ut alt fra posisjon 1 til 5 med "car1" "car2",
new_list_1 = ["bmw", "volvo", "audi", "mercedez", "ford"]
new_list_1[1:5] = ["car1", "car2"]
print(new_list_1)

#legge til en "ting" i listen uten å fjerne noe.
new_list_2 =["bmw", "volvo", "audi"]
new_list_2.insert(1, "mercedez")
print(new_list_2)
#legge til ting på slutten av listen.
new_list_2.append("ford")
print(new_list_2)

#liste sortert oppover og nedover.
numeric_list = [1,5,7,6,9,8,4,3,2]
numeric_list.sort(reverse =True)
print(numeric_list)
numeric_list.sort()
print(numeric_list)


def myfunc(n):
    return abs(n - 50)

list1 = [100,50,70,60,80,90]
list1.sort(key=myfunc)
print(list1)