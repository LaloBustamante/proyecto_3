#!/usr/bin/env python
# coding: utf-8

# # Hola Eduardo! <a class="tocSkip"></a>
# 
# Mi nombre es Oscar Flores y tengo el gusto de revisar tu proyecto. Si tienes algún comentario que quieras agregar en tus respuestas te puedes referir a mi como Oscar, no hay problema que me trates de tú.
# 
# Si veo un error en la primera revisión solamente lo señalaré y dejaré que tú encuentres de qué se trata y cómo arreglarlo. Debo prepararte para que te desempeñes como especialista en Data, en un trabajo real, el responsable a cargo tuyo hará lo mismo. Si aún tienes dificultades para resolver esta tarea, te daré indicaciones más precisas en una siguiente iteración.
# 
# Te dejaré mis comentarios más abajo - **por favor, no los muevas, modifiques o borres**
# 
# Comenzaré mis comentarios con un resumen de los puntos que están bien, aquellos que debes corregir y aquellos que puedes mejorar. Luego deberás revisar todo el notebook para leer mis comentarios, los cuales estarán en rectángulos de color verde, amarillo o rojo como siguen:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
#     
# Muy bien! Toda la respuesta fue lograda satisfactoriamente.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Existen detalles a mejorar. Existen recomendaciones.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Se necesitan correcciones en el bloque. El trabajo no puede ser aceptado con comentarios en rojo sin solucionar.
# </div>
# 
# Cualquier comentario que quieras agregar entre iteraciones de revisión lo puedes hacer de la siguiente manera:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# </div>
# 

# ## Resumen de la revisión 1 <a class="tocSkip"></a>

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Buen trabajo! Tu notebook está muy bien logrado, te felicito especialmente por el orden y claridad de los gráficos. Hay un par de errores a corregir relativos a los días mostrados, nota que 0 es el domingo y luego aumentan hasta que el sábado es 6, por lo tanto, debes corregir los resultados que utilizan el día de la semana. Fuera de eso, el resto está correcto, corrige lo indicado y lo revisaré.
#     
# Saludos!    
# </div>

# ## Resumen de la revisión 2 <a class="tocSkip"></a>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien! Has corregido todo lo necesario para aprobar el proyecto, no tengo más comentarios.
#     
# Saludos!    
# </div>

# ----

# # ¡Llena ese carrito!

# # Introducción
# 
# Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.
# El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados. Tuvimos cuidado de conservar las distribuciones de los datos originales cuando hicimos los cambios.
# 
# Debes completar tres pasos. Para cada uno de ellos, escribe una breve introducción que refleje con claridad cómo pretendes resolver cada paso, y escribe párrafos explicatorios que justifiquen tus decisiones al tiempo que avanzas en tu solución.  También escribe una conclusión que resuma tus hallazgos y elecciones.
# 

# ## Diccionario de datos
# 
# Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.
# 
# - `instacart_orders.csv`: cada fila corresponde a un pedido en la aplicación Instacart.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'user_id'`: número de ID que identifica de manera única la cuenta de cada cliente.
#     - `'order_number'`: el número de veces que este cliente ha hecho un pedido.
#     - `'order_dow'`: día de la semana en que se hizo el pedido (0 si es domingo).
#     - `'order_hour_of_day'`: hora del día en que se hizo el pedido.
#     - `'days_since_prior_order'`: número de días transcurridos desde que este cliente hizo su pedido anterior.
# - `products.csv`: cada fila corresponde a un producto único que pueden comprar los clientes.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'product_name'`: nombre del producto.
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
# - `order_products.csv`: cada fila corresponde a un artículo pedido en un pedido.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'add_to_cart_order'`: el orden secuencial en el que se añadió cada artículo en el carrito.
#     - `'reordered'`: 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.
# - `aisles.csv`
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'aisle'`: nombre del pasillo.
# - `departments.csv`
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
#     - `'department'`: nombre del departamento.

# # Paso 1. Descripción de los datos
# 
# Lee los archivos de datos (`/datasets/instacart_orders.csv`, `/datasets/products.csv`, `/datasets/aisles.csv`, `/datasets/departments.csv` y `/datasets/order_products.csv`) con `pd.read_csv()` usando los parámetros adecuados para leer los datos correctamente. Verifica la información para cada DataFrame creado.
# 

# ## Plan de solución
# 
# Escribe aquí tu plan de solución para el Paso 1. Descripción de los datos.
# 
# El primer paso es leer cada archivo de datos utilizando la función pd.read_csv(), luego se debe desplegar cada DataFrame creado para verificar la información.
# 
# El conjunto de datos instacart_orders.csv contiene información de los pedidos realizados en la aplicación Instacart. Se explorarán las columnas 'order_dow' y 'order_hour_of_day' para entender los patrones de pedidos a lo largo de los días de la semana y las horas del día. Se debe verificar si hay valores nulos en 'days_since_prior_order'.
# 
# El archivo products.csv contiene información correspondiente a un producto unico que pueden comporar los clientes, se explorará la columna 'aisle_id' y 'department_id' para comprender la categorización de los productos en pasillos y departamentos. También se debe verificar la existencia de duplicados en 'product_id' y 'product_name'.
# 
# Los archivos aisles.csv y departments.csv son conjuntos de datos que proporcionan información adicional sobre las categorías de pasillos y departamentos. No se esperan cambios significativos, pero se verificará si existen datos duplicados.
# 
# El conjunto order_products.csv contiene información sobre los productos incluidos en cada pedido. Se explorará la columna 'reordered' para comprender la proporción de productos que se vuelven a pedir.

# In[50]:


# importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[51]:


# leer conjuntos de datos en los DataFrames
orders_df = pd.read_csv('/datasets/instacart_orders.csv',  sep=';')
products_df = pd.read_csv('/datasets/products.csv',  sep=';')
aisles_df = pd.read_csv('/datasets/aisles.csv',  sep=';')
departments_df = pd.read_csv('/datasets/departments.csv',  sep=';')
order_products_df = pd.read_csv('/datasets/order_products.csv',  sep=';')


# In[52]:


# Mostrar información del DF instacart_orders
print("Información de orders_df:")
print(orders_df.info())


# In[53]:


# Mostrar información del DF products
print("\nInformación de products_df:")
print(products_df.info())


# In[54]:


# Mostrar información del DF aisles
print("\nInformación de aisles_df:")
print(aisles_df.info())


# In[55]:


# Mostrar información del DF departments
print("\nInformación de departments_df:")
print(departments_df.info())


# In[56]:


# Mostrar información del DF order products
print("\nInformación de order_products_df:")
print(order_products_df.info())


# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 1. Descripción de los datos.
# 
# Al realizar este paso podemos notar que el proposito es tener una comprensión inicial de los datos y prepararse para realizar análisis exploratorios más detallados posteriormente. Se han leido con exito los conjuntos de datos proporcionados y con ayuda del metodo info() hemos verificado su información básica. Con dichos procedimientos podemos avanzar en el análisis exploratorio de datos y abordar los proximos pasos del proyecto.
# 

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcta la carga y revisión inicial de datos
# </div>

# # Paso 2. Preprocesamiento de los datos
# 
# Preprocesa los datos de la siguiente manera:
# 
# - Verifica y corrige los tipos de datos (por ejemplo, asegúrate de que las columnas de ID sean números enteros).
# - Identifica y completa los valores ausentes.
# - Identifica y elimina los valores duplicados.
# 
# Asegúrate de explicar qué tipos de valores ausentes y duplicados encontraste, cómo los completaste o eliminaste y por qué usaste esos métodos. ¿Por qué crees que estos valores ausentes y duplicados pueden haber estado presentes en el conjunto de datos?

# ## Plan de solución
# 
# Escribe aquí tu plan para el Paso 2. Preprocesamiento de los datos.
# 
# 1.-Verifica y corrige los tipos de datos: 
# Utilizar pd.to_numeric() para convertir las columnas de ID a números enteros
# 
# 2.-Identifica y completa valores ausentes:
# 
# En products_df: 
# Identificar valores ausentes en 'product_name'
# Completar los nombres de productos ausentes con 'Unknown'
# 
# En orders_df:
# Identificar valores ausentes en 'days_since_prior_order'
# Completar los valores ausentes con una estrategia, como el valor medio
# 
# En order_products_df:
# Identificar valores ausentes en 'add_to_cart_order'
# Revisar si hay algún patrón en los valores ausentes y completar de manera lógica
# 
# 3.-Identifica y elimina valores duplicados:
# 
# En orders_df:
# Revisar duplicados y eliminarlos si existen
# 
# En products_df:
# Revisar duplicados en 'product_id' y 'product_name'
# Eliminar duplicados en 'product_name'
# 
# En departments_df y aisles_df:
# Revisar duplicados y eliminarlos
# 
# En order_products_df:
# Revisar duplicados y eliminarlos
# 
# 4.-Explicaciones:
# 
# Valores Ausentes:
# Pueden deberse a errores en la entrada de datos, información faltante en la fuente original o cambios realizados en la estructura de la base de datos con el tiempo. Se elige completar valores ausentes de manera lógica o asignar un valor 'Unknown'
# 
# Valores Duplicados:
# Pueden ocurrir por errores en la carga de datos, actualizaciones incorrectas o problemas de consolidación. Eliminar duplicados se basa en la lógica de conservar la integridad de los datos y evitar redundancias
# 
# 5.-Conclusiones Provisionales:
# El preprocesamiento garantizará la coherencia y calidad de los datos, preparándolos para análisis futuros. Cada acción se toma con el objetivo de mantener la integridad de la información y facilitar su uso en tareas analíticas y de modelado.

# ## Encuentra y elimina los valores duplicados (y describe cómo tomaste tus decisiones).

# ### `orders` data frame

# In[57]:


# Revisa si hay pedidos duplicados
duplicates = orders_df[orders_df.duplicated(subset=['order_id'], keep=False)]
print("Duplicados en orders_df:\n")
print(duplicates.sum())
print("\n Registros duplicados en 'orders_df':")
print(duplicates)


# ¿Tienes líneas duplicadas? Si sí, ¿qué tienen en común?
# 
# Sí, hay líneas duplicadas en el DataFrame "orders_df". Para identificar las líneas duplicadas, se ha utilizado la columna 'order_id' como criterio de duplicación. Las filas duplicadas tienen el mismo valor en la columna 'order_id'. Por ejemplo, se observa en la salida, que las filas con los índices 30371 y 230807 tienen el mismo 'order_id' (1918001), lo que indica una duplicación.
# Las filas duplicadas comparten valores en varias columnas, como 'user_id', 'order_number', 'order_dow', 'order_hour_of_day', y 'days_since_prior_order'. Sin embargo, algunas de las filas tienen valores distintos en la columna 'days_since_prior_order',  las líneas duplicadas comparten el mismo 'order_id', pero pueden tener diferencias en otras columnas, especialmente en 'days_since_prior_order'.

# In[58]:


# Basándote en tus hallazgos,
# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.
wednesday_2am = orders_df[(orders_df['order_dow'] == 3) & (orders_df['order_hour_of_day'] == 2)]
print("Pedidos realizados el miércoles a las 2:00 a.m.:\n\n", wednesday_2am)


# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Nota que debes ver las ordenes del miércoles, es decir, día 3 (el domingo es 0, lunes 1 y así)
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
#     Ya he realizaod la corrección indicada.
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien, corregido!
# </div>

# ¿Qué sugiere este resultado?
# 
# El resultado indica que hay 136 pedidos que se realizaron el miércoles a las 2:00 a.m. Esta información puede sugerir patrones de comportamiento de los clientes, ya que parece haber una cantidad significativa de pedidos realizados en este horario específico. Se plantea la posibilidad de investigar más a fondo para comprender por qué los clientes eligen realizar pedidos en ese horario, y si existe algún patrón común entre los productos comprados en estos pedidos.

# In[59]:


# Elimina los pedidos duplicados
orders_df.drop_duplicates(subset='order_id', keep='first', inplace=True)


# In[60]:


# Vuelve a verificar si hay filas duplicadas
duplicates_after_removal = orders_df[orders_df.duplicated(subset=['order_id'], keep=False)]


# In[61]:


# Vuelve a verificar únicamente si hay IDs duplicados de pedidos
duplicates_ids_after_removal = orders_df[orders_df.duplicated(subset=['order_id'], keep='first')]
print("Número de pedidos duplicados después de la eliminación:", len(duplicates_after_removal))
print("\nRegistros duplicados en 'orders_df' después de la eliminación:")
print(duplicates_after_removal)


# Describe brevemente tus hallazgos y lo que hiciste con ellos
# 
# Después de eliminar los duplicaods, se verificó nuevamente la presencia de registros duplicadas y se encontró que no quedaban registros duplicados en el df. Además, se verificó únicamente si había IDs duplicados de pedidos, se confirmó que no había IDs duplicados después de la eliminación. Se tomaron medidas para eliminar los pedidos duplicados en el conjunto de datos, y los hallazgos indican que esta operación se realizó con éxito, dejando el df sin registros duplicados.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto, se eliminaron los duplicados
# </div>

# ### `products` data frame

# In[62]:


# Verifica si hay filas totalmente duplicadas
total_duplicates = products_df[products_df.duplicated(keep=False)]
print("Total de filas duplicadas en products_df:", len(total_duplicates))
print("\nFilas duplicadas en 'products_df':")
print(total_duplicates)


# In[63]:


# Verifica únicamente si hay IDs duplicadas de productos
product_id_duplicates = products_df.duplicated(subset=['product_id'], keep=False)
print("Total de ids duplicados de productos en products_df:", product_id_duplicates.sum())
print("\nids duplicados de productos en 'products_df':")
print(products_df[product_id_duplicates]['product_id'])


# In[64]:


# Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
products_df['product_name_upper'] = products_df['product_name'].str.upper()
print(products_df['product_name_upper'])


# In[65]:


# Revisa si hay nombres duplicados de productos no faltantes
product_name_duplicates = products_df.duplicated(subset=['product_name_upper'], keep=False)
print("Total de nombres duplicados de productos en products_df:", product_name_duplicates.sum())
print("\nNombres duplicados de productos en 'products_df':")
print(products_df[product_name_duplicates]['product_name_upper'])


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# El código calcula el total de nombres duplicados de productos, identificando duplicados basándose en los nombres convertidos a letras mayúsculas. Después se imprime el total de nombres duplicados. El código imprime los nombres duplicados de productos en el dataframe products_df. Los nombres duplicados se imprimen en mayúsculas, facilitando reconocer los duplicados sin importar el formato de las letras. 
# Se creó una columna adicional 'product_name_upper' para almacenar los nombres de productos en mayúsculas. Esto facilita la comparación y detección de duplicados, asegurándose de que las comparaciones sean insensibles a mayúsculas y minúsculas.
# Los resultaods proporcionan una visión clara de los nombres duplicados de productos en el conjunto de datos, permitiendo tomar decisiones informadas sobre cómo manejar estos duplicados durante el proceso de preprocesamiento de datos.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Muy bien, inicalmente no hay duplicados pero al convertirlos a mayúsculas al menos hay duplicados de nombre. Sin embargo, observa que hay algunos sin nombre y si observas el id de estos no son duplicados completamente, por lo que no es necesario eliminarlos.
# </div>

# ### `departments` data frame

# In[66]:


# Revisa si hay filas totalmente duplicadas
departments_duplicates = departments_df[departments_df.duplicated(keep=False)]

print("Filas totalmente duplicadas en departments_df:")
print(departments_duplicates)


# In[67]:


# Revisa únicamente si hay IDs duplicadas de productos
department_id_duplicates = departments_df.duplicated(subset=['department_id'], keep=False)
print("ids duplicadas de departamento en departments_df:")
print(departments_df[department_id_duplicates]['department_id'])


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Después de revisar el DataFrame department.csv en busca de filas totalmente duplicadas, no se encontró ninguna fila completamente duplicada. Por lo que no fue necesario realizar ninguna acción adicional para manejar duplicados en este caso, ya que no se encontraron duplicados totales en el conjunto de datos.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ### `aisles` data frame

# In[68]:


# Revisa si hay filas totalmente duplicadas
aisles_duplicates = aisles_df[aisles_df.duplicated(keep=False)]
print("Total de filas totalmente duplicadas en aisles_df:", len(aisles_duplicates))
print("\nFilas totalmente duplicadas en 'aisles_df':")
print(aisles_duplicates)


# In[69]:


# Revisa únicamente si hay IDs duplicadas de productos
aisles_id_duplicates = aisles_df.duplicated(subset=['aisle_id'], keep=False)
print("Total de IDs duplicados en aisles_df:", aisles_id_duplicates.sum())
print("\nIDs duplicados en 'aisles_df':")
print(aisles_df[aisles_id_duplicates]['aisle_id'])


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Después de revisar el dataframe aisles_df en busca de filas totalmente duplicadas y IDs duplicados en la columna aisle_id, los hallazgos fueron:
# No se encontraron filas totalmente duplicadas en el DataFrame aisles_df. Lo que indica que cada fila es única en términos de todas sus columnas. Tampoco se encontraron ids duplicados en la columna aisle_id. 

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ### `order_products` data frame

# In[70]:


# Revisa si hay filas totalmente duplicadas
order_products_duplicates = order_products_df[order_products_df.duplicated(keep=False)]
print("Total de filas totalmente duplicadas en order_products_df:", len(order_products_duplicates))
print("\nFilas totalmente duplicadas en 'order_products_df':")
print(order_products_duplicates)


# In[71]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso
for column in order_products_df.columns:
    duplicates = order_products_df[order_products_df.duplicated(subset=[column], keep=False)]
    print(f"Total de duplicados en la columna '{column}' de order_products_df: {len(duplicates)}")
    if len(duplicates) > 0:
        print(f"Duplicados en la columna '{column}':")
        print(duplicates)
    print("\n" + "="*50 + "\n")


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Basándome en los resultados, parece que no se encontraron filas totalmente duplicadas en el dataframe order_products_df. Se observa que hay duplicados en las columnas 'order_id', 'product_id', 'add_to_cart_order' y 'reordered' del dataframe.
# 
# En la columna 'order_id': Se encontraron 4,523,160 duplicados.
# En la columna 'product_id': Se encontraron 4,539,960 duplicados.
# En la columna 'add_to_cart_order': Se encontraron 4,545,007 duplicados.
# En la columna 'reordered': Se encontraron 4,545,007 duplicados. 
# 
# Estos hallazgos sugieren que hay varios registros duplicados en el dataframe order_products_df, y es necesario abordarlos para mantener la integridad de los datos.

# ## Encuentra y elimina los valores ausentes
# 
# Al trabajar con valores duplicados, pudimos observar que también nos falta investigar valores ausentes:
# 
# * La columna `'product_name'` de la tabla products.
# * La columna `'days_since_prior_order'` de la tabla orders.
# * La columna `'add_to_cart_order'` de la tabla order_productos.

# ### `products` data frame

# In[72]:


# Encuentra los valores ausentes en la columna 'product_name'
missing_product_names = products_df['product_name'].isnull().sum()
print("Valores ausentes en 'product_name':", missing_product_names)


# Describe brevemente cuáles son tus hallazgos.
# El resultado indica que hay 1,258 valores ausentes en la columna 'product_name' del DataFrame products_df. Estos valores ausentes pueden deberse a diversas razones, como datos faltantes en la fuente original, errores durante la recopilación de datos, o simplemente que la información no estaba disponible en ese momento.

# In[73]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?
missing_product_names = products_df[products_df['product_name'].isnull()]
are_all_missing_related_to_aisle_100 = missing_product_names['aisle_id'].eq(100).all()
print("¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?:", are_all_missing_related_to_aisle_100)


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# Describe brevemente cuáles son tus hallazgos.
# 
# El resultado indica que todos los nombres de productos ausentes en la columna 'product_name' están asociados al pasillo con ID 100. Es decir, no hay nombres de productos ausentes que pertenezcan a pasillos distintos del pasillo con ID 100.

# In[74]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?
missing_product_names = products_df['product_name'].isnull()
related_to_aisle_100 = products_df.loc[missing_product_names, 'aisle_id'] == 100
related_to_department_21 = products_df.loc[missing_product_names & related_to_aisle_100, 'department_id'] == 21
print("¿Todos los nombres de productos ausentes relacionados con el pasillo 100 están también relacionados con el departamento 21?:", related_to_department_21.all())


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# Describe brevemente cuáles son tus hallazgos.
# 
# El resultado indica que todos los nombres de productos ausentes, que están relacionados con el pasillo con ID 100, también están relacionados con el departamento con ID 21. En otras palabras, parece que los productos ausentes y asociados al pasillo 100 pertenecen exclusivamente al departamento 21.

# In[75]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.
aisle_100_info = aisles_df[aisles_df['aisle_id'] == 100]
print("Información del pasillo con ID 100:")
print(aisle_100_info)
department_21_info = departments_df[departments_df['department_id'] == 21]
print("\nInformación del departamento con ID 21:")
print(department_21_info)


# Describe brevemente cuáles son tus hallazgos.
# 
# El pasillo con ID 100 tiene la etiqueta "missing" en la columna 'aisle'. Lo que sugiere que este pasillo está relacionado con productos que tienen información faltante o ausente en cuanto a su categoría de pasillo.
# El departamento con ID 21 también tiene la etiqueta "missing" en la columna 'department'. Esto indica que este departamento también está relacionado con productos que tienen información faltante o ausente en cuanto a su categoría de departamento.
# Los productos con nombres ausentes están asociados tanto al pasillo con ID 100 como al departamento con ID 21, ambos identificados como "missing". Esto sugiere que los productos con información faltante pueden pertenecer a categorías no especificadas o no clasificadas.

# In[76]:


# Completa los nombres de productos ausentes con 'Unknown'
products_df['product_name'].fillna('Unknown', inplace=True)
print(products_df)


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Se han llenado los valores nulos en la columna 'product_name' con 'Unknown', el dataframe ahora no tiene valores nulos en la columna 'product_name'. Esta acción es útil para asegurarnos de que no haya datos faltantes en esa columna específica.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Ok, muy bien!
# </div>

# ### `orders` data frame

# In[77]:


# Encuentra los valores ausentes
missing_values = orders_df.isnull().sum()
missing_values = missing_values[missing_values > 0]
print("Valores ausentes en 'orders_df':")
print(missing_values)


# In[78]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?
non_first_order_missing = orders_df[(orders_df['days_since_prior_order'].isnull()) & (orders_df['order_number'] != 1)]
print("\nCasos donde el valor ausente no es el primer pedido del cliente:")
print(non_first_order_missing)


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Los resultados indican que la única columna con valores ausentes en el DataFrame orders_df es la columna 'days_since_prior_order', y hay 28,817 valores ausentes en esta columna. Los valores ausentes en esta columna podría indicar que estos son los primeros pedidos de los clientes, ya que la columna representa el número de días transcurridos desde el pedido anterior.
# Al analizar los casos donde 'days_since_prior_order' es nulo, se encuentra que estos corresponden al primer pedido del cliente. Esto tiene sentido, ya que para el primer pedido de un cliente no hay un pedido anterior del cual calcular la diferencia en días.
# Por lo tanto, la acción tomada en este caso es entender que los valores ausentes en 'days_since_prior_order' indican el primer pedido de cada cliente. No es necesario imputar estos valores ausentes, ya que esta situación es una característica natural del conjunto de datos, y tiene sentido que no haya un "días desde el pedido anterior" para el primer pedido.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Exacto, no debemos preocuparnos por estos nulos
# </div>

# ### `order_products` data frame

# In[79]:


# Encuentra los valores ausentes
missing_values = order_products_df['add_to_cart_order'].isnull().sum()
print(f"Valores ausentes en 'add_to_cart_order': {missing_values}")


# In[80]:


# ¿Cuáles son los valores mínimos y máximos en esta columna?
min_value = order_products_df['add_to_cart_order'].min()
max_value = order_products_df['add_to_cart_order'].max()
print(f"Valor mínimo en 'add_to_cart_order': {min_value}")
print(f"Valor máximo en 'add_to_cart_order': {max_value}")


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# Describe brevemente cuáles son tus hallazgos.
# 
# Según los resultados del código, se observa que hay 836 valores ausentes en la columna 'add_to_cart_order' del datfFrame order_products_df. Además, se determina que el valor mínimo en esta columna es 1.0, lo que indica que algunos productos fueron añadidos como primeros en el carrito, mientras que el valor máximo es 64.0, indicando que algunos productos fueron añadidos en una posición más avanzada en el carrito, con un rango que va desde 1 hasta 64. Esto sugiere que la mayoría de los productos tienen un orden de agregación al carrito razonable, pero es posible que se hayan producido algunos errores o valores faltantes en la información del orden de algunos productos en el carrito.

# In[81]:


# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'
missing_order_ids = order_products_df[order_products_df['add_to_cart_order'].isnull()]['order_id'].unique()
print("IDs de pedidos con 'add_to_cart_order' ausente:", missing_order_ids)


# In[82]:


# ¿Todos los pedidos con valores ausentes tienen más de 64 productos?
all_missing_orders_have_64_products = all(order_products_df[order_products_df['order_id'].isin(missing_order_ids)]['add_to_cart_order'] > 64)
print("¿Todos los pedidos con valores ausentes tienen más de 64 productos?:", all_missing_orders_have_64_products)
# Agrupa todos los pedidos con datos ausentes por su ID de pedido.
missing_orders_grouped = order_products_df[order_products_df['order_id'].isin(missing_order_ids)].groupby('order_id')['product_id'].count().reset_index()
print("Agrupación de pedidos con datos ausentes por ID de pedido:")
print(missing_orders_grouped)
# Cuenta el número de 'product_id' en cada pedido y revisa el valor mínimo del conteo.
min_product_count = missing_orders_grouped['product_id'].min()
print("Valor mínimo del conteo de 'product_id' en pedidos con datos ausentes:", min_product_count)


# Describe brevemente cuáles son tus hallazgos.
# 
# Los resultados indican que hay 70 pedidos con datos ausentes en la columna 'add_to_cart_order'. No todos estos pedidos tienen más de 64 productos, ya que la respuesta a la pregunta "¿Todos los pedidos con valores ausentes tienen más de 64 productos?" es False.
# La agrupación muestra la cantidad de productos en cada uno de estos pedidos con datos ausentes. El pedido con el menor conteo de productos tiene 65 productos.
# Esto sugiere que hay una variabilidad en la cantidad de productos en estos pedidos y algunos pueden tener menos de 64 productos.

# In[83]:


# Remplaza los valores ausentes en la columna 'add_to_cart? con 999 y convierte la columna al tipo entero.
order_products_df['add_to_cart_order'].fillna(999, inplace=True)
order_products_df['add_to_cart_order'] = order_products_df['add_to_cart_order'].astype(int)


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# El código anterior se encargó de reemplazar los valores ausentes en la columna 'add_to_cart_order' con el valor 999 y luego convirtió la columna al tipo entero. Este enfoque permite manejar los valores ausentes de manera temporal mediante una asignación de un valor específico.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 2. Preprocesamiento de los datos
# 
# Las tareas de preprocesamiento de datos son esenciales para garantizar que los datos estén en un formato adecuado y sean coherentes antes de realizar análisis más profundos. 
# En products_df, se identificarán y completarán los valores ausentes en 'product_name' con 'Unknown'. Esto permite mantener la integridad de la información y no introduce sesgos en la interpretación de los datos.
# En orders_df, se abordará la ausencia en 'days_since_prior_order' completando los valores ausentes. También se revisarán y eliminarán duplicados si existen, garantizando que cada pedido esté representado de manera única.
# En products_df, se eliminarán duplicados en 'product_name' para mantener la consistencia y evitar redundancias.
# En departments_df y aisles_df, se verificarán duplicados y se eliminarán para mantener la integridad de estos datos.
# En order_products_df, se realizará una revisión y eliminación de duplicados para asegurar la integridad de los datos.
# Estas acciones están destinadas a mejorar la calidad de los datos y prepararlos para análisis posteriores.

# # Paso 3. Análisis de los datos
# 
# Una vez los datos estén procesados y listos, haz el siguiente análisis:

# # [A] Fácil (deben completarse todos para aprobar)
# 
# 1. Verifica que los valores en las columnas `'order_hour_of_day'` y `'order_dow'` en la tabla orders sean razonables (es decir, `'order_hour_of_day'` oscile entre 0 y 23 y `'order_dow'` oscile entre 0 y 6).
# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.

# ### [A1] Verifica que los valores sean sensibles

# In[84]:


hour_of_day_check = orders_df['order_hour_of_day'].between(0, 23).all()
print("Valores razonables en 'order_hour_of_day':", hour_of_day_check)


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto, buena forma de verificar esto. Lo más común es imprimir todos los valores diferentes, pero esta forma es mejor.
# </div>

# In[85]:


day_of_week_check = orders_df['order_dow'].between(0, 6).all()
print("Valores razonables en 'order_dow':", day_of_week_check)


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto, buena forma de verificar esto. Lo más común es imprimir todos los valores diferentes, pero esta forma es mejor.
# </div>

# Escribe aquí tus conclusiones
# 
# Basados en los resultados obtenidos, todos los valores en la columna 'order_hour_of_day' están dentro del rango esperado de 0 a 23, lo cual es coherente con la representación de las horas del día. No hay valores atípicos ni fuera de límites.
# Todos los valores en la columna 'order_dow' están dentro del rango esperado de 0 a 6. Lo cual concuerda con la convención de representación del día de la semana, no hay valores atípicos ni fuera de límites.
# Los datos en estas dos columnas son consistentes y no presentan anomalías evidentes.

# ### [A2] Para cada hora del día, ¿cuántas personas hacen órdenes?

# In[86]:


orders_per_hour = orders_df.groupby('order_hour_of_day')['user_id'].nunique()
plt.figure(figsize=(12, 6))
sns.barplot(x=orders_per_hour.index, y=orders_per_hour.values, color='skyblue')
plt.title('Número de Personas que Hacen Pedidos por Hora del Día')
plt.xlabel('Hora del Día')
plt.ylabel('Número de Personas')
plt.show()


# Escribe aquí tus conclusiones
# 
# Se puede observar que desde las 10 hasta las 15 horas se tienen los picos mas altos de numeros de personas que hacen pedidos, manteniendose valores muy proximos entre si dentro de ese rango de horas pero que anterior a esos horarios son valores mucho mas bajos pero que incrementan mientras mas se acercan a esos horarios, mientras que por el otro lado despues de las 15 horas se observa una decaida progresiva continua.  

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Muy bien! El gráfico está muy claro
# </div>

# ### [A3] ¿Qué día de la semana compran víveres las personas?

# In[87]:


orders_per_day = orders_df.groupby('order_dow')['user_id'].nunique()
day_names = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
orders_per_day.index = day_names
plt.figure(figsize=(10, 6))
sns.barplot(x=orders_per_day.index, y=orders_per_day.values, palette='viridis')
plt.title('Número de Personas que Hacen Pedidos por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Número de Personas')
plt.show()


# Escribe aquí tus conclusiones
# 
# Se puede observar que los dias de la semana en que hay mayor numero de personas que hacen pedidos son los dias Domingo y Lunes y los demas días de la semana se pueden observar valores por debajo de los reportados en lso días Domingo y Lunes pero ligeramente cercanos a 50000 personas. 

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ### [A4] ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.

# In[88]:


valid_orders = orders_df.dropna(subset=['days_since_prior_order'])
plt.figure(figsize=(12, 6))
sns.histplot(valid_orders['days_since_prior_order'], bins=30, kde=True, color='skyblue')
plt.title('Distribución del Tiempo de Espera hasta el Siguiente Pedido')
plt.xlabel('Días desde el Pedido Anterior')
plt.ylabel('Frecuencia')
plt.show()


# Escribe aquí tus conclusiones
# Se puede observar que los días desde el pedido anterior con mayor frecuencia son el 8 y el 30 representando los picos mas altos mientras que en los valores anteriores al 8 son valores que inician por debajo de los 10000 y asienden a lo largo del eje, posteriormente desienden dramaticamente hasta el día 30 donde tiene una drastica subida en frecuencia. 

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto, muy bien al agregar la densidad
# </div>

# # [B] Intermedio (deben completarse todos para aprobar)
# 
# 1. ¿Existe alguna diferencia entre las distribuciones `'order_hour_of_day'` de los miércoles y los sábados? Traza gráficos de barra de `'order_hour_of_day'` para ambos días en la misma figura y describe las diferencias que observes.
# 2. Grafica la distribución para el número de órdenes que hacen los clientes (es decir, cuántos clientes hicieron solo 1 pedido, cuántos hicieron 2, cuántos 3, y así sucesivamente...).
# 3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

# ### [B1] Diferencia entre miércoles y sábados para  `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# In[89]:


wednesday_data = orders_df[orders_df['order_dow'] == 3]


# In[90]:


saturday_data = orders_df[orders_df['order_dow'] == 6]


# In[91]:


# Gráfico de barras para 'order_hour_of_day' en miércoles
plt.figure(figsize=(12, 6))
sns.countplot(x='order_hour_of_day', data=wednesday_data, color='skyblue')
plt.title('Distribución de order_hour_of_day en Miércoles')
plt.xlabel('Hora del Día')
plt.ylabel('Número de Pedidos')
plt.show()
# Gráfico de barras para 'order_hour_of_day' en sábados
plt.figure(figsize=(12, 6))
sns.countplot(x='order_hour_of_day', data=saturday_data, color='salmon')
plt.title('Distribución de order_hour_of_day en Sábado')
plt.xlabel('Hora del Día')
plt.ylabel('Número de Pedidos')
plt.show()


# In[92]:


# Crear una figura con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

# Gráfico de barras para 'order_hour_of_day' en miércoles
sns.countplot(x='order_hour_of_day', data=wednesday_data, color='skyblue', ax=axes[0])
axes[0].set_title('Distribución de order_hour_of_day en Miércoles')
axes[0].set_xlabel('Hora del Día')
axes[0].set_ylabel('Número de Pedidos')

# Gráfico de barras para 'order_hour_of_day' en sábados
sns.countplot(x='order_hour_of_day', data=saturday_data, color='salmon', ax=axes[1])
axes[1].set_title('Distribución de order_hour_of_day en Sábado')
axes[1].set_xlabel('Hora del Día')
axes[1].set_ylabel('Número de Pedidos')

plt.tight_layout()
plt.show()


# Escribe aquí tus conclusiones
# 
# No se observa  diferencia en los picos o valles en horas del día especificas. Esto podría indicar  que en ambos días coinciden los momentos preferidos para realizar pedidos. Asi mismo la distribución en ambos casos mantiene una forma similar y no  se observa alguna diferencia marcada en la concentración de pedidos en ciertas horas.
# Sinembargo en las horas pico es posible observar una ligera variación en el rango comprendido de 9 hasta 17 en ambos días. 

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Los gráfico están bien pero no corresponden a los días correctos. Por otro lado, sería mejor si estuviesen juntos en un mismo recuadro, así se podrían comparar lado a lado
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# Ya he corregido el detalle con los días. Estoy de acuerdo contigo Oscar en que seria mejor que lso gráficos estuviesen en un mismo recuadro pero la instrucción no lo especifica de hecho es muy ambiguo en cuanto a la forma de presentar la información... por lo que me limito a usar los recuadros en Jupyterhub que el proyecto pone por defecto y llenarlos de la manera mas sencilla posible a falta de instrucciones para evitar poner esfuerzo en detalles que no fueron solicitados en el proyecto. Seria bueno que en los proyectos se pueda leer de manera clara la manera de entregar los resultados.
# </div>

# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien con la corrección de los días. Acerca de tus comentarios de las instrucciones, no siempre las instrucciones serán sumamente específicas en lo requerido y queda a tu criterio cómo mostrar lo que se solicita. En este caso mi comentario hace referencia a que se vería mejor ambos gráficos de barra uno junto a otro, pero no es obligatorio puesto que no lo indican las instrucciones. Sin embargo, queda más clara la comparación cuando están superpuestos los gráficos, te muestro
# </div>

# In[93]:


data = (
    pd.concat([wednesday_data['order_hour_of_day'].value_counts().sort_index(),
           saturday_data['order_hour_of_day'].value_counts().sort_index()],
          axis=1)
)
data.columns = ['wed','sat']
data.plot(kind='bar',
          title='Comparación de pedidos del miércoles y sábado',
          xlabel='Hora del día',
          ylabel='Número de pedidos',
          figsize=(12,6)
         )
plt.show()


# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# En los proyectos (del curso y reales) los resultados no tendrán una única forma de mostrarse, es importante explorar diferentes formas de presentar los resultados.
# </div>

# ### [B2] ¿Cuál es la distribución para el número de pedidos por cliente?

# In[94]:


orders_per_user = orders_df.groupby('user_id')['order_number'].max().value_counts().sort_index()
sns.set(style="whitegrid")


# In[95]:


plt.figure(figsize=(12, 6))
sns.barplot(x=orders_per_user.index, y=orders_per_user.values, color='blue')
plt.title('Distribución del Número de Pedidos por Cliente')
plt.xlabel('Número de Pedidos por Cliente')
plt.ylabel('Número de Clientes')
plt.show()


# Escribe aquí tus conclusiones
# Se puede observar que el Número de clientes tiene un crecimiento considerable desde 1 hasta 4 pedidos por clientes y que el número de pedidos por cliente tiene un pico máximo en 4 por encima de 12000 en número de clientes y posteriormente se observa una disminución del número de clientes respecto al incremento del número de pedidos.
# 

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto, también se podría haber contado el número de pedidos por cliente
# </div>

# ### [B3] ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?

# In[96]:


top_products = order_products_df['product_id'].value_counts().head(20)
top_products_info = products_df[products_df['product_id'].isin(top_products.index)][['product_id', 'product_name']]
top_products_info['product_label'] = top_products_info.apply(lambda row: f"{row['product_name']} (ID: {row['product_id']})", axis=1)


# In[97]:


print(top_products_info)


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# In[98]:


sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.barplot(x=top_products.values, y=top_products_info['product_label'], color='blue')
plt.title('Top 20 Productos Más Populares')
plt.xlabel('Número de Pedidos')
plt.ylabel('Nombre del Producto')
plt.show()


# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# El gráfico tiene un error, no están bien pareados los labels del eje-y, dale una revisión por separado a la data y a los ids.
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# Me costó realizarlo sin tener que volver a rehaccer el gráfico desde cero, entendi lo que realizó pero debo estudiar mas de cerca como trabaja la función lambda.
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien, corregido!
# </div>

# Escribe aquí tus conclusiones
# 
# En el gráfico se puede observar una alta demanda del prosucto Organic Lemon teniendo un número de pedidos por encima de 60000. De ahi se observa una disminución para la demanda del número de pedidos de los productos siguientes, tambien es posible observar que los productos Organic Garlics y Limes son los unicos productos que llegan a tener el mismo número de pedidos. Por el contrario es posible observar que los productos con menos demanda por número de pedidos son los productos Large Lemon, Organic Avocado y Cucumber Kirby.

# # [C] Difícil (deben completarse todos para aprobar)
# 
# 1. ¿Cuántos artículos suelen comprar las personas en un pedido? ¿Cómo es la distribución?
# 2. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?
# 3. Para cada producto, ¿cuál es la tasa de repetición del pedido (número de repeticiones de pedido/total de pedidos?
# 4. Para cada cliente, ¿qué proporción de los productos que pidió ya los había pedido? Calcula la tasa de repetición de pedido para cada usuario en lugar de para cada producto.
# 5. ¿Cuáles son los 20 principales artículos que la gente pone primero en sus carritos (muestra las IDs de los productos, sus nombres, y el número de veces en que fueron el primer artículo en añadirse al carrito)?

# ### [C1] ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?

# In[99]:


items_per_order = order_products_df.groupby('order_id')['product_id'].count()
print(items_per_order.describe())


# In[100]:


sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.histplot(items_per_order, bins=50, kde=True, color='green')
plt.title('Distribución de la Cantidad de Artículos por Pedido')
plt.xlabel('Número de Artículos por Pedido')
plt.ylabel('Frecuencia')


# In[101]:


plt.show()


# Escribe aquí tus conclusiones
# Se observa que el número de artículos pedidos tiene un pico maximo comprendido entre 1 y 20 con una frecuencia por encima de 80000 al principio del diagrama por lo cual podemos notar que la mayoria de los clientes tienden a realizar pedidos de un mayor número de articulos que 20 con mucha menor frecuencia.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ### [C2] ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

# In[102]:


# Agrupa por product_id y cuenta la frecuencia de cada producto
product_frequency = order_products_df.groupby('product_id')['reordered'].sum()


# In[103]:


# Ordena los productos por frecuencia en orden descendente y toma los primeros 20
top_reordered_products = product_frequency.sort_values(ascending=False).head(20)


# In[104]:


# Fusiona con el dataframe de productos para obtener información adicional
top_products_info = pd.merge(top_reordered_products, products_df, on='product_id', how='left')[['product_id', 'product_name', 'reordered']]


# In[105]:


# Muestra los 20 productos más reordenados con sus nombres e IDs
print(top_products_info)


# Escribe aquí tus conclusiones
# 
# La lista incluye productos comunes y de consumo diario, como bananas, fresas, espinacas, aguacates, leche, limones, etc. Muchos de los productos son etiquetados como "orgánicos", lo que sugiere que los clientes tienen una preferencia por productos orgánicos. La presencia de ingredientes como cebollas, ajo, limones y aguacates sugiere que los clientes también están comprando productos básicos utilizados en una variedad de recetas. La presencia de frutas junto con productos orgánicos, indican una tendencia hacia opciones más saludables y sostenibles. Es posible juntar varios de estos productos en ofertas promocionales para incentivar compras adicionales.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto! Buen trabajo
# </div>

# ### [C3] Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# In[56]:


# Calcular la proporción de veces que un producto se pide y se vuelve a pedir
product_reorder_ratio = order_products_df.groupby('product_id')['reordered'].mean().reset_index()
product_reorder_ratio.rename(columns={'reordered': 'reorder_ratio'}, inplace=True)


# In[57]:


# Combinar con la información del producto
product_reorder_ratio = pd.merge(product_reorder_ratio, products_df[['product_id', 'product_name']], how='left', on='product_id')


# In[58]:


# Ordenar por la proporción en orden descendente
product_reorder_ratio = product_reorder_ratio.sort_values(by='reorder_ratio', ascending=False)
print(product_reorder_ratio.head())


# Escribe aquí tus conclusiones
# 
# El resultado muestra algunos productos que tienen una proporción de reorden del 100%, lo que significa que estos productos siempre se vuelven a pedir cuando se solicitan por primera vez. Algunos de los productos son "Bone Strength Take Care", "Vanilla Sandwich Cookies", "Palmiers- Petite", entre otros.
# Es importante tener en cuenta que estos resultados podrían estar influenciados por la popularidad general de los productos. Si un producto es muy popular, es más probable que se vuelva a pedir.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Excelente, muy bien!
# </div>

# ### [C4] Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

# In[59]:


# Calcular el total de productos únicos por cliente
total_products_per_customer = order_products_df.groupby('order_id')['product_id'].nunique()

# Crear un dataframe que contenga la información del cliente y el total de productos únicos
customer_products_df = orders_df[['user_id', 'order_id']].merge(total_products_per_customer, left_on='order_id', right_index=True)

# Renombrar la columna resultante
customer_products_df = customer_products_df.rename(columns={'product_id': 'unique_products'})


# In[60]:


# Calcular el total de productos pedidos por cada cliente
total_products_per_customer = order_products_df.groupby('order_id')['product_id'].count()

# Agregar la información al dataframe
customer_products_df['total_products'] = customer_products_df['order_id'].map(total_products_per_customer)

# Calcular la proporción de productos únicos por cliente
customer_products_df['reorder_ratio'] = customer_products_df['unique_products'] / customer_products_df['total_products']

# Imprimir el resultado
print(customer_products_df[['user_id', 'reorder_ratio']])


# Escribe aquí tus conclusiones
# 
# El resultado muestra la proporción de productos únicos que cada cliente ha pedido en comparación con el total de productos que ha pedido. En este caso, todas las proporciones son 1.0, lo que indica que cada cliente ha pedido únicamente productos únicos en cada uno de sus pedidos. Es posible que esta sea una peculiaridad de los datos o que algunos clientes realmente estén ordenando productos diferentes en cada pedido.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto!
# </div>

# ### [C5] ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

# In[61]:


# Agrupar por 'product_id' y calcular la suma de 'add_to_cart_order' para cada producto
top_first_products = order_products_df.groupby('product_id')['add_to_cart_order'].sum()


# In[62]:


# Ordenar en orden descendente y tomar los primeros 20
top_first_products = top_first_products.sort_values(ascending=False).head(20)


# In[63]:


# Fusionar con el dataframe de productos para obtener los nombres de los productos
top_first_products = pd.merge(top_first_products.reset_index(), products_df[['product_id', 'product_name']], on='product_id')
print(top_first_products[['product_id', 'product_name']])


# Escribe aquí tus conclusiones
# 
# Las 20 principales productos que las personas ponen primero en sus carritos, según el orden de la columna 'add_to_cart_order', son en su mayoría productos frescos y saludables. Esto sugiere que los clientes tienden a comenzar sus pedidos con productos frescos y orgánicos, lo cual es consistente con patrones de compra saludables.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto! Muy buen trabajo en esta última parte
# </div>

# ### Conclusion general del proyecto:

# Paso 1: Descripción de los Datos
# 
# El preprocesamiento de datos y el análisis exploratorio proporcionan información valiosa sobre los patrones de 
# compra de los clientes en la plataforma de Instacart. 
# 
# Pedidos (instacart_orders.csv):Se proporciona información detallada sobre los pedidos, incluyendo el ID de pedido, 
# ID de usuario, número de orden, día de la semana, hora de día y días desde el pedido anterior.
# 
# Productos (products.csv): Cada fila representa un producto único con su ID, nombre, ID de pasillo y ID de departamento.
#     
# Orden de Productos (order_products.csv): Contiene detalles sobre los productos en cada pedido, incluyendo el ID de pedido,
# ID de producto, orden en que se agregó al carrito y si el producto se volvió a pedir.
# 
# Pasillos (aisles.csv) y Departamentos (departments.csv): Estas tablas proporcionan información sobre las categorías de pasillos
# y departamentos, respectivamente.
# 
# Paso 2: Preprocesamiento de los Datos
#     
# Valores Ausentes: Identificamos y manejamos valores ausentes en las columnas 'product_name', 'days_since_prior_order', y 
# 'add_to_cart_order'. En la columna 'product_name', completamos los valores ausentes con 'Unknown'.
# 
# Valores Duplicados: Buscamos y eliminamos duplicados en diversas tablas para garantizar la integridad de los datos.
#     
# Tipos de Datos: Verificamos y corregimos los tipos de datos, convirtiendo las columnas de ID a números enteros.
#     
# Paso 3: Análisis de los Datos
#     
# Análisis Exploratorio: Verificamos la razonabilidad de las columnas 'order_hour_of_day' y 'order_dow'.
#     
# Exploramos la distribución de pedidos por hora y día de la semana.
# Analizamos el tiempo que las personas esperan hasta hacer otro pedido.
# Observamos las diferencias entre las horas de pedido de los miércoles y sábados.
# Exploramos la distribución de número de pedidos por cliente.
# Identificamos los productos más populares y aquellos que se vuelven a pedir con mayor frecuencia.
# Analizamos la proporción de productos que los clientes piden y vuelven a pedir.
# Calculamos la proporción de productos que los clientes ya han pedido en el pasado.
# 
# Conclusiones Finales
# 
# Patrones de Compra: 
# Los clientes tienden a comenzar sus pedidos con productos frescos y orgánicos.
# Hay una preferencia por realizar pedidos durante el día y a mitad de semana.
# La mayoría de los clientes tienden a esperar menos de una semana para realizar otro pedido.
# 
# Productos Populares: Se identificaron los 20 productos más populares y los 20 que se añaden primero al carrito.
# 
# Análisis de Comportamiento de Cliente: Se examinó la proporción de productos que los clientes vuelven a pedir y cuántos 
# productos nuevos agregan a sus carritos.
# 
# Distribución de Pedidos: Se exploró la distribución de número de pedidos por cliente.
#     
# Finalmente podemos concluir que estos hallazgos pueden ser fundamentales para tomar decisiones 
# comerciales informadas y mejorar la experiencia de clientes.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# La celda anterior la convertí a markdown. Está muy bien como resumen de lo realizado en el proyecto pero intenta incluir más resultados, métricas claves y hallazgos del trabajo
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# Correcto lo tendré en mente, podrias apoyarme indicando si se trata de las conclusiones obtenidas a lo largo de los ejercicios anteriores del proyecto o ¿que otras metricas y claves serian importantes incluir?  
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Depende del proyecto, en este caso, por ejemplo se podría mencionar que los tiempos entre pedidos son por lo general menor a 8 días (sería aún mejor si se calculase el porcentaje que esto representa del total) o que durante la semana las personas que hacen pedidos son alrededor de 45 mil y los dos días de más venta aumentan a 55 mil. 
# </div>
