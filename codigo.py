import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#http://datos.salud.gob.ar/dataset/vacunas-contra-covid19-dosis-aplicadas-en-la-republica-argentina

data = pd.read_csv (r'datos_nomivac_covid19.csv')

#contador de hombres y mujeres (sin tener en cuenta los 'S.I.')
sexo = data['sexo'].tolist()
#print(len(sexo))
hombres = data['sexo'].tolist().count('M')
mujeres = data['sexo'].tolist().count('F')
sinInfo = data['sexo'].tolist().count('S.I.')

#contador segun el grupo etario
grupo_etario = data['grupo_etario'].tolist()
#sin_repeticion = list(dict.fromkeys(grupo_etario))
#print(sin_repeticion)
#print(len(grupo_etario))
grupo_etario_18_29 = grupo_etario.count('18-29')
grupo_etario_30_39 = grupo_etario.count('30-39')
grupo_etario_40_49 = grupo_etario.count('40-49')
grupo_etario_50_59 = grupo_etario.count('50-59')
grupo_etario_60_69 = grupo_etario.count('60-69')
grupo_etario_70_79 = grupo_etario.count('70-79')
grupo_etario_80_89 = grupo_etario.count('80-89')
grupo_etario_90_99 = grupo_etario.count('90-99')
grupo_etario_100 = grupo_etario.count('>=100')
grupo_etario_sininfo = grupo_etario.count('S.I.')


#contador tipo de vacuna
tipo_vacuna = data['vacuna'].tolist()
#print(len(tipo_vacuna))
sputnik = tipo_vacuna.count('Sputnik')
sinopharm = tipo_vacuna.count('Sinopharm')
covishield = tipo_vacuna.count('COVISHIELD')
astrazeneca = tipo_vacuna.count('AstraZeneca')


#contador provincia

jurisdiccion_residencia = data['jurisdiccion_residencia'].tolist()
buenosaires = jurisdiccion_residencia.count('Buenos Aires')
caba = jurisdiccion_residencia.count('CABA')
larioja = jurisdiccion_residencia.count('La Rioja')
mendoza = jurisdiccion_residencia.count('Mendoza')
misiones = jurisdiccion_residencia.count('Misiones')
entrerios = jurisdiccion_residencia.count('Entre Ríos')
santafe = jurisdiccion_residencia.count('Santa Fe')
cordoba = jurisdiccion_residencia.count('Córdoba')
tucuman = jurisdiccion_residencia.count('Tucumán')
lapampa = jurisdiccion_residencia.count('La Pampa')
sanluis = jurisdiccion_residencia.count('San Luis')
santacruz = jurisdiccion_residencia.count('Santa Cruz')
jujuy = jurisdiccion_residencia.count('Jujuy')
chaco = jurisdiccion_residencia.count('Chaco')
chubut = jurisdiccion_residencia.count('Chubut')
santiagodelestero = jurisdiccion_residencia.count('Santiago del Estero')
salta = jurisdiccion_residencia.count('Salta')
rionegro = jurisdiccion_residencia.count('Río Negro')
neuquen = jurisdiccion_residencia.count('Neuquén')
sanjuan = jurisdiccion_residencia.count('San Juan')
formosa = jurisdiccion_residencia.count('Formosa')
corrientes = jurisdiccion_residencia.count('Corrientes')
catamarca = jurisdiccion_residencia.count('Catamarca')
tierradelfuego = jurisdiccion_residencia.count('Tierra del Fuego')
sininformacion = jurisdiccion_residencia.count('S.I.')

#Contador segun CONDICION DE VACUNACION ['Estratégico', 'Riesgo', '>60', 'Salud', 'Otros']

condicion_aplicacion = data['condicion_aplicacion'].tolist()
estrategico = condicion_aplicacion.count('Estratégico')
riesgo = condicion_aplicacion.count('Riesgo')
mayor60 = condicion_aplicacion.count('>60')
salud = condicion_aplicacion.count('Salud')
otros = condicion_aplicacion.count('Otros')

#Contador de Orden de dosis

