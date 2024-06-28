"""
Escreva um programa que conte o número de 
palavras em uma frase fornecida pelo usuário.
"""   
frase = input("Qual seu hobby? ")
tamanho_da_frase = len(frase)

if frase:
    print(f'Sua frase tem {len(frase)} palavras. ')

else:
    print(f'Desculpe, você deixou campo vazio, Preencha-lo!. {frase}')