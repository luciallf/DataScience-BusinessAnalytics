#!/usr/bin/env python
# coding: utf-8

# In[2]:


# PRUEBA FINAL HERRAMIENTAS DEL CIENTIFICO DE DATOS
"""

El Informe Mundial de la Felicidad es una encuesta histórica sobre el estado de la felicidad global. El primer informe se publicó en 2012, el segundo en 2013,
el tercero en 2015 y el cuarto en la actualización de 2016. El World Happiness 2017, que clasifica a 155 países según sus niveles de felicidad, se lanzó en las Naciones Unidas en un evento que celebra el día internacional de la felicidad el 20 de marzo. El informe continúa ganando reconocimiento mundial a medida que los gobiernos, las organizaciones y la sociedad civil utilizan cada vez más los indicadores de felicidad para informar de sus decisiones de formulación de políticas. Los principales expertos en todos los campos (economía, psicología, análisis de encuestas, estadísticas nacionales, salud, políticas públicas y más)
describen cómo las mediciones de bienestar se pueden usar de manera efectiva para evaluar el progreso de las naciones.
Sobre los informes de felicidad de 2015 y 2016, realizar las siguientes exploraciones:

Cargar los dos CSV como datasets.
Identificra las columnas de ambos datasets: ¿hay diferencias entre ambos?
Une ambos dataframes, sin importar que los dos compartan las mismas diferencias.
Revisa el número de nulos que hay por cada columna, así como su porcentaje.
Cambia los valores nulos de las columnas "Lower Confidence Interval" y "Upper Confidence Interval" por un número aleatorio entre el valor mínimo y máximo de la misma columna (un único número, no es necesario uno diferente para cada fila con valor nulo).
Cambia los valores nulos de la columna "Standard Error" por su media al cuadrado.
Obtén un resumen estadístico del dataframe sin valores nulos.
Muestra de forma gráfica la relación entre la familia y la salud.
Muestra de forma gráfica la relación entre la puntuación de felicidad y la confianza (corrupción del gobierno).
Muestra la matriz de correlación del daframe.
Tras unir los dataframes, los países aparecerán más de una vez. Muestra agrupado el dataframe por país con el valor máximo de felicidad, sin importar el año.
¿Tiene relación la felicidad con la generosidad? Muéstralo gráficamente a través de la puntuación de libertad.
Muestra la distribución del grado de distopía en función de la región.

"""

## Ejercicio 1 - Python
### Se pide: 


# In[3]:


# Cargar los dos CSV como datasets


# In[59]:


import pandas as pd
import numpy as np
import seaborn as sns
from plotnine import *
from matplotlib import pyplot as plt


# In[5]:


datos_2015 = pd.read_csv('2015.csv')
datos_2016 = pd.read_csv('2016.csv')


# In[6]:


#Identificar las columnas de ambos datasets: ¿hay diferencias entre ambos?


# In[7]:


datos_2015.columns


# In[8]:


datos_2016.columns


# In[9]:


""" 
Sí hay diferencia entre las columnas de ambos datasets, ya que ambos tienen muchas columnas del mismo nombre pero sin embargo hay otras que cambian por ejemplo 'Lower Confidence Interval', que se encuentra en el dataset del 2016.
"""


# In[10]:


#Une ambos dataframes, sin importar que los dos compartan las mismas diferencias.


# In[11]:


df = pd.concat([datos_2015, datos_2016], ignore_index=True, join="outer")


# In[12]:


df


# In[13]:


#Revisa el número de nulos que hay por cada columna, así como su porcentaje.


# In[14]:


df.isnull().sum().sum()


# In[15]:


def show_nulls(df):
    #Nulos totales
    total_nan = df = df.isnull().sum()
    #Porcentaje de nulos
    perc_nan = total_nan/len(df)*100
    
    return total_nan, perc_nan


# In[16]:


print('Total nulos', show_nulls(df=df)[0])


# In[17]:


print('Porcentaje de nulos', show_nulls(df=df)[1])


# In[19]:


# Cambia los valores nulos de las columnas "Lower Confidence Interval" y "Upper Confidence Interval" por un número aleatorio entre el valor mínimo y máximo de la misma columna (un único número, no es necesario uno diferente para cada fila con valor nulo).