orden_dosis = data['orden_dosis'].tolist()
primera_dosis = orden_dosis.count(1)
segunda_dosis = orden_dosis.count(2)
#sin_repeticion = list(dict.fromkeys(orden_dosis))
#print(sin_repeticion)


#GRAFICO SEGUN ORDEN DE DOSIS

cantidad_orden = [primera_dosis,segunda_dosis]
numero_orden = ['Primera Dosis','Segunda Dosis']

fig, ax = plt.subplots()
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.set_ylabel('Cantidad')
ax.set_xlabel('Numero De Dosis')
ax.set_title('Dosis Vacunadas')
plt.bar(numero_orden,cantidad_orden,width=0.7)
plt.savefig('Segun-Orden-Dosis.jpg')
plt.show()



#GRAFICO SEGUN SEXO

cantidad = [hombres,mujeres,sinInfo]
nombres = ['Hombres','Mujeres','Sin Info']

fig, ax = plt.subplots()
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.set_ylabel('Cantidad')
ax.set_xlabel('Sexo')
ax.set_title('Vacunados Según Sexo')
plt.bar(nombres,cantidad)
plt.savefig('Segun-Sexo.jpg')
plt.show()

#GRAFICO SEGUN LA VACUNA 

cantidad_vacunas = [sputnik,sinopharm,covishield,astrazeneca]
nombres_vacunas = ['Sputnik','Sinopharm','Covishield','Astrazeneca']

fig,ax = plt.subplots()
ax = plt.gca()
ax.get_yaxis()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.set_ylabel('Aplicadas')
ax.set_xlabel('Vacuna')
ax.set_title('Tipos de Vacunas Aplicadas')
plt.bar(nombres_vacunas,cantidad_vacunas)
plt.savefig('Segun-Nombre-Vacuna.jpg')
plt.show()

#GRAFICO RANGO ETARIO 

cantidad_rango_etario = [grupo_etario_18_29, 
grupo_etario_30_39,
grupo_etario_40_49,
grupo_etario_50_59,
grupo_etario_60_69,
grupo_etario_70_79,
grupo_etario_80_89,
grupo_etario_90_99,
grupo_etario_100,
grupo_etario_sininfo]
rango_etario = ['18-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99', '>=100', 'S.I.']

fig,ax = plt.subplots(figsize=(20,10))
ax = plt.gca()
ax.get_yaxis()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.set_ylabel('Cantidad')
ax.set_xlabel('Rango Etario')
ax.set_title('Vacunados Según Rango Etario')
plt.bar(rango_etario,cantidad_rango_etario)
plt.savefig('Segun-Rango-Etario.jpg')
plt.show()

#GRAFICO POR PROVINCIA

cantidad_provincia = [buenosaires,
                     caba,
                     larioja,
                     mendoza,
                     misiones,
                     entrerios,
                     santafe,
                     cordoba,
                     tucuman,
                     lapampa,
                     sanluis,
                     santacruz,
                     jujuy,
                     chaco,
                     chubut,
                     santiagodelestero,
                     salta,
                     rionegro,
                     neuquen,
                     sanjuan,
                     formosa,
                     corrientes,
                     catamarca,
                     tierradelfuego,
                     sininformacion]
nombre_provincia = ['Buenos Aires',
                     'CABA',
                     'La Rioja',
                     'Mendoza',
                     'Misiones',
                     'Entre Ríos',
                     'Santa Fe',
                     'Córdoba',
                     'Tucuman',
                     'La Pampa',
                     'San Luis',
                     'Santa Cruz',
                     'Jujuy',
                     'Chaco',
                     'Chubut',
                     'Santiago del Estero',
                     'Salta',
                     'Río Negro',
                     'Neuquén',
                     'San Juan',
                     'Formosa',
                     'Corrientes',
                     'Catamarca',
                     'Tierra del Fuego',
                     'Sin Info']

fig,ax = plt.subplots(figsize=(35,10))
ax = plt.gca()
ax.get_yaxis()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.set_ylabel('Vacunados')
ax.set_xlabel('Provincia')
ax.set_title('Vacunados Según Provincia')
plt.bar(nombre_provincia,cantidad_provincia)
plt.savefig('Segun-Provincia.jpg')
plt.show()


