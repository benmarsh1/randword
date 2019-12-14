import random
vowels = ["a","e","i""o","u","oo","ee"]
constanants = ["b","c","d","f","g","h","j","k","l","m","n","p","qu","r","s","t","v","w","y","z","ch","sh"]
word=[]
output=""

def gen_word(length):
    num=1
    for i in range(length):
        if num % 2 == 1:
            char=random.choice(vowels)

        else:
            char = random.choice(constanants)
        num+=1
        word.append(char)
    join=output.join(word)
    join = join[(len(join))-length:]
    return join
