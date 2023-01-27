import json


def calc_ap(fluido : str, formula: str, p_atm: float,p_r_ini: float, tramos: list):
    return "None"

def print_info():
    print("")
    print("------------------------")
    print("")

    print(f"Fluido a calcular: {fluido}")
    print(f"Presion atmosferica: {p_atm}")
    print(f"Regimen de alta presión: {alta_presion}")
    print(f"Regimen de baja presión: {baja_presion}")

    print("")
    print("------------------------")
    print("")

#Open file and load data
file = open('test.json')
data = json.load(file)

#orginize data
fluido = data['fluido']
p_atm = data['p_atm']
alta_presion = data['alta_presion']
baja_presion = data['baja_presion']
print_info()

