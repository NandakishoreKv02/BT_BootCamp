import random 
#x="Hello".lower()
list_of_words=["Apple","Banana","Papaya"]
x=random.choice(list_of_words)
print(list(x))
n=len(x)
x=x.lower()
blank_word=["_"]*n
print(" ".join(blank_word))
chances=6

while chances>0:
    fg=False
    l=input(f'Enter a letter (chances left {chances}): ').lower()
    for i in range(n):
        if x[i]==l:
            blank_word[i]=x[i]
            fg=True
    if '_' not in blank_word:
        print("You have successfully guessed the word "+"".join(blank_word))
        break
    if not fg:
        chances-=1
        print("Please Try again ")
    print(" ".join(blank_word))
if chances<=0:   
    print("Sorry You lost the game")
