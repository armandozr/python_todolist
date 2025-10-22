'''To do list application'''

print("Bienvenido a tu lista de tareas")
print("Para comenzar selecciona una opción:")
task = input("1. Agregar tarea\n2. Ver tareas\n3. Eliminar tarea\n4. Salir\n")
tasks = []
while task != '4':
    if task == '1':
        new_task = input("Ingresa la tarea que deseas agregar: ")
        tasks.append(new_task)
        print(f"Tarea '{new_task}' agregada.")
    elif task == '2':
        if tasks:
            print("Tus tareas:")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t}")
        else:
            print("No tienes tareas pendientes.")
    elif task == '3':
        if tasks:
            print("Selecciona la tarea que deseas eliminar:")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t}")
            to_delete = int(input("Número de la tarea a eliminar: ")) - 1
            if 0 <= to_delete < len(tasks):
                removed_task = tasks.pop(to_delete)
                print(f"Tarea '{removed_task}' eliminada.")
            else:
                print("Número inválido.")
        else:
            print("No tienes tareas para eliminar.")
    else:
        print("Opción inválida. Por favor selecciona una opción válida.")
    task = input("1. Agregar tarea\n2. Ver tareas\n3. Eliminar tarea\n4. Salir\n")
print("Gracias por usar la aplicación de lista de tareas. ¡Hasta luego!")
