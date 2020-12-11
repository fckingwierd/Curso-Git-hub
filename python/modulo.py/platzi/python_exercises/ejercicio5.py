def average_temps(temps):
    i_temps = float()
    for temp in temps:
        i_temps += temp

    return i_temps / len(temps)
    

if __name__ == "__main__":
    temps = [12,24,15,17,18,15,29]
    result = average_temps(temps)
    print (f"La temperatura promedio en esta semana fue de: {result}")

