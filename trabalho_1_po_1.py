# -*- coding: utf-8 -*-
"""Trabalho 1 - PO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zib5uDsJRR_v_ta4il1JZCuCmqP5ZVE-
"""

'''

TRABALHO 1 - PO

Gabriel Lucena Camboim
Lucas Henrique Lopes Rodrigues da Silva
Bruno Henrique Araújo da Costa

  - Referência: https://developers.google.com/optimization/reference/python/graph/pywrapgraph
  - Como utilizar: Coloque os arquivos "instance" de 1-7 disponibilizados pelo professor
    e altere o nome do arquivo aberto para que o código seja executado no arquivo desejado.

'''

from ortools.graph import pywrapgraph   #Biblioteca utilizada para calcular a solução  

arquivo = open("instance1.txt", "r")        #Abrindo o arquivo
arquivo.readline()                           #Pulando a linha duas vezes para pegar o índice da origem
arquivo.readline()                     
s = arquivo.readline()                     #Índice da origem (início)
t = arquivo.readline()                     #Índice do escoadouro (fim)

#Separado em três arrays diferentes o nó de começo do arco, nó de fim do arco e sua capacidade
node_start = []                            
end_nodes = []
capacities = []


for linha in arquivo:           #Preenchendo os arrays
    valores = linha.split()     #Separa a linha em índices e cada índice vai para um array
    node_start.append(int(valores[0]))
    end_nodes.append(int(valores[1]))
    capacities.append(int(valores[2]))

flow = pywrapgraph.SimpleMinCostFlow()          #Inicializando o algoritmo PFCM

for i in range(0, len(node_start)):  
    #Custos de cada arco: Para fazer a transformação de PFM para PFCM é necessário colocar os custos de cada arco em zero
    flow.AddArcWithCapacityAndUnitCost(node_start[i], end_nodes[i], capacities[i], 0)  #Adicionando os arcos no algoritmo com o custo 0

#Adicionando o último arco com capacidade "infinita" no algoritmo e custo -1 pois o final tem que ser o único local com custo diferente de zero
#Com isso, os índices de origem e de escoadouro também são nós de transbordo
flow.AddArcWithCapacityAndUnitCost(int(t), int(s),100000000000000000, -1) 

#Daqui pra baixo são só os prints
print('--------------------')

if flow.SolveMaxFlowWithMinCost() == flow.OPTIMAL:  #Verificando se a solução encontrada é uma solução ótima    
    print('| Custo mínimo:', -1*flow.OptimalCost())   
    print('--------------------')
    print('|    Arco    Fluxo ')
    for i in range(flow.NumArcs()):
      if flow.Flow(i) > 0:                   #Exibindo somente os fluxos não nulos como requisitado no trabalho
        print('|   %1s -> %1s   %3s' % (
            flow.Tail(i),
            flow.Head(i),
            flow.Flow(i),
            ))
else:
    print('Erro na entrada')

print('--------------------')