# In[37]:


df.min()


# In[23]:


df.max()


# In[38]:


use_min , use_max = int(df['Lower Confidence Interval'].min()) , int(df['Lower Confidence Interval'].max())
import random

df['Lower Confidence Interval'].fillna(random.randint(use_min,use_max))


# In[39]:


aleatorio_lower=df['Lower Confidence Interval'].fillna(random.randint(use_min,use_max))


# In[40]:


use_min , use_max = int(df['Upper Confidence Interval'].min()) , int(df['Upper Confidence Interval'].max())


# In[41]:


df['Upper Confidence Interval'].fillna(random.randint(use_min,use_max))


# In[42]:


aleatorio_Upper=df['Upper Confidence Interval'].fillna(random.randint(use_min,use_max))


# In[43]:


aleatorio_Upper=df['Upper Confidence Interval'].fillna(random.randint(use_min,use_max))


# In[44]:


df


# In[45]:


# Cambia los valores nulos de la columna "Standard Error" por su media al cuadrado.


# In[46]:


df_Valores_nulos = df["Standard Error"]


# In[47]:


media_al_cuadrado = df_Valores_nulos.mean()**2


# In[48]:


media_al_cuadrado


# In[49]:


df = df.fillna(media_al_cuadrado)


# In[53]:


df


# In[52]:


# Obtén un resumen estadístico del dataframe sin valores nulos.


# In[54]:


df.describe()


# In[55]:


#Comprobamos que no hay nulos


# In[56]:


df.isnull().sum()


# In[57]:


# Muestra de forma gráfica la relación entre la familia y la salud.


# In[65]:


(ggplot(df)
+aes(y="Health (Life Expectancy)", x = "Family")
+geom_point(color="green", alpha=0.3 )
+geom_smooth(aes(y="Health (Life Expectancy)", x="Family"), color="red")
+ggtitle('Relación entre la familia y la salud')
+ylab('Salud')
+xlab('Familia')
)


# In[67]:


"""
En esta nube de puntos podemos observar que cuanto más aumenta la familia, más aumenta la salud 
"""


# In[68]:


# Muestra de forma gráfica la relación entre la puntuación de felicidad y la confianza (corrupción del gobierno).


# In[74]:


(ggplot(df)
+aes(y="Trust (Government Corruption)", x = "Happiness Score")
+geom_point(color="Orange", alpha=0.4 )
+geom_smooth(aes(y="Trust (Government Corruption)", x="Happiness Score"), color="red")
+ggtitle('Relación entre la felicidad y la confianza en corrupción del gobierno')
+ylab('Confianza')
+xlab('Felicidad')
)


# In[75]:


"""
Podemos observar que no hay una fuerte relación entre ambas variables a excepción de la pequeña relación que hay en los valores mayores de Felicidad y de Confianza 
"""


# In[76]:


#Muestra la matriz de correlación del daframe.


# In[77]:


df.corr()


# In[78]:


#Tras unir los dataframes, los países aparecerán más de una vez. Muestra agrupado el dataframe por país con el valor máximo de felicidad, sin importar el año.


# In[79]:


df.groupby("Country").max("Hapiness Score")


# In[80]:


#¿Tiene relación la felicidad con la generosidad? Muéstralo gráficamente a través de la puntuación de libertad.


# In[86]:


(ggplot(df) 
+geom_point(aes(x='Happiness Score', y = 'Generosity', color = 'Freedom'))  
+geom_smooth(aes(y="Generosity", x="Happiness Score"),color="red")
+ggtitle('Relación entre la felicidad y la generosidad') 
+xlab('Felicidad')
+ylab('Generosidad')
)


# In[87]:


# Muestra la distribución del grado de distopía en función de la región.


# In[103]:


(ggplot(df)
+aes(x='Dystopia Residual', fill='Region')
+geom_histogram(color = 'blue', alpha=0.8)
+ggtitle('Grado de Distopía en función de la Región')
+ylab('')
+xlab('Distopía')
)


# In[ ]:


#En la gráfica se puede ver que en los valores centrales de distopía es donde se centran la mayoría de las regiones.

