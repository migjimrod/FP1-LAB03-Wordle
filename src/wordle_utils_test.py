# Pruebas para las funciones de wordle_utils.py
from wordle_utils import es_palabra_valida
from datetime import datetime

def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

#test_es_palabra_valida()
from wordle_utils import calcula_minutos_y_segundos
def test_calcula_minutos_y_segundos():
    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 1, 23, 0, 30)) == (0, 30)

    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 1, 23, 3, 45)) == (3, 45)

    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 2, 0, 1, 15)) == (61, 15)
#test_calcula_minutos_y_segundos()
from wordle_utils import quitar_letra
def test_quitar_letra():
    assert quitar_letra("casar", "a") == "csar"

    assert quitar_letra("casar", "c") =="asar"

    assert quitar_letra("casar", "r") =="casa"

    assert quitar_letra("casar", "z") == "casar"

    assert quitar_letra("aaaaa", "a") == "aaaa" 
#test_quitar_letra()

from wordle_utils import marcar_verdes
def test_marcar_verdes():
    print("Probando marcar_verdes...")
    assert marcar_verdes("casar", "polio") == ("_____", "casar")
    assert marcar_verdes("casar", "casar") == ("VVVVV", "")
    assert marcar_verdes("casar", "cazar") == ("VV_VV", "s")
    assert marcar_verdes("casar", "secta") == ("_____", "casar")
    assert marcar_verdes("casar", "sacar") == ("_V_VV","cs")
    assert marcar_verdes("casar", "peras") == ("___V_", "csar")
#test_marcar_verdes()
from wordle_utils import marcar_amarillos
def test_marcar_amarillos():
    print("Probando marcar_amarillos...")
    assert marcar_amarillos("polio", "_____", "casar") == "_____"
    assert marcar_amarillos("casar", "VVVVV", "") == "VVVVV"
    assert marcar_amarillos("cazar", "VV_VV", "s") == "VV_VV"
    assert marcar_amarillos("secta", "_____", "casar") == "A_A_A"
    assert marcar_amarillos("sacar", "_V_VV", "cs") == "AVAVV"
    assert marcar_amarillos("peras", "___V_", "csar") == "__AVA"
test_marcar_amarillos()
print("✅Todas las pruebas pasaron correctamente.")