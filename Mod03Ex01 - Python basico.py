#!/usr/bin/env python
# coding: utf-8

# ### 01 - Teste de gravidez
# Escreva uma célula com controle de fluxos que tem como premissa a existência das seguintes variáveis:
# 
# - ```sexo``` como ```str``` indicando os valores '**M**' para masculino e '**F**' para feminino  
# - ```beta_hcg``` que indica a quantidade do beta-HCG no sangue em mUI/mL.
# 
# A sua tarefa é escrever um código que imprima como resultado "indivíduo do sexo masculino" quando sexo = 'M', caso sexo = 'F', se o valor de beta-HCG for maior que 5, retorne "Positivo" indicando que a paciente está grávida, e retorne "Negativo" caso contrário.
# 
# Não mexa nos valores da variável ```sexo``` nem em ```beta_hcg```, e escreva um código que funcione para quaisquer valores possíveis de ambos: ```sexo``` = '**M**' ou '**F**' e ```beta_hcg``` assumindo valores inteiros positivos.

# In[16]:


sexo = 'M'
beta_hcg = 0

sexo = input("Digite M para sexo masculino ou F Para feminino: ")
if sexo == "M":
    print("Indivíduo do sexo masculino")
elif sexo == "F":
    beta_hcg = int(input("Digite o valor de Beta-HCG: "))
    if beta_hcg > 5:
        print("Positivo")
    else:
        print("Negativo")




# ### 02 - Renomeando variáveis
# 
# Vamos ver adiante que uma forma de renomear variáveis de um conjunto de dados é através de dicionários - o dicionário deve conter como chave o nome original, associando a cada chave um único valor (tipo *str*) que contenha o nome novo.
# 
# A sua tarefa é escrever um dicionário que possa ser utilizado para traduzir as variáveis ```name``` (nome), ```age``` (idade) e ```income``` (renda). Ou seja, esse dicionário deve relacionar as chaves *name, age* e *income* às suas respectivas traduções.

# In[17]:


dic_renomeacao = {'name':'nome', 'age':'idade','income':'renda'}
dic_renomeacao


# ### 03 - É divisível?
# A sua tarefa é escrever um código que indique se um número ```N``` é divisível por um número P. Escreva um programa que faça essa verificação para quaisquer combinações de ```N``` e ```M``` e devolva uma mensagem indicativa no output.

# In[19]:


N = 42
M = 7

N = int(input('Digite um valor: '))
M = int(input('Digite outro valor: '))

if N % M == 0:
    print(f'O valor {N} é divisível por {M}')
else:
    print(f'O valor {N} não é divísivel por {M}')
    


# ### 04 - Números primos
# > Um número **N** é primo se e somente se é divisível por 1, -1, por **N** e por -**N**.  
# 
# Escreva um script que verifica se ```N``` é um número primo, verificando se ```N``` é divisível por todos os números de ```1``` a ```N-1```. Você vai precisar usar alguma ferramenta de *loop* que você aprendeu para isto. No final, devolva uma mensagem no output indicando se o número é primo ou não.

# In[21]:


N = 47

N = int(input("Digite um número inteiro positivo: "))

for i in range(2, N):
    if N % i == 0:
        print(N, "não é um número primo")
        break
else:
    print(N, "é um número primo")


# ### 05 - Desafio
# O algorítmo do exercício anterior não é o mais eficiente. O que você pode fazer para deixá-lo mais eficiente? Ou seja, executar menos comparações, portanto consumir menos tempo.
# 1. Será que precisamos correr o loop até o final sempre?
# 2. Será que precisamos mesmo verificar **todos** os números?
# 3. Será que precisamos ir até N-1?
# 
# Essas perguntas levam ao tipo de pensamento voltado a deixar um algoritmo mais eficiente. Veja se você consegue melhorar o seu.

# In[6]:


# Utilizando uma função lambda - retornará True para primo e False para número composto


primo = lambda N: N > 1 and all(N % i != 0 for i in range(2, N)) 

#função lambda recebe um argumento N (um número)
# verifica se N é maior que 1, pois todos os números primos são maiores que 1
#all: verifica se todos os elementos da lista são True
#(N % i != 0 for i in range(2, N))  : verifica se o valor digitado é divisivel por i (iniciando por 2) 
# já que todo número é dividido por 1 e por ele mesmo o valor do range vai até N-1 e verifica se é divisível até o fim da operação
# se não for divisível por nenhum dos números da lista, é portanto, um número primo.



primo(17)



# ### 06 - Peso ideal 1
# O IMC (índice de massa corpórea) é um indicador de saúde mais bem aceito que o peso. Ele é calculado como:
# 
# $$ IMC = \dfrac{peso}{altura^2}$$
# 
# Segundo a OMS, valores *normais* são entre 18.5 e 24.9.
# 
# Sua tarefa é encontrar o ponto médio dessa faixa.

# In[22]:


imc_ideal = (18.5 + 24.9) / 2
imc_ideal


# ### 07 - Peso ideal 2
# Recebendo um valor de altura, encontre o peso '*ideal*' dessa pessoa, que fornece o IMC encontrado acima

# In[26]:


altura = 1.70

altura = float(input('Digite a altura: '))

IMC_ideal = 21.7
peso_ideal = IMC_ideal * altura**2

print("O peso ideal para a altura de", altura, "metros é de", peso_ideal, "quilos.")



# ### 08 - Peso ideal 3
# Dada uma lista contendo as alturas de pacientes, crie uma nova lista que contenha o peso '*ideal*' (que fornece o IMC calculado em **Peso ideal 1**) desses pacientes.

# In[28]:


lista_alturas = [1.95, 2.05, 1.70, 1.65]

lista_peso_ideal = []
IMC_ideal = 21.7

for i in lista_alturas:
    peso_ideal = IMC_ideal * i **2
    lista_peso_ideal.append(peso_ideal)


lista_peso_ideal


# ### 09 - Peso ideal 4
# Dada uma lista de tuplas - cada elemento da lista é uma tupla contendo altura e peso de um paciente - crie uma nova lista com o IMC desses pacientes.

# In[29]:


altura_peso = [(1.80, 90), (1.65, 75), (1.91, 70)]

imc_lista = []

for tupla in altura_peso:
    altura, peso = tupla
    imc = peso / altura ** 2
    imc_lista.append(imc)

imc_lista


# ### 10 - Peso ideal 5
# Dada uma lista de **listas** - cada elemento da lista é uma **lista** contendo altura e peso de um paciente, adicione mais um elemento à lista de cada paciente contendo o IMC do paciente. Verifique também se é 'baixo', 'normal' ou 'alto' segundo os padrões da OMS em que normal é entre 18.5 e 24.9.
# 
# Reflexão: por que no problema anterior temos que criar uma nova lista, e não podemos adicionar os dados de cada indivíduo à tupla?

# In[35]:


# não se pode adicionar à tupla porque esse tipo de dados é imutável.

altura_peso = [[1.80, 90], [1.65, 75], [1.91, 70]]

for paciente in altura_peso:
    altura, peso = paciente
    imc = peso / altura ** 2
    paciente.append(imc)
    if imc < 18.5:
        paciente.append('baixo')
    elif imc >= 18.5 and imc <= 24.9:
        paciente.append('normal')
    else:
        paciente.append('alto')

altura_peso


# In[ ]:




