from usuarios import usuarios

def login_admin(usuario, password):
    for user in usuarios:
        if (user["usuario"] == usuario and user["password"] == password and user["rol"] == "administrador"):
            return f"Inicio de sesión exitoso. Bienvenido/a, {user['nombre']}!"
    return "Usuario o Contraseña inválida, o no tiene permisos de administrador."

def buscar_usuario(usuario_a_actualizar):
   for user in usuarios:
      if user["usuario"] == usuario_a_actualizar:  
         return user
   return None  
   
def cambiar_rol(usuario_a_actualizar, nuevo_rol):
    roles_definidos = ["administrador", "usuario"]
    if nuevo_rol not in roles_definidos:
        return f"Rol no definido. Los roles válidos son: {roles_definidos}"
   
    user = buscar_usuario(usuario_a_actualizar)
    if not user:
       return "Usuario no encontrado."
    rol_anterior = user["rol"]
    if user["rol"] == nuevo_rol:
        return f"El usuario {usuario_a_actualizar} tiene un nuevo rol como: '{nuevo_rol}'."
    user["rol"] = nuevo_rol
    return f"Cambio de rol exitoso: {usuario_a_actualizar} paso de {rol_anterior} a {nuevo_rol}"

def mostrar_usuario(usuario_a_actualizar):
    user = buscar_usuario(usuario_a_actualizar)
    if user:
        return f"Usuario: {user['usuario']}, Nombre: {user['nombre']} {user['apellido']}, Rol: {user['rol']}"
    else:
        return "Usuario no encontrado."
   
def listar_usuarios():
    salida = "Listado de usuarios:\n"
    for user in usuarios:
        salida += f"- {user['usuario']} ({user['nombre']} {user['apellido']}): {user['rol']}\n"
    return salida