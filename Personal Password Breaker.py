# Projeto para criar variaveis de uma senha com informações previas de um individuo - Versao simples
from itertools import permutations

#Pega o documento com as informacoes e transforma em uma lista
def cria_lista(path_file):
    with open(path_file, "r") as file:    
        infos = [linhas.rstrip() for linhas in file]
    return infos

#Permuta/Embaralha as palavras
def shuffle(lista):
    return list(permutations(lista))

def main():
    path_file = "dados.txt"
    info = cria_lista(path_file)
    info = shuffle(info)
    for i in info:
        #Concatena as listas em "strings"
        print(''.join(i))
        
        
if __name__ == "__main__":
    main()