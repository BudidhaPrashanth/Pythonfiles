
#polindrome
def pal(num):
    x = num[::-1]
    if x ==num:
        print("its polindrome")
    else:
        print("its not polindrone")

print(pal("bablu"))
print(pal("madam"))
print(pal("121"))

#astrantnum

def ast(num):

    #return  sorted(str(num))
    x = 0
    for i in sorted(str(num)):
        x += int(i)**3

    if x ==num:
        print("its astrom number")
    else:
        print("no ita not num")
print(ast(153))