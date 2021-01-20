l  = ["tony",'spider',"thor","antman","panther","captain",'loki','marvel']
user = "Welcome to birthday dictionary !!! \nWe know birthdays of : "
print(user)
for i in l:
    print(i)
user1 = print("who's birthday do you want look up ? ")
name = input("Enter a name : ")
d = {
    "tony" : '25-12-1965',
    'spider' : '12-5-1945',
    'thor' : '29-2-1962',
    'antman' : '9-9-1999',
    'panther' : '13-7-1972',
    'captain' : '12-11-1910',
    'marvel' : '15-4-1982',
    'loki' : '24-8-1935',


}

for i ,j in d.items():
    if i == name:
        print("{0}'s birthday is {1}.".format(i,j))





