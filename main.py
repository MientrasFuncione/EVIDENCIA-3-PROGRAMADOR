from gestion import registrar_dispositivo, agregar_dispositivos, listar_dispositivo, buscar_dispositivo, eliminar_dispositivo
from usuarios import agregar_usuario, login_usuario, buscar_usuario, consultar_datos_personales
from admin import login_admin, cambiar_rol, buscar_usuario as buscar_usuario_admin
from automatizacion import listar_estado_automatizacion, activar_automatizacion, verificar_limpieza

def menu_principal():
    print("\n**** SISTEMA DE GESTIÓN SMART-HOME ****")
    print("¿Ya estás registrado en el sistema?")
    print("1. --Si, iniciar sesión--")
    print("2. --No, registrarme por primera vez--")
    print("3. Salir")

def registrar_nuevo_usuario():
    print("\n**** REGISTRO NUEVO USUARIO ****")
    print(" ---El primer usuario registrado, será ADMINISTRADOR---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    usuario = input("Nombre de usuario: ").lower()
    password = input("Contraseña: ")

    resultado = agregar_usuario(nombre, apellido, usuario, password)
    print(resultado)
    input("Presione Enter para continuar.")

def menu_administrador():
    print("\n**** MENÚ ADMINISTRADOR ****")
    print("1. Consultar automatizaciones activas")
    print("2. Gestionar dispositivos")
    print("3. Modificar rol de usuario")
    print("4. Salir")

def menu_usuario_estandar():
    print("\n**** MENÚ USUARIO ESTÁNDAR ****")
    print("1. Consultar mis datos personales")
    print("2. Consultar dispositivos disponibles")
    print("3. Configurar automatización")
    print("4. Salir")

def submenu_gestion_dispositivos():
    while True:
        print("\n**** GESTIÓN DE DISPOSITIVOS ****")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            while True:
                id_dispositivo = int(input("Ingrese ID del dispositivo: "))
                if registrar_dispositivo(id_dispositivo):
                    print("Ya está registrado. Intente otro ID.")
                else:
                    nombre = input("Nombre: ")
                    categoria = input("Categoría: ")
                    marca = input("Marca: ")
                    print(agregar_dispositivos(id_dispositivo, nombre, categoria, marca))
                    break
            input("Presione Enter para continuar.")
            
        elif opcion == "2":
            print("\n--- LISTADO DE DISPOSITIVOS ---")
            print(listar_dispositivo())
            input("Presione Enter para continuar.")
            
        elif opcion == "3":
            id_dispositivo = int(input("Ingrese ID a buscar: "))
            dispositivo = buscar_dispositivo(id_dispositivo)
            if dispositivo:
                print(f"Dispositivo encontrado: {dispositivo}")
            else:
                print("Dispositivo no encontrado")
            input("Presione Enter para continuar.")
            
        elif opcion == "4":
            id_dispositivo = int(input("ID a eliminar: "))
            confirmacion = input("¿Eliminar? (s/n): ").lower()
            if confirmacion == "s":
                print(eliminar_dispositivo(id_dispositivo))
            else:
                print("Cancelado.")
            input("Presione Enter para continuar.")
            
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    while True:
        menu_principal()
        seleccion = input("Ingrese una opción: ")

        if seleccion == "1":
            print("\n--- INICIO DE SESIÓN ---")
            usuario = input("Usuario: ")
            password = input("Contraseña: ")
            
            resultado_admin = login_admin(usuario, password)
            
            if "exitoso" in resultado_admin:
                print(resultado_admin)
                while True:
                    menu_administrador()
                    opcion = input("Seleccione una opción: ")
                    
                    if opcion == "1":
                        print("\n--- AUTOMATIZACIONES ACTIVAS ---")
                        print(listar_estado_automatizacion())
                        input("Presione Enter para continuar.")
                        
                    elif opcion == "2":
                        submenu_gestion_dispositivos()
                        
                    elif opcion == "3":
                        print("\n*** MODIFICAR ROL DE USUARIO ***")
                        usuario_modificar = input("Ingrese nombre de usuario: ")
                        nuevo_rol = input("Ingrese nuevo rol (administrador/usuario): ")
                        
                        if nuevo_rol in ["administrador", "usuario"]:
                            resultado = cambiar_rol(usuario_modificar, nuevo_rol)
                            print(resultado)
                        else:
                            print("Rol inválido. Use 'administrador' o 'usuario'")
                        input("Presione Enter para continuar.")
                        
                    elif opcion == "4":
                        print("Saliendo del menú de Administrador...")
                        break
                    else:
                        print("Opción inválida")
                        
            else:
                resultado_usuario = login_usuario(usuario, password)
                
                if "exitoso" in resultado_usuario:
                    print(resultado_usuario)
                    usuario_logueado = buscar_usuario(usuario)
                    
                    while True:
                        menu_usuario_estandar()
                        opcion = input("Seleccione una opción: ")
                        
                        if opcion == "1":
                            print("\n**** MIS DATOS PERSONALES ****")
                            print(consultar_datos_personales(usuario_logueado))
                            input("Presione Enter para continuar.")
                            
                        elif opcion == "2":
                            print("\n**** DISPOSITIVOS DISPONIBLES ****")
                            print(listar_dispositivo())
                            input("Presione Enter para continuar.")
                            
                        elif opcion == "3":
                            print("\n**** CONFIGURAR AUTOMATIZACIÓN ****")
                            print("Dispositivos disponibles:")
                            print(listar_dispositivo())
                            id_dispositivo = int(input("Ingrese ID del dispositivo: "))
                            accion = input("Ingrese acción (activar/desactivar): ")
                            resultado = activar_automatizacion(id_dispositivo, accion)
                            print(resultado)
                            input("Presione Enter para continuar.")
                            
                        elif opcion == "4":
                            print("Saliendo del menú de Usuario...")
                            break
                        else:
                            print("Opción inválida")
                else:
                    print("---Usuario o contraseña incorrectos---")

        elif seleccion == "2":
            registrar_nuevo_usuario()
            
        elif seleccion == "3":
            print("¡Gracias por usar el sistema! Hasta pronto.")
            break
            
        else:
            print("Opción inválida. Intente nuevamente.")