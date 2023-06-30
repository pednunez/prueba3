alumnos=[]
def registro_alumnos():
    nombre=input("ingrese el nombre del alumno: ")
    apellido=input("ingrese el apellido del alumno: ")
    rut=input("ingrese el rut del alumno: ")
    fecha_nacimiento=input("ingrese la fecha de nacimiento: ")
    direccion=input("ingrese la direccion del alumno: ")
    carrera=input("ingrese la carrera del alumno: ")
    asignatura1=input("ingrese la asignatura: ")
    asignatura2=input("ingrese la asignatura: ")
    asignatura3=input("ingrese la asignatura: ")
    nota1=int(float(input("ingrese su promedio: ")))
    nota2=int(float(input("ingrese su promedio: ")))
    nota3=int(float(input("ingrese su promedio: ")))
    
    alumno={
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut,
        "direccion": direccion,
        "fecha de nacimiento": fecha_nacimiento,
        "carrera": carrera,
        "asignatura-1": asignatura1,
        "asignatura-2": asignatura2,
        "asignatura-3": asignatura3,
        "promedio-1": nota1,
        "promedio-2": nota2,
        "promedio-3": nota3,     
    }
    
    alumnos.append(alumno)
    print("¡El alumno a sido registrado!")
    

def buscar():
    buscar_rut=input("ingrese el rut del alumno: ")
    
    for alumno in alumnos:
        if alumno ["rut"] == buscar_rut:
            print("Datos del alumno: ")
            print(f"nombre: {alumno['nombre']}")
            print(f"apellido: {alumno['apellido']}")
            print(f"rut: {alumno['rut']}")
            print(f"fecha de nacimiento: {alumno['fecha de nacimiento']}")
            print(f"direccion: {alumno['direccion']}")
            print(f"carrera: {alumno['carrera']}")
            print(f"asignaturas: {alumno['asignatura']}")
            return
    print("alumno no encontrado, ingrese un rut valido.")
    
    
def certificado_alumno():
    certificado1_rut=input("ingrese el rut del alumno: ")
    
    for alumno in alumnos:
        if alumno ["rut"] == certificado1_rut:
            print("----Certificado de alumno regular----")
            print(f"nombre: {alumno['nombre']}")
            print(f"apellido: {alumno['apellido']}")
            print(f"rut: {alumno['rut']}")
            print(f"fecha de nacimiento: {alumno['fecha de nacimiento']}")
            print(f"direccion: {alumno['direccion']}")
            print(f"carrera: {alumno['carrera']}")
            print("--------------------------------------")
            return
    print("alumno no encontrado, ingrese un rut valido.")
    
    
def certificado_matricula():
    certificado2_rut=input("ingrese el rut del alumno a buscar: ")

    for alumno in alumnos: 
        if alumno ["rut"] == certificado2_rut:
            print("----certificado de matricula----")
            print(f"nombre: {alumno['nombre']}")
            print(f"apellido: {alumno['apellido']}")
            print(f"rut: {alumno['rut']}")
            print(f"fecha de nacimiento: {alumno['fecha de nacimiento']}")
            print(f"direccion: {alumno['direccion']}")
            print(f"carrera: {alumno['carrera']}")
            print("el alumno a sido matriculado.")
            print("--------------------------------")
            return
    print("alumno no encontrado, ingrese un rut valido.")
    
def certificado_notas():
    certificado3_rut=input("ingrese el rut del alumno a buscar: ")
    
    for alumno in alumnos:
        if alumno ["rut"] == certificado3_rut:
            print("----Certificado de Notas----")
            print(f"nombre: {alumno['nombre']}")
            print(f"apellido: {alumno['apellido']}")
            print(f"rut: {alumno['rut']}")
            print(f"fecha de nacimiento: {alumno['fecha de nacimiento']}")
            print(f"direccion: {alumno['direccion']}")
            print(f"carrera: {alumno['carrera']}")
            print(f"asignatura-1: {alumno['asignatura-1']}")
            print(f"asignatura-2: {alumno['asignatura-2']}")
            print(f"asignatura-3: {alumno['asignatura-3']}")
            print(f"promedio-1: {alumno['promedio-1']}")
            print(f"promedio-2: {alumno['promedio-2']}")
            print(f"promedio-3: {alumno['promedio-3']}")
            print("------------------------------")
            
    
while True:
    print("----Bienvenido a Duoc----")
    print("--------------------------")
    print("valor certificados: ")
    print("certificado alumno regular: $1.950-.")
    print("certificado matricula: $3.500-.")
    print("certificado de notas: $2.100-.")
    print("--------------------------")
    print("1) Registrar alumno.")
    print("2) Buscar alumno.")
    print("3) Certificado de alumno regular.")
    print("4) Certificado de matricula.")
    print("5) Certificado de notas.")
    print("6) Salir.")
    print("--------------------------")
    
    opcion=input("Seleccione una opcion: ")
        
    if opcion == "1":
        registro_alumnos()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        certificado_alumno()
    elif opcion == "4":
        certificado_matricula()
    elif opcion == "5":
        certificado_notas()
    elif opcion == "6":
        print("¡gracias por ocupar nuestra plataforma!")
        break
        
    else:
        print("seleccione una opcion valida, intenta nuevamente.")