from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    if len(cadena) == 5 and cadena.isalpha():
        return True
    else: 
        return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    tiempo_tardado = fin - inicio
    segundos_totales = int(tiempo_tardado.total_seconds())
    mins = segundos_totales // 60
    segundos = segundos_totales % 60 
    return (mins , segundos)

def quitar_letra(cadena:str,caracter: str)->str:
    '''
    Recibe una cadena y un caracter a eliminar, devuelve la cadena con el texto sin el caracter

    Parámetros:
        cadena:Palabra introducida
        caracter: caracter deseado a eliminar
    Devulve:
        La cadena sin el caracter especificado
    '''
    if not caracter in cadena:
        return cadena
    else:
        txt =""
        borrado= False
        for c in cadena:
            if c == caracter and not borrado:
                txt += ""
                borrado = True 
            else:
                txt += c
        return txt
        

def marcar_verdes(palabra_secreta: str, intento: str)->str:
    verdes = ""
    restantes= palabra_secreta
    for c in range(len(intento)):
        if intento[c] == palabra_secreta[c]:
            verdes += "V"
            restantes = quitar_letra(restantes,intento[c])
        else:
            verdes += "_"
    return (verdes, restantes)

def marcar_amarillos(intento:str,verdes:str,restantes:str)->str:
    colores =""
    for c in range(len(intento)):
        if intento[c] == verdes[c] == "V":
            colores += "V"
        else:
            if intento[c] in restantes:
                colores += "A"
                restantes = quitar_letra(restantes,intento[c])
            else:
                colores+="_"
    return colores
        

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    # TODO: Implementa esta función
    return "_____"  # Elimina esta línea cuando la implementes


