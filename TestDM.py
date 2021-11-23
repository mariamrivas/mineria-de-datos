#!/usr/bin/env python
# coding: utf-8

# LIBRERÍA PANDAS: 
# Pandas es una librería de Python que es utilizada para manejar y analizar las estructuras de los datos. Además con esta libreria se puede leer y escribir archivos en formato CSV, Excel y bases de datos SQL. Para tener un acceso de los datos se lo realiza con índices tanto para las filas como las columnas.

# In[10]:


#importación de la libreria 
import pandas as pd 


# In[14]:


#Leer el archivo csv
df = pd.read_csv('https://query.data.world/s/d5ko4ixgkjvj5xbxdlemp2fjqquof4')
df.head()


# In[15]:


#Realización de un DataFrame con los datos del archivo
mascotas = pd.read_csv('https://query.data.world/s/d5ko4ixgkjvj5xbxdlemp2fjqquof4', index_col=0)
print(mascotas)


# In[16]:


#Mostrar en pantalla las dimensiones y el número de datos que tiene el archivo 
print('Dimensiones:', mascotas.shape)
print('Número de elementos:', mascotas.size)


# In[19]:


#Mostrar en pantalla las filas pares del DataFrame
print(mascotas.iloc[range(0,mascotas.shape[0],2)])


# 

# LIBRERÍA NUMPY:
# Numpy es usada para el cálculo numérico y para analizar datos, especialmente para un volumen de datos grande. 
# Tiene estructuras de datos muy potentes. Numpy puede inplementar matrices y matrices multidimensionales.
# 

# In[27]:


#leer la primera linea del archivo csv
import numpy as np
archivo = open('austin-animal-center-outcomes-1.csv','r')
archivo.readline()
                  


# In[77]:


#Averiguar el número de lineas que tiene el archivo csv
import numpy as np
with open("./austin-animal-center-outcomes-1.csv") as f:

    n = len(list(f))
print("número de lineas =", n)


# In[78]:


#Conocer el número de columnas que tiene el archivo csv
import numpy as np
with open("austin-animal-center-outcomes-1.csv") as f:
    
    ncols = len(f.readline().split(','))
    
print ("número de columnas=", ncols)


# 
# 

# LIBRERÍA MATPLOTLIB:
# Matplotlib es una librería que ayuda a realizar gráficos desde datos de lista. Esta librería produce figuras o gráficos
# de una buena calidad que pueden ser públicados en una variedad de formatos impresos y plataformas. Aquí se pueden realizar
# histogramas, espectros de potencia. gráficos de barras, pasteles, etc.

# In[18]:


#Gráficar lineas verticales con los primeros 10 datos de la columnas AnimalID y Name.
import pandas as pd
import matplotlib.pyplot as plot

datos = pd.read_csv('austin-animal-center-outcomes-1.csv').iloc[0:10, 0:2]

for p in datos:

    plot.axvline(p,  label='Columnas del Dataset')

plot.legend()

plot.show()


# In[16]:


#Gráfico de barras para poder visualizar la cantidad de los tipos de animales (Animal Type)
import pandas as pd
import matplotlib.pyplot as plot
d = pd.read_csv('https://query.data.world/s/d5ko4ixgkjvj5xbxdlemp2fjqquof4', index_col=0)
d['Animal Type'].value_counts().plot(kind='bar', title='Cantidades de animales según el tipo')


# In[8]:


#Visualizar en un diagrama de pastel el porcentaje de los animales según su tipo de resultado (Outcome Type)
import pandas as pd
import matplotlib.pyplot as plot
d = pd.read_csv('https://query.data.world/s/d5ko4ixgkjvj5xbxdlemp2fjqquof4', index_col=0)
d['Outcome Type'].value_counts().plot(kind='pie', autopct='%.2f%%', title='Porcentaje de los animales según su tipo de resultado  ')


# LIBRERÍA SEABORN:
# Seaborn es una librería para poder visualizar los datos para Python. Esta librería trabaja con un paquete muy avanzado para que así se pueda crear dibujos más convenientes y de forma rápida. Es fácil de utilizar y hasta una persona sin experiencia puede realizar un gráfico sencillo con un código minímo.

# In[1]:


#Visualizar en un gráfico de barras la cantidad de los diferentes tipos de animales (Animal Type)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('https://query.data.world/s/d5ko4ixgkjvj5xbxdlemp2fjqquof4')
data = df['Animal Type']
sns.displot(data)
plt.show()


# In[5]:


# Trazo de un diagrama KDE (Densidad de Kernel)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('https://query.data.world/s/d5ko4ixgkjvj5xbxdlemp2fjqquof4')
data = df['Animal Type']
sns.displot(data, discrete = True, kde = True)
plt.show()


# In[6]:


#Visualizar la parcela de distribución conjunta entre la columna Name y la Animal Type
#Visualizar la distribución entre el Name y el Animal Type
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('https://query.data.world/s/d5ko4ixgkjvj5xbxdlemp2fjqquof4')
df.dropna(inplace=True)
sns.jointplot(x = "Name", y = "Animal Type", data = df)
plt.show()


# In[ ]:





# In[ ]:




