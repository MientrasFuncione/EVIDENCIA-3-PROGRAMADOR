import gestion
import usuarios
import admin
import automatizacion

def menu_principal():
    print("\n Bienvenido/a!!: ")
    print("1. Ingresar como Administrador")
    print("2. Ingresar como Usuario común")
    print("3. Registrarse como Nuevo Usuario")
    print("4. Salir")

def registrar_nuevo_usuario():
    print("\n Registro de nuevo usuario:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    usuario = input("Nombre de usuario: ").lower()
    password = input("Contraseña: ")

    resultado = usuarios.agregar_usuario(nombre, apellido, usuario, password)
    print(resultado)
    input("Presione Enter para continuar.")

def menu_administrador():
    print("\n Menú del Administrador")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Consultar automatizaciones activas")# cambie funciones avanzadas por consultar automatizaciones
    print("6. Cambiar roles de usuario")
    print("7. Salir")

def menu_usuario():
    print("\n Menú del Usuario")
    print("1. Consultar datos")
    print("2. Consultar dispositivos")
    print("3. Configurar automatizacion")
    print("4. Salir")

if __name__ == "__main__":
    while True:
        menu_principal()
        seleccion = input("Ingrese una opción: ")

        if seleccion == "1":  # ADMIN
            usuario = input("Usuario Admin: ")
            password = input("Contraseña: ")
            login_administrador = admin.login_admin(usuario, password)
            print(login_administrador)

            if "exitoso" in login_administrador:
                while True:
                    menu_administrador()
                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":  # AGREGAR DISPOSITIVO
                        while True:
                            id_dispositivo = int(input("Ingrese ID del dispositivo: "))
                            if gestion.registrar_dispositivo(id_dispositivo):
                                print("Ya está registrado. Intente otro ID.")
                            else:
                                nombre = input("Nombre: ")
                                categoria = input("Categoría: ")
                                marca = input("Marca: ")
                                print(gestion.agregar_dispositivos(id_dispositivo, nombre, categoria, marca))
                                input("Presione Enter para continuar.")
                                break

                    elif opcion == "2":  # LISTAR
                        print("Listado:")
                        print(gestion.listar_dispositivo())
                        input("Enter para continuar.")

                    elif opcion == "3":  # BUSCAR
                        id_dispositivo = int(input("Ingrese ID a buscar: "))
                        print(gestion.buscar_dispositivo(id_dispositivo))
                        input("Enter para continuar.")

                    elif opcion == "4":  # ELIMINAR
                        id_dispositivo = int(input("ID a eliminar: "))
                        confirmacion = input("¿Eliminar? (s/n): ").lower()
                        if confirmacion == "s":
                            print(gestion.eliminar_dispositivo(id_dispositivo))
                        else:
                            print("Cancelado.")
                        input("Enter para continuar.")
          
                    elif opcion == "5":  # CONSULTAR AUTOMATIZACIONES ACTIVAS
                            print("Automatizaciones activas:")
                            print(automatizacion.listar_estado_automatizacion())
                            input("Presione Enter para continuar.")    
                            
                       
                    
                    elif opcion == "6":  # CAMBIAR ROLES DE USUARIOS
                         confirmar = input("Desea cambiar el rol del usuario? (s/n): ").lower()
                         if confirmar == "s":        
                            usuario_a_modificar = (input("Ingrese nombre del usuario: ")).lower()
                            usuario_a_buscar = admin.buscar_usuario(usuario_a_modificar)
                            if not usuario_a_buscar:
                                print("Usuario no encontrado.")
                            else:
                                nuevos_roles= input("Ingrese nuevo rol: ('administrador' o 'usuario' ): ").lower()
                                print(admin.cambiar_rol(usuario_a_modificar,nuevos_roles))

                         else:
                            print(" Operación Cancelada.")
                         input("Enter para continuar.")

                    elif opcion == "7":
                        print("Saliendo del menú de Administrador.")
                        break

                    else:
                        print("Opción inválida.")

        elif seleccion == "2":  # USUARIO COMÚN
            usuario = input("Usuario: ")
            password = input("Contraseña: ")
            login_usuario = usuarios.login_usuario(usuario, password)
            print(login_usuario)

            if "exitoso" in login_usuario:
                usuario_logueado = usuarios.buscar_usuario(usuario) 

                while True:
                     menu_usuario()
                
                     opcion = input("Seleccione una opción: ")                    
                        
                     if opcion == "1":  # CONSULTAR DATOS PERSONALES
                        print("Datos Personales: ")
                        print(usuarios.consultar_datos_personales(usuario_logueado))
                        input(" Presione Enter para finalizar.")
                  
                     elif opcion =="2": #CONSULTAR DISPOSITIVOS
                        print("Dispositivos disponibles: ")
                        print(gestion.listar_dispositivo())
                        input(" Presione Enter para finalizar.")

                     elif opcion == "3":  # ACTIVAR AUTOMATIZACION
                        print("Dispositivos disponibles: ")
                        print(gestion.listar_dispositivo())
                        id_dispositivo = int(input("Ingrese el ID del dispositivo que desea automatizar: "))
                        accion = input("Ingrese: ('activar' o 'desactivar'): ").lower()
                        resultado_activar = automatizacion.activar_automatizacion(id_dispositivo, accion)
                        print(resultado_activar)
                        input("Presione Enter para continuar.")
                    
                     elif opcion == "4":
                        print("Saliendo del menú de Usuario.")
                        break
                     else:
                        print("Opción inválida.")

        elif seleccion == "3": #REGISTRAR NUEVO USUARIO
                registrar_nuevo_usuario()
        
        elif seleccion == "4": # SALIR DEL MENU PRINCIPAL
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")