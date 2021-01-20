import random


l = ["prashanth",'ravi','srikanth','sagar']
print(random.choice(l))

print(random.sample(l, 2)) # no .of samples need i.e 2
print(random.randrange(1, 10))
print(random.randint(1, 10))
random.seed(3)
print(random.randrange(10))
random.seed(3)
print(random.randrange(10))
