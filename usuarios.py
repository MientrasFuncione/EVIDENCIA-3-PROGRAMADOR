usuarios = []

def agregar_usuario(nombre, apellido, usuario, password):
    for us in usuarios:
        if us["usuario"] == usuario:
            return "Usuario ya registrado."
    
    if len(usuarios) == 0:
        rol_asignado = "administrador"
    else:
        rol_asignado = "usuario"
       
    nuevo_usuario = {
       "nombre": nombre,
       "apellido": apellido,
       "usuario": usuario,
       "password": password,
       "rol": rol_asignado
    }

    usuarios.append(nuevo_usuario)
    return f"Usuario agregado correctamente. Rol:--- {rol_asignado}---"

def login_usuario(usuario, password):
    for us in usuarios:
        if us["usuario"] == usuario and us["password"] == password:
            return f"Inicio de sesión exitoso. Bienvenido/a, {us['nombre']}!"
    return "Usuario o Contraseña inválida. Intente nuevamente."

def consultar_datos_personales(usuario_logueado):
    return (
        f"Nombre: {usuario_logueado['nombre']}\n"
        f"Apellido: {usuario_logueado['apellido']}\n"
        f"Usuario: {usuario_logueado['usuario']}\n"
        f"Rol: {usuario_logueado['rol']}"
    )
 
def buscar_usuario(usuario_nombre):
    for user in usuarios:
        if user["usuario"] == usuario_nombre:
            return user
    return None