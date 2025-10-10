from gestion import dispositivos, buscar_dispositivo

# ESTA ORIENTADO A LAS FUNCIONES ESPECIFICAS DE LA ASPIRADORA

def verificar_limpieza(id_dispositivo):
    for dispositivo in dispositivos:
        if dispositivo["id_dispositivo"] == id_dispositivo:
             if dispositivo ["categoria"] != "aspiradora":
                return f"El dispositivo {dispositivo['categoria']} no tiene función de limpieza automática."
              #Chequeamos que la actualizacion este activa
             if "automatizacion_activa" in dispositivo:
                if dispositivo["automatizacion_activa"] == False:
                    return f"La automatización está desactivada para el dispositivo {dispositivo['categoria']}."
                else:
                     pass
               
             if dispositivo["estado"] == False:
                return f"Su dispositivo {dispositivo['categoria']} está apagado, no se puede verificar el estado."
             elif dispositivo["estado"] == True:
                if 60 <= dispositivo["indice_de_suciedad"] <= 100:
                    return f"  El dispositivo {dispositivo['categoria']} necesita limpieza urgente. Regresa a la base para autolimpieza automática. ¡Índice reseteado!"
                elif 30 <= dispositivo["indice_de_suciedad"] < 60:
                    return f" Su {dispositivo['categoria']} esta en un nivel medio de suciedad. Se recomienda una limpieza preventiva."
                elif 0 <= dispositivo["indice_de_suciedad"] < 30:
                    return f" Su {dispositivo['categoria']} puede seguir funcionando. Nivel óptimo de limpieza."
                else:
                    return "Índice de suciedad inválido o fuera de rango."
    return "Dispositivo no encontrado."

def activar_automatizacion(id_dispositivo, accion):
    dispositivo = buscar_dispositivo(id_dispositivo)
    if not dispositivo:
        return "Dispositivo no encontrado."

    if dispositivo["categoria"] != "aspiradora":
        return f"La automatización de limpieza solo está disponible para aspiradoras, no para {dispositivo['categoria']}."

    if accion == "activar":
        dispositivo["estado"] = True
        return "Automatización para aspiradora activada correctamente."
    elif accion == "desactivar":
        dispositivo["estado"] = False
        return "Automatización para aspiradora desactivada correctamente."
    else:
        return "Acción inválida. Ingrese 'activar' o 'desactivar'."

def listar_estado_automatizacion():
    resultado = ""
    for dispositivo in dispositivos:
        # Solo las aspiradoras tienen automatización de limpieza
        if dispositivo["categoria"].lower() == "aspiradora":
            # Si no existe la clave, asumimos que está desactivada
            if "automatizacion_activa" in dispositivo and dispositivo["automatizacion_activa"] == True:
                estado_auto = "Activada"
            else:
                estado_auto = "Desactivada"
        else:
            estado_auto = "No aplica"
       
        resultado += (
            f"ID {dispositivo['id_dispositivo']}    "
            f"{dispositivo['nombre']} ({dispositivo['categoria']})   "
            f"Automatización: {estado_auto}\n"
        )
    
    if resultado == "":
        return "No hay dispositivos registrados."
    return resultado