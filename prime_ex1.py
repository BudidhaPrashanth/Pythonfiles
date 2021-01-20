def prime(n):
    if n ==1:
        print('its not prime')
    for i in range(2,n):
        if n%i ==0:
            break
    else:
        print(n)
for n in range(1,101):
    prime(n)
