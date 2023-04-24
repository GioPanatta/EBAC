#!/usr/bin/env python
# coding: utf-8

# ## Exercício 1: Vestibular
# 
# Considere que a os dados gerados na célula abaixo contêm o número de acertos de 100 alunos em um vestibular para um curso de exatas, divididas pelos respectivos assuntos. Considere que cada assunto possui um número de questões conforme a tabela abaixo:
# 
# | assunto | número de questões |
# |:---:|:---:|
# | Matemática | 24 |
# | Português | 18 |
# | Geografia | 8 |
# | Inglês | 8 |
# | História | 8 |
# | Física | 12 |
# | Química | 12 |
# 
# Usando os comandos de operações com DataFrames que você aprendeu na Aula 03, calcule:
# 
# 1. (operações com escalar) Calcule o percentual de acerto dos alunos por assunto.  
# 2. (operações entre *DataFrames) Calcule o total de acertos de cada aluno.  
# 3. Calcule o porcentual geral de cada aluno.  
# 4. Suponha que a nota de corte para a segunda fase seja 45. Quantos alunos tiveram nota maior que 45?  

# In[138]:


import pandas as pd 
import numpy as np

np.random.seed(42) 

df_mat = pd.DataFrame(np.random.randint(24, size=(100, 1)), columns=['Qt_acertos'])

df_por = pd.DataFrame(np.random.randint(18, size=(100, 1)), columns=['Qt_acertos'])

df_geo = pd.DataFrame(np.random.randint(8, size=(100, 1)), columns=['Qt_acertos'])

df_ing = pd.DataFrame(np.random.randint(8, size=(100, 1)), columns=['Qt_acertos'])

df_his = pd.DataFrame(np.random.randint(8, size=(100, 1)), columns=['Qt_acertos'])

df_fis = pd.DataFrame(np.random.randint(12, size=(100, 1)), columns=['Qt_acertos'])

df_qui = pd.DataFrame(np.random.randint(12, size=(100, 1)), columns=['Qt_acertos'])

df_mat, df_por


# In[139]:


# 1) Seu código aqui / (operações com escalar) Calcule o percentual de acerto dos alunos por assunto.
pc_mat = df_mat / 24 * 100
pc_por = df_por / 18 * 100
pc_geo = df_geo /  8 * 100
pc_ing = df_ing /  8 * 100
pc_his = df_his /  8 * 100
pc_fis = df_fis /  12 * 100
pc_qui = df_qui /  12 * 100



# In[107]:


# 2) Seu código aqui (operações entre *DataFrames) Calcule o total de acertos de cada aluno.
total["Total_acertos"] = df_mat['Qt_acertos'] + df_por['Qt_acertos'] + df_geo['Qt_acertos'] + df_ing['Qt_acertos'] + df_his['Qt_acertos'] + df_fis['Qt_acertos'] + df_qui['Qt_acertos']
total["Total_acertos"]


# In[93]:


# 3) Seu código aqui / Calcule o porcentual geral de cada aluno.
total["Percentual_total"] = total["Total_acertos"] /90*100
total["Percentual_total"]


# In[88]:


total[]


# In[119]:


# 4) Seu código aqui / Quantos alunos tiveram nota maior que 45?
total_gt_45 = total["Total_acertos"]>  45
count_gt_45 = total_gt_45.sum() #Deve-se usar o método sum() para somar o total de True da condição booelana anteior
count_gt_45


# ## 2) Vestibular II
# 
# Ainda sobre o mesmo banco de dados:
# 
# 1. Neste vestibular, quem 'zera' em matemática, física ou química está desqualificado. Monte um novo *DataFrame* com os alunos desqualificados por este critério.
# 2. Quantos são esses alunos?
# 3. Qual a média desses alunos em história e geografia?
# 4. Monte um *DataFrame* com os alunos que passaram para a segunda fase. Repare que estes alunos não podem ter sido desqualificados.

# In[116]:


#Novo DataFrame com os alunos que acertaram 0
df_mat[df_mat["Qt_acertos"] == 0]
df_fis[df_fis["Qt_acertos"] == 0]
df_qui[df_qui["Qt_acertos"] == 0]


# In[118]:


#Contagem dos Alunos que acertaram 0 = 9
df_mat['Qt_acertos'].value_counts()[0] # value_counts()[0] retorna o número de linhas que contêm 0
df_fis["Qt_acertos"].value_counts()[0]
df_qui["Qt_acertos"].value_counts()[0]


# In[ ]:





# # 3) Vacinações no Acre
# Vamos trabalhar agora com a base de vacinações no Acre. Para facilitar a sua vida, copiamos o link do arquivo na célula abaixo.
# 
# 1. Quantas vacinas estão registradas nessa base?  
# 2. Quantos pacientes foram vacinados? (considere um paciente para cada valor único de ```paciente_id```)  
# 3. Quantos pacientes únicos tomaram a primeira dose? OBS: Há um caractere especial neste campo. Receba os valores do campo com o método ```.unique()```.   
# 4. Quantos pacientes com menos de 18 anos foram vacinados?  
# 5. Quantos estabelecimentos aplicaram vacina no Acre?
# 
# 
# **OBS:** O portal do DATASUS pode apresentar instabilidades, retornando um erro na segunda célula abaixo. Por este motivo está disponível uma base estática, que se for baixada para o seu *working directory* pode ser lida com este comando: ```df = pd.read_csv('registros de vacinacao covid ACRE.csv', sep=';')```.
# 
# **OBS2:** Para saber qual é o seu working directory, rode no jupyter: ```!pwd```.

# In[142]:


#Não foi possível adiquirir o dataset direto da web, fiz o download conforme as intruções acima.
#Embora estoure um erro de "mixed types o DF funcionou normalmente

df = pd.read_csv('registros_vacinacao_COVID_Acre.csv', sep=';')


# In[143]:


df.head()


# In[161]:


print(df.columns)


# In[149]:


#VIsualizando as descrições das vacinas
df["vacina_descricao_dose"].value_counts()


# In[146]:


#1quantas vacinas aplicadas no total: 
df["vacina_descricao_dose"].count()


# In[187]:


df.shape #df.shape retorna uma tupla com duas dimensões (linhas/colunas)


# In[188]:


#1quantas vacinas aplicadas no total: verificando todas as linhas (registros) já que cada vacina é um registro
df.shape[0] #para obter somente o número de linhas, deve-se usar shape[0] onde 0 representa o primeiro elemento da tupla (linha)


# In[151]:


# 2)  Quantos pacientes foram vacinados?
df['paciente_id'].nunique() #método nunique retorna o número de valores únicos, no caso, da coluna paciente_id. 
# o método unique retorna um array com os valores unicos, no caso, retornaria todos os pacientes_id já que id é por si único


# In[192]:


# 3) 
primeira_dose = df['vacina_descricao_dose'].unique()[0] 
df['paciente_id'].loc[df['vacina_descricao_dose'] == primeira_dose].nunique()


# In[191]:


# 3) solução alternativa
primeira_dose = df['vacina_descricao_dose'].unique()[0]
df_primeira_dose = df[df['vacina_descricao_dose'] == primeira_dose]
df_primeira_dose['paciente_id'].nunique()


# In[157]:


# 4) 
df_menor = df[df["paciente_idade"]<18]
df_menor['paciente_id'].nunique()


# In[162]:


# 5)
df['estabelecimento_razaoSocial'].nunique()


# ## 4) Vacinação II
# Gere um *DataFrame* que contenha somente os estabelecimentos que aplicaram vcinas a menores de 18 anos. Nesse *DataFrame* devem conter somente os dados dos estabelecimentos, mais uma coluna sendo a quantidade de vacinas que o estabelecimento aplicou a menores de 18 anos.  
#   
# 1. crie uma cópia do *DataFrame* original, contendo somente os registros de vacinas realizadas a menores de 18 anos.  
# 2. crie uma lista das colunas desse *DataFrame* com o atributo de *DataFrame* **.columns()**  
# 3. Nesse *DataFrame* faça uma contagem do campo ```vacina_categoria_nome```.
# 3. a partir da lista de colunas, escolha somente aquelas que são referentes ao estabelecimento, faça uma lista com esses valores.  
# 4. usando o método *.loc*, selecione somente essas variáveis  
# 5. Aplique o método **.drop_duplicates** e crie uma lista com uma linha para cada estabelecimento, com os dados do estabelecimento  

# In[175]:


# 1) 
df_menor = df[df["paciente_idade"]<18].copy()


# In[164]:


# 2) 
df_menor.columns


# In[167]:


# 3)
df_menor['vacina_categoria_nome'].value_counts()


# In[182]:


# 4)
# cria uma lista chamada lista_variaveis contendo os nomes de 6 colunas que serão selecionadas do dataframe.
lista_variaveis = ['estabelecimento_valor', 
                   'estabelecimento_razaoSocial', 
                   'estalecimento_noFantasia', 
                   'estabelecimento_municipio_codigo', 
                   'estabelecimento_municipio_nome',
                   'estabelecimento_uf']
#cria um novo dataframe chamado df_menor_lista que contém apenas as colunas especificadas na lista lista_variaveis.
df_menor_lista = df_menor.loc[:,lista_variaveis] 
# método loc para selecionar linhas e colunas do dataframe. ":" indica que todas as linhas serão seleciaionadas
#lista_variaveis, indica que a as colunas (atribuidas à lista_variáveis anteriormemnte) serão selecionadas


# In[184]:


# 5) Aplique o método .drop_duplicates e crie uma lista com uma linha para cada estabelecimento, com os dados do estabelecimento
df_menor_lista = df_menor_lista.drop_duplicates() #drop_duplicates() remove as linhas duplicadas do dataframe
df_menor_lista.shape #df_menor_lista. shape retorna uma tupla com as dimensões do dataframe df_menor_lista (linhas/colunas)


# In[ ]:




