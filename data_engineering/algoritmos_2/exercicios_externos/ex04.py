'''
04 - make a program that read a sentence and display how many consonants there are in this sentence / Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

einstein_quote = 'Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution.'
count = 0
for letter in einstein_quote:
    if letter == " ":
        continue
    elif letter == "a" or "e" or "i" or "o" or "u":
        count += 1
        
print(count)
# list_einstein_quote = einstein_quote.split()
# print(len(list_einstein_quote))