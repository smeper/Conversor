#conversiones termicas

def centigrados_fahrenheit(temperatura):
    return ((float(temperatura) * 1.8 ) + 32)

def fahrenheit_centigrados(temperatura):
    return ((float(temperatura) / 1.8 ) - 32)

def centigrados_kelvin(temperatura):
    return (float(temperatura) + 273.15)

def kelvin_centigrados(temperatura):
    return (float(temperatura) - 273.15)


#conversion de distancias
def metros_kilometros(distancia):
    return (float(distancia) / 1000)

def pulgadas_centimetros(distancia):
    return (float(distancia) * 2.54)

def milimetros_pulgadas(distancia):
    return ((float(distancia) / 2.54) / 10)

def kilometros_yardas(distancia):
    return (float(distancia) * 1.609344)

def centimetros_pugadas(distancia):
    return (float(distancia) / 2.54)

def pulgadas_milimetros(distancia):
    return ((float(distancia) * 2.54) * 10)

def yarda_kilometros(distancia):
    return (float(distancia) / 1.609344)


#conversion de peso
def kilogramos_libras(peso):
    return (float(peso) / 0.45359)

def kilogramos_piedras(peso):
    return (float(peso) / 6.3503)

def onzas_gramos(peso):
    return (float(peso) * 28.3495)

def onzas_libras(peso):
    return (float(peso) / 16)

def libras_kilogramos(peso):
    return (float(peso) * 0.45359)

def piedras_kilogramos(peso):
    return (float(peso) * 6.3503)

def gramos_onzas(peso):
    return (float(peso) / 28.3495)

def libras_onzas(peso):
    return (float(peso) * 16)