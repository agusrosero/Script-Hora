# Script en el que ingresando la hora que son te calcula la hora en que te tenes que despertar teniendo en cuenta que dormis: 7.5 hrs. (FORMATO HH:MM)
import datetime

def calcular_hora_despertar(hora_dormir):
    hora_dormir_obj = datetime.datetime.strptime(hora_dormir, '%H:%M') # Convertir la hora de dormir en objeto datetime

    hora_despertar_obj = hora_dormir_obj + datetime.timedelta(hours=7, minutes=30) # Sumar 7.5 horas

    hora_despertar = hora_despertar_obj.strftime('%H:%M') # Convertir la hora de despertar en formato string

    return hora_despertar

hora_dormir = input("Ingresa la hora a la que te vas a dormir (formato HH:MM): ")
hora_despertar = calcular_hora_despertar(hora_dormir)

print(f"Te tendrias que despertar a las: {hora_despertar}")