#GRAFICO SEGÚN CONDICION DE VACUNACIÓN

condicion = [estrategico,riesgo,mayor60,salud,otros]
nombre_condicion = ['Estratégico', 'Riesgo', '>60', 'Salud', 'Otros']

fig, ax = plt.subplots()
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.set_ylabel('Vacunados')
ax.set_xlabel('Condición')
ax.set_title('Vacunados Según Condición')
plt.bar(nombre_condicion,condicion)
plt.savefig('Segun-Condicion.jpg')
plt.show()

#TABLAS 


print("-------------------------------------------------")
tipo_de_vacuna = [['Sputnik',sputnik],['Sinopharm',sinopharm],['Covishield',covishield],['Astrazeneca',astrazeneca]]
df_tipo_de_vacuna = pd.DataFrame(tipo_de_vacuna,columns=['Vacuna','Aplicadas'])
print(df_tipo_de_vacuna.sort_values(by='Aplicadas',ascending=False).to_string(index=False))
print("-------------------------------------------------")
hombres_mujeres = [["Hombres",hombres],['Mujeres',mujeres],['Sin Info',sinInfo]]
df_hombres_mujeres = pd.DataFrame(hombres_mujeres, columns=['Sexo','Vacunados'])
print(df_hombres_mujeres.sort_values(by='Vacunados',ascending=False).to_string(index=False))

print("-------------------------------------------------")
rango_etario = [['18-29',grupo_etario_18_29 ],['30-39',grupo_etario_30_39 ],['40-49',grupo_etario_40_49 ],['50-59',grupo_etario_50_59 ],['60-69',grupo_etario_60_69 ],['70-79',grupo_etario_70_79 ],['80-89',grupo_etario_80_89 ],['90-99',grupo_etario_90_99 ],['>=100',grupo_etario_100],['Sin Información', grupo_etario_sininfo]]
df_rango_etario = pd.DataFrame(rango_etario,columns=['Rango','Vacunados'])
print(df_rango_etario.to_string(index=False))
print("-------------------------------------------------")
segun_provincia = [['Buenos aires',buenosaires ],
                ['CABA', caba],
                ['La Rioja',larioja ],
                ['Mendoza',mendoza],
                ['Misiones',misiones ],
                ['Entre Rios',entrerios],
                ['Santa Fe',santafe ],
                ['Córdoba',cordoba ],
                ['Tucuman',tucuman ],
                ['La Pampa',lapampa ],
                ['San Luis',sanluis ],
                ['Santa Cruz',santacruz ],
                ['Jujuy',jujuy ],
                ['Chaco',chaco ],
                ['Chubut',chubut ],
                ['Santiago del Estero',santiagodelestero ],
                ['Salta',salta ],
                ['Rio Negro',rionegro ],
                ['Neuquen',neuquen ],
                ['San Juan',sanjuan ],
                ['Formosa',formosa ],
                ['Corrientes',corrientes ],
                ['Catamarca',catamarca ],
                ['Tierra del Fuego',tierradelfuego ],
                ['Sin Información',sininformacion ]]

df_provincia = pd.DataFrame(segun_provincia,columns=['Provincia','Vacunados'])
print(df_provincia.sort_values(by='Vacunados',ascending=False).to_string(index=False))

print("-------------------------------------------------")

segun_condicion = [ ['Estratégico',estrategico],[ 'Riesgo',riesgo],[ '>60',mayor60],[ 'Salud',salud],['Otros',otros]]
df_condicion = pd.DataFrame(segun_condicion,columns=['Condición','Vacunados'])
print(df_condicion.sort_values(by='Vacunados',ascending=False).to_string(index=False))

print("-------------------------------------------------")

segun_orden_dosis = [['Primera Dosis',primera_dosis],['Segunda Dosis',segunda_dosis]]
df_orden_dosis = pd.DataFrame(segun_orden_dosis,columns=['Orden','Vacunados'])
print(df_orden_dosis.to_string(index=False))


print("-------------------------------------------------")
