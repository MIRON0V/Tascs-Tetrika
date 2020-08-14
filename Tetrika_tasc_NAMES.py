file = open('C:/Users/russi/Downloads/Names.txt', 'r') 
names = file.readline().split(',')
names.sort() 

alphabet = 'abcdefghijklmnopqrstuvwxyz' 
alph = {}
for i in range(len(alphabet)):
        alph[alphabet[i]] = i + 1

def countLetters(w):
    sum = 0
    for i in w.capitalize()[1:len(w)-1]:                     
        sum += alph[i]
    return sum


for ind in range(len(names)):
    sum = 0
    sum += countLetters(names[ind]) * (ind + 1)

print(sum)

file.close()


# result: 377045








