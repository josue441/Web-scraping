from bs4 import BeautifulSoup
import requests


avion = "https://wiki.warthunder.com/unit/f2a-1"

result = requests.get(avion)
if result.status_code == 404:
    print("avion no encontrado")

bs = BeautifulSoup(result.text, "lxml")
temp = bs.find_all("div", "game-unit_card-info_value")

rank = temp[0].text.strip() if len(temp) > 0 else "Desconocido"
battle_rating = temp[1].text.strip() if len(temp) > 1 else "Desconocido"
nation = temp[4].text.strip() if len(temp) > 4 else "Desconocido"
unit = temp[5].text.strip() if len(temp) > 5 else "Desconocido"
operator = temp[6].text.strip() if len(temp) > 6 else "Desconocido"

if rank == "II":
    rank = temp[0].text.strip()
    nation = temp[2].text.strip()
    unit = temp[3].text.strip()
    operator = temp[2].text.strip()

if rank == "I" or rank == "III" or rank == "V" or rank == "IV":
    rank = temp[0].text.strip()
    nation = temp[2].text.strip()
    unit = temp[3].text.strip()
    operator = temp[2].text.strip()

print(f"""Rank: {rank}
    Game nation: {nation}
    Main role: {unit}
    Operator country: {operator}""")


# Maneja posibles datos faltantes
# rank = temp[0].text.strip() if len(temp) > 0 else "Desconocido"
# battle_rating = temp[1].text.strip() if len(temp) > 1 else "Desconocido"
# nation = temp[4].text.strip() if len(temp) > 4 else "Desconocido"
# unit = temp[5].text.strip() if len(temp) > 5 else "Desconocido"
# operator = temp[6].text.strip() if len(temp) > 6 else "Desconocido"