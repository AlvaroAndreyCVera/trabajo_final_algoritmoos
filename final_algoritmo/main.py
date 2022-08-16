datos = {"codigo": ["e-001", "e-002", "e-003", "e-004", "e-005"],
          "nombre": ["Dayahana", "Alvaro", "Luis"],
         "curso": ["Literatura", "Desarrolo", "Fisisca"]}
nota_ = []
resp = "s"
while resp == "s":
    codigo = input("Ingresar el codigo del alumno: ")
    curso = input("Ingresa el nombre del curso: ")
    nota_1 = int(input("Ingrese la primera nota del alumno: "))
    nota_2 = int(input("Ingrese la segunda nota del alumno: "))
    nota_3 = int(input("Ingrese la tercera nota del alumno: "))
    x = 0
    for i in datos["codigo"]:
        if i == codigo:
            codigoTemp = i
            nombreTemp = datos["nombre"][x]
            promedio = (nota_1 + nota_2 + nota_3 )/3
            registro = ["Codigo: " + str(codigoTemp) + " | " + "Nombre :" + str(nombreTemp) + " | " + "Curso :" + curso + " | " + "Promedio: " + str(promedio) + " | " +"Nota 1: " + str(nota_1) + "| " + "Nota 2: " + str(nota_2) + " | " + "Nota 3: " + str(nota_3)]
            f = open("examen_final.txt", "a")
            cadena = "".join(registro)
            f.write("\n" + cadena)
            f.close()
        x += 1
    resp = input("¿Desea seguir ingresando datos? : s/n ")
    f = open("examen_final.txt")
    print(f.read())
    f.close()