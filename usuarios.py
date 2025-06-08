# Base de datos para Registrar un usuario estandar nuevo
usuarios = [ {"nombre": "sol",
              "apellido": "ceballos",
               "usuario":"solcito",
               "password":"holaquetal",
               "rol":"usuario"}]


#1-Se corrobora si el usuario esta registrado
def registrar_usuario(usuario, password):
  for us in usuarios:
   if us["usuario"] == usuario and us["password"] == password:
        return True
  return None


#2- Si no esta registrado, agregar nuevo usuario estandar
def agregar_usuario(nombre, apellido, usuario, password):
    for us in usuarios:
        if us["usuario"] ==usuario:
            return "Usuario ya registrado."
       
    # Si no se encontró el usuario en el registro lo agrego
    nuevo_usuario={
       "nombre": nombre,
       "apellido": apellido,
        "usuario": usuario,
       "password": password,
        "rol": "usuario"
    }


    usuarios.append(nuevo_usuario)
    return "Usuario agregado correctamente"




#3-Validacion de usuario y contraseña para usuario estandar
def login_usuario(usuario, password):
 for us in usuarios:
   if us["usuario"] == usuario and us["password"]== password:
    return f"Inicio de sesión exitoso . Bienvenido/a, {us['nombre']} !"


 return" Usuario o Contraseña inválida. Intente nuevamente."


# Permitir consultar datos


def consultar_datos_personales(usuario_logueado):
      return(
      f"Nombre: {usuario_logueado['nombre']}\n"
      f"Apellido: {usuario_logueado['apellido']}\n"
      f"Usuario: {usuario_logueado['usuario']}\n"
      f"Password: {usuario_logueado['password'] }\n"
      )
 
def buscar_usuario (usuario_nombre):
   for user in usuarios:
      if user["usuario"] ==usuario_nombre:
        return user
   return None
