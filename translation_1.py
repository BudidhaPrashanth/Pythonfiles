def transalte(word):
    transalation = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transalation = transalation + "G"
            else:
                transalation = transalation + "g"
        else:
            transalation = transalation + letter
    return transalation

print(transalte(input("enter a word: ")))