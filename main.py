import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import numpy as np



data = pd.read_csv('C:/Users/Juan David/PycharmProjects/pythonProject3/covidColombia.csv',dtype={"ID de caso":"string","Fecha de notificación":"string","Código DIVIPOLA":"string","Ciudad de ubicación":"string","Departamento o Distrito ":"string","atención":"string","Edad":"int","Sexo":"string","Tipo":"string","Estado":"string","País de procedencia":"string","FIS":"string","Fecha de muerte":"string","Fecha diagnostico":"string","Fecha recuperado":"string","fecha reporte web":"string","Tipo recuperación":"string","Codigo departamento":"string","Codigo pais":"string","Pertenencia etnica":"string","Nombre grupo etnico":"string"})
#print(data)
df=pd.DataFrame(data)
df.rename(columns={'ID de caso':'numero de casos'},inplace=True)
df.groupby('sexo ')['sexo'].count().plot(kind='bar',legend="Reverse",xlabel="departamentos",ylabel="# de casos")
plt.title("casos por sexo")
df.groupby('Departamento o Distrito ')['numero de casos'].count().plot(kind='bar',legend="Reverse",xlabel="departamentos",ylabel="# de casos")
plt.title("casos por departamento")
df.groupby('Departamento o Distrito ')['Fecha de muerte'].count().plot(kind='barh',legend="Reverse",xlabel="departamentos",ylabel="# de casos")
df.groupby('atención')['numero de casos'].count().plot(kind='pie',cmap='Paired')
plt.axis("equal")
plt.ylabel("")
df.groupby('Estado')['numero de casos'].count().plot(kind='pie',cmap='Paired',autopct="%0.01f %%")
plt.axis("equal")
plt.ylabel("")

