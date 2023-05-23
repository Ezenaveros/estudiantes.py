estudiantes = []
ingresos_invalidos = 0

while True:
    estudiante = input("Ingresar apellido y nombre del estudiante: ").strip().upper()
    if len(estudiante) == 0:
        break

    estudiante_trozado = estudiante.split()
    if len(estudiante_trozado) != 2:
        ingresos_invalidos += 1
        print("solo ingrese apellido y nombre!")
        continue
        
    apellido = estudiante_trozado[0].strip()
    nombre = estudiante_trozado[1].strip()
    if apellido.isalpha() == False or nombre.isalpha() == False:
        ingresos_invalidos += 1
        print("Solo se puede ingresar letras!")
    else:
        estudiante_validado = apellido + " " + nombre
        if estudiante_validado in estudiantes:
            ingresos_invalidos += 1
            print("Estudiante ya ingresado!")
        else:
            estudiantes.append(estudiante_validado)
            print("*ingresado correctamente")

estudiantes.sort()
print(ingresos_invalidos, estudiantes)

print("-" * 80)
print("la cantidad de ingresos invalidos:", (ingresos_invalidos)) 
print("lista ordenada de estudiantes:")
for elemento in estudiantes:
    print(elemento)
print("los estudiantes ingresados son:",len(estudiantes))
print("-" * 80)

archivo = open("estudiantes.txt", "w")
for estudiante in estudiantes:
    archivo.write(estudiante+ "\n")
archivo.close()

    
