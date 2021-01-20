f= open("jpg.jpg","rb")

f1 = open("mypic.jpg","wb")
for i in f:
    f1.write(i)
f1.close()