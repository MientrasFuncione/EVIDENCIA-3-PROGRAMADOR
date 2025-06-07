dispositivos=[
 {"id_dispositivo":1,"nombre":"santi cafetera", "categoria": "cafetera","marca":"bgh", "estado":True,"indice_de_suciedad": 0, "automatizacion_activa":False},
 {"id_dispositivo":2,"nombre": "roomba alexia","categoria": "aspiradora","marca":"roomba", "estado":True, "indice_de_suciedad": 100, "automatizacion_activa":True}
 ]


#1- Para agregar decidimos primero corroborar si estaba registrado, de lo contrario agregarlo

def registrar_dispositivo(id_dispositivo):
  for dispositivo in dispositivos:
    if id_dispositivo == dispositivo["id_dispositivo"]:
        return True
  return False

#AGREGAR DISPOSITIVO
def agregar_dispositivos(id_dispositivo,nombre, categoria, marca):
    # Si no se encontró el dispositivo en el registro lo agrego
    nuevo_dispositivo = {
        "id_dispositivo": id_dispositivo,
        "nombre": nombre,
        "categoria": categoria,
        "marca": marca
    }
    dispositivos.append(nuevo_dispositivo)
    return "Dispositivo agregado correctamente"


#2 -LISTAR DISPOSITIVO

def listar_dispositivo():
  resultado_lista=""
  for dispositivo in dispositivos:
      resultado_lista+= f"ID: {dispositivo['id_dispositivo']} , Nombre: {dispositivo['nombre']} , Categoría: {dispositivo['categoria']} , Marca: {dispositivo['marca'] }\n" 
  return(resultado_lista)

#3-BUSCAR DISPOSITIVO

def buscar_dispositivo(id_dispositivo):
   for dispositivo in dispositivos:
        if dispositivo["id_dispositivo"] == id_dispositivo:
         return dispositivo  # Devuelve el dict completo
   return None
         # return f"Dispositivo encontrado:{dispositivo}"
   #return f"Dispositivo Inexistente."


#4- ELIMINAR DISPOSITIVO
def eliminar_dispositivo(id_dispositivo):
   for dispositivo in dispositivos:
        if dispositivo["id_dispositivo"] == id_dispositivo:
          dispositivos.remove(dispositivo)
          return f"Dispositivo {id_dispositivo} eliminado correctamente."
   return "El dispositivo que usted busca no existe."
