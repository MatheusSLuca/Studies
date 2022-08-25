#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[6]:


# series são um array de rotulos do PD de 1 dimensão, capaz de conter qualquer tipo de dados em Python. Os rotulos são
# chamados de indice(index):
#Exemplo de criação de um Series
#s = pd.Series(data =dados, index = indice)

# "dados" podem ser listas, dicionarios, nd-array e valores escalares em python.
#indices são os nomes dos rotulos para cada linha


# In[5]:


dados = [20, 30, 40, 50]
ClasseSocialSemIndex = pd.Series(data = dados)
ClasseSocialSemIndex


# In[6]:


ClasseSocialSemIndex.index


# In[7]:


indice = ["A","B","C","D"]
dados = [20, 30, 40, 50]
ClasseSocialComIndex = pd.Series(data = dados, index = indice)
ClasseSocialComIndex


# In[8]:


ClasseSocialComIndex.index


# In[9]:


ClasseSocialComIndex["C"]


# In[10]:


ClasseDict = {'Classe_A:':100,
             'Classe_B:':90,
             'Classe_C:':80}
ClasseSeriesDict = pd.Series(ClasseDict)
ClasseSeriesDict


# In[11]:


np.random.randn(5)


# In[12]:


pd.Series(np.random.rand(5))


# In[13]:


pd.DataFrame(dados, columns = ["Par"], index = indice)


# In[14]:


pd.DataFrame({"Par":[2,4,6,8],
            "Impar":[1,3,5,7]}, index = indice)


# In[15]:


pd.DataFrame(ClasseSeriesDict, columns =["Classe"])


# In[16]:


PopBrasilDict = {"amazonas":1000,
                "amapa":2000,
                "sao paulo":3000}

popbrasilserie = pd.Series(PopBrasilDict)
popbrasilserie


# In[17]:


areabrasildict = {"amazonas":1000,
                "amapa":2000,
                "sao paulo":3000}
areabrasilserie = pd.Series(areabrasildict)
areabrasilserie


# In[19]:


final = pd.DataFrame({"População": popbrasilserie,
                     "Area": areabrasilserie})
final


# In[22]:


final["Area"].sum()


# In[27]:


anos_anomalia_dict = {"1900":-0.8,
                "1920": -0.27,
                "1940":0.12,
                "1960":0.03,
                "1980":0.26,
                "2000":0.40,
                "2020":1.02}

anos_anomalia_serie = pd.Series(anos_anomalia_dict)
anos_anomalia_serie


# <table style = "width: 100%; align = center">
# <tr>
# <th>Operação</th>
# <th>Código</th>
# <th>Resultado</th>
# </tr>
# <tr>
# <td>Seleciona uma coluna</td>
# <td>df[col]</td>
# <td>Series</td>
# </tr>
# <tr>
# <td>Seleciona duas colunas</td>
# <td>df[[col1, col2]]</td>
# <td>DataFrame</td>
# </tr>
# <tr>
# <td>Seleciona uma linha usando rotulo</td>
# <td>df.loc["rotulo"]</td>
# <td>Series</td>
# </tr>
# <tr>
# <td>Seleciona uma linha usando inteiro</td>
# <td>df.iloc[i]</td>
# <td>Series</td>
# </tr>
# <tr>
# <td>Recorta um DataFrame da linha i a j</td>
# <td>df[i:j]</td>
# <td>DataFrame</td>
# </tr>
# <tr>
# <td>Recorta um DataFrame usando um vetor booleano</td>
# <td>df[vetor_bool]</td>
# <td>DataFrame</td>
# </tr>

# In[42]:


PopBrasilDict = {"amazonas": 12341231,
                "amapa":1520043,
                "sao paulo":1283819,
                "Minas Gerais":12565476,
                "Rio de Janeiro":1234743,
                "Paraná":41234521,
                "Alagoas":1243132123,
                "Sergipe": 987123,
                "Bahia":8182301}
popbrasilseries = pd.Series(PopBrasilDict)
popbrasilseries


# In[56]:


popbrasildataframe = pd.DataFrame(popbrasilseries, columns=["1900"])
popbrasildataframe


# In[46]:


print(popbrasildataframe["1900"])


# In[57]:


i = 1
indices = []
while i <= 9:
    indices.append(np.random.normal(10000))
    i += 1

popbrasildataframe["1920"] = indices
popbrasildataframe


# In[60]:


vetor_bool = popbrasildataframe["1900"] > 10000000
vetor_bool


# In[63]:


popbrasildataframe[vetor_bool]


# In[64]:


popbrasildataframe.T


# In[67]:


pd.options.display.float_format = '{:.2f}'.format


# In[68]:


popbrasildataframe.T


# In[69]:


popbrasildataframe.values


# In[70]:


popbrasildataframe.values[0]


# In[71]:


popbrasildataframe.values[0][0]


# In[72]:


popbrasildataframe.values[0][1]


# In[76]:


popbrasildataframe.loc[popbrasildataframe['1920'] < 10000, '1920']


# In[ ]:





# In[89]:


df1 = pd.DataFrame(np.random.randint(10, size=(3,5)), columns = ["A","B","C","D","E"])
df1


# In[90]:


df2 = pd.DataFrame(np.random.randint(10, size=(3,5)), columns = ["A","B","C","D","E"])
df2


# In[91]:


df1.iloc[0]


# In[94]:


df1.loc[0] - df1.iloc[0]


# In[95]:


df1


# In[96]:


df1 - df1.iloc[0]


# In[104]:


vacinacao_acre = pd.read_csv('https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIPNI/COVID/uf/uf%3DAC/part-00000-10fee369-3177-449f-b242-f9ddc22c2d47.c000.csv', sep = ';')
vacinacao_acre


# In[105]:


vacinacao_acre.head()


# In[106]:


vacinacao_acre.info()


# In[107]:


vaci_acre_copy = vacinacao_acre[:10000].copy()


# In[108]:


vaci_acre_copy


# In[109]:


vaci_acre_copy.info()


# In[110]:


vaci_acre_copy['fl_capital'] = 0


# In[111]:


vaci_acre_copy.head(1)


# In[121]:


vaci_acre_copy.loc[vaci_acre_copy["paciente_endereco_nmMunicipio"] == "RIO BRANCO", 'fl_capital'] = 1
   

    
vaci_acre_copy.head(10)


# In[126]:


vaci_acre_copy[['paciente_endereco_nmMunicipio','fl_capital']]


# In[128]:


percentual_capital = vaci_acre_copy['fl_capital'].sum()/10000


# In[129]:


percentual_capital


# In[132]:


vaci_acre_copy["paciente_idade"].mean()


# In[ ]:




