class Grafo:
    def __init__(self, listaAdjacencias = [], matrizAdjacencias = [], grafosTotais = [], arestasGrafo = []):
        self.matrizAdjacencias = matrizAdjacencias
        self.listaAdjacencias = listaAdjacencias
        self.grafosTotais = grafosTotais
        self.arestasGrafo = arestasGrafo

    #-------------------------------------------------------------------------------------
    def cadastrarGrafos(self):
        tipoGrafo = '0'
        escolha = input('Deseja cadastrar um Grafo [y/n]: ')
        escolha = escolha.strip().lower()

        #Decide a forma de cadastro do Grafo
        if escolha == 'y':
            print("Que forma você deseja cadastrar seus Grafos?")
            print("Digite [1] para lista de adjacências.")
            print("Digite [2] para Matriz de adjacências.")
            print("Digite [0] para Sair.")

            tipoGrafo = input("Digite sua Escolha: ")
            tipoGrafo = tipoGrafo.strip().lower()
            
        elif escolha == 'n':
            print("Cadastro Encerrado!")
        else:
            print("Digite um valor Válido!")
            self.cadastrarGrafos()
        
        #Cadastra efetivamente o Grafo
        if tipoGrafo == '1':
            self.cadastraListaAdjacencias()
        elif tipoGrafo == '2':
            self.cadastraMatrizAjacencias()
        elif tipoGrafo == '0':
            pass
        else:
            print("Houve um erro ao decidir o tipo de cadastro!")
            self.cadastrarGrafos()
    
    #-------------------------------------------------------------------------------------
    def cadastraListaAdjacencias(self):
        #Inicio Variaveis
        grafo = ''
        cadLista = 'y'
        listaArestas = []
        listaGrafosTotais = []

        while cadLista == 'y':

            #Inicio Variáveis
            adjacencia = ''
            grafo = ''
            listaAdjacenciasTemp = []


            #Cadastra o Grafo principal que terá suas Adjacencias digitadas
            print("Cadastro de Nova Lista de Adjacencias!!")
            grafo = input(f'Digite o nome do Grafo que será inserido as Adjacências: ')
            grafo = str(grafo.strip()).lower()
            listaAdjacenciasTemp.append(grafo)


            #Cadastra Adjacências do Grafo
            while True:
                #Insere grafo
                print("Digite 'sair' caso queira encerra o ESTA lista Adjacências!!!")
                adjacencia = input(f'Insira um Grafo Adjacente de {grafo}: ')

                #Valida se o usuário quer sair
                if adjacencia == "sair":
                    break
        
                #Trata e insere a adjasencia
                adjacencia = adjacencia.strip().lower()
                listaAdjacenciasTemp.append(adjacencia)

                #Valida mais adjacencias
                print("------------------------------------------------------------------")
                print(f'Lista de Adjacências do Grafor {grafo} atualizada!')
                print(f'Lista atual de Adjacências: {listaAdjacenciasTemp}')
                print("------------------------------------------------------------------")

                #Registra Aresta
                listaArestas.append((grafo, adjacencia))
            
            #Valida se o usuário quer inserir mais uma lista de adjacencias
            if cadLista == 'y':
                while True:
                    cadLista = input('Deseja cadastrar outra lista de Adjacencias? [y/n]: ')
                    cadLista = cadLista.strip().lower()
                    if cadLista not in ['y', 'n']:
                        print('Coloque uma entrada válida!')
                    else:
                        print("Cadastro Encerrado!")
                        break


            #Insere na Lista de feita a lista maior
            self.listaAdjacencias.append(listaAdjacenciasTemp)

        #Calcula os vertices encontrados na lista de Ajacências
        for linha in self.listaAdjacencias:
            for grafinho in linha:
                listaGrafosTotais.append(grafinho)
        
        #Remove as duplicatas 
        self.grafosTotais = list(set(listaGrafosTotais))

        
        #Atualiza o Valor de arestas do Grafo
        self.arestasGrafo.extend(listaArestas)

    #-------------------------------------------------------------------------------------
    def cadastraMatrizAjacencias(self):
        grafo = ''
        aresta = ''
        listaAresta = []

        #Cadastra os Grafos da Matriz
        print("--[Digite 'concluir' para sair do cadastro de grafos da Matriz de Adjacencias]---")
        print("--[Insira os grafos que serão detalhados na MAtriz de Adjacências]--")
        while grafo != 'concluir':
            grafo = input(f'Digite o nome do Grafo: ')
            grafo = str(grafo.strip()).lower()
            self.grafosTotais.append(grafo)
        
        #Retira a palavra concluir da lista de grafos
        self.grafosTotais.pop()
        
        #Mostra ao Usuário a lista de Grafos
        print("------------------------------------------------")
        print(f'Grafos registrados: {self.grafosTotais}')
        print("------------------------------------------------")

        #Produz a Matriz de Adjacências
        for grafoColuna in self.grafosTotais:
            linhaTemp = []
            for grafoLinha in self.grafosTotais:
                    print('Digite [1] para Verdadeiro e [0] para Falso')
                    aresta = input(f'Aresta: {grafoColuna} --> {grafoLinha}: ')
                    aresta = aresta.strip().lower()
                    linhaTemp.append(aresta)

                    #Registra Aresta
                    if aresta != '0':
                        listaAresta.append((grafoColuna, grafoLinha))   

            #Atualiza a Matriz do grafo geral
            self.matrizAdjacencias.append(linhaTemp)
        
        #Atualiza o Valor de arestas do Grafo
        self.arestasGrafo.extend(listaAresta) 
    
    #-------------------------------------------------------------------------------------
    def getVertices(self):
        return self.grafosTotais

    #-------------------------------------------------------------------------------------
    def getArestas(self):
        return self.arestasGrafo
        