#chamando funcaoes atraves de listas

def pri1():
    print('esse e um funcao que quero chamr atraves dde uma lista')

def pri2():
    print('mesma coisa')

def pri3():
    print('funcao diferenciada')

def func_list(*args):#elementos passados como para metros ficarao dentro desse args
    lista = []
    lista.extend(args)#entao a lista vai recebelos aqui, extend e usado para fazer uma copia dos valores...

    for i,funcao in enumerate(lista, 1):# enumerate esta interligado com a primeira variavel devolvera valores a ela, segundo parametro fara com que comece inumerar apartir de 1
        print(f"{i}. para a funcao({funcao.__name__}) ")# se voce nao coloca o __name__ meio que ela retorna um id da funcao

    qual = int(input('escolha a funcao desejada:'))
    #aqui voce colocara indice da lista que retornara a funcao respectiva
    while qual < 1 or qual > len(lista):
        
        print('desculpa, a funcao escolhida nao existe, tente novamente:')
        qual = int(input('escolha a funcao desejada:'))
    
        
    

    funcao_exe = lista[qual - 1] # variavel ira se igualar ao idice que coporta o metodo entao ela se torna a função
    funcao_exe() #executando o metodo selecionado.

    
        
        
        
func_list(pri1,pri2)# primeira maneira e adicionar manualmente cada funcao que deseja colocar

# Segunda maneira usando uma lista
lista2 = [pri1, pri3]
func_list(*lista2)  # Use o operador * para desempacotar a lista ao chamar a função








