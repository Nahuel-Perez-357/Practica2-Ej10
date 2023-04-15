#A
def estructura_general(nombres_alum,notas_alum1,notas_alum2):
	notas_alum= tuple(zip(notas_alum1,notas_alum2))
	nombres_alum=nombres_alum.split(',')
	new_list_name=list(map(lambda nombre: nombre.replace(' ','').replace(',','').replace('\n','').replace("'",''),nombres_alum))
	
	index=range(len(notas_alum))
	dicc={new_list_name[i]:notas_alum[i] for i in index}
	return dicc

#B	
def promedio_x_estudiante(dicci_alum):
	prom_x_estu=dict()
	for clave in dicci_alum:
		prom_x_estu[clave]=sum(dicci_alum[clave])/len(dicci_alum[clave]) if (len(dicci_alum[clave]) > 0) else 0	
	return prom_x_estu

	
#C
def promedio_general(dicci_prom):#usar la lista de promedios y sacar el promedio de promedios
	promedio=sum(dicci_prom.values())/(len(dicci_prom))
	print(f"Resultado del promedio de la clase {round(promedio,2)}")	
	 		
#D
def promedio_alto(dicci_prom):
	alum_max=max(dicci_prom, key=dicci_prom.get)
	print(f"El/La Alumno/a '{alum_max}' tiene el mayor promedio de la clase con un puntaje de '{dicci_prom.get(alum_max)}'")

#E
def select_min(alumno):
	return min(alumno[1])
	
def nota_mas_baja(dicci_alum): 
	alum_min=min(dicci_alum.items(),key=select_min)
	print(f"El/La Alumno/a '{alum_min[0]}' tiene la nota mas baja, teniedo '{min(alum_min[1])}' como nota mas baja")
	
	
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#A)Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. 
#  Utilizar esta estructura para la resolución de los siguientes items.

diccio = estructura_general(nombres,notas_1,notas_2)
print("#Inciso A")
print("*"*150)
print(diccio)
print("*"*150)
print()
#B) Calcular el promedio de notas de cada estudiante.

prom_x_estu=promedio_x_estudiante(diccio)
print("#Inciso B")
print("*"*150)
print(prom_x_estu)
print("*"*150)
print()

#C) Calcular el promedio general del curso.
print("#Inciso C")
promedio_general(prom_x_estu)

#D) Identificar al estudiante con la nota promedio más alta.
print()
print("#Inciso D")
promedio_alto(prom_x_estu)

#E) Identificar al estudiante con la nota más baja.
print()
print("#Inciso E")
nota_mas_baja(diccio)
