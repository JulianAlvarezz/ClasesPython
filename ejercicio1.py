#Recibir un numero en teclado y determinar si este es múltiplo de 5

''' def es_multiplo_de_cinco(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

if es_multiplo_de_cinco(numero):
    print(f"{numero} es múltiplo de 5.")
else:
    print(f"{numero} no es múltiplo de 5.")
 '''
#Recibir un numero en teclado y determinar si este es múltiplo de 3

''' def es_multiplo_de_tres(numero):
    if numero % 3 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

if es_multiplo_de_tres(numero):
    print(f"{numero} es múltiplo de 3.")
else:
    print(f"{numero} no es múltiplo de 3.") '''

#Recibir dos números y determinar cual es mayor
''' def determinar_mayor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    elif numero2 > numero1:
        return numero2
    else:
        return "Los números son iguales."

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resultado = determinar_mayor(numero1, numero2)
print("El número mayor es:", resultado) '''

#Juan tiene N cantidad de pesos, Camila tiene la mitad de lo que posee Juan y Ricardo tiene la mitad de lo que poseen Camila y Juan Juntos. ¿Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3?

''' def calcular_dinero(juan):
    camila = juan / 2
    ricardo = (juan + camila) / 2
    return juan, camila, ricardo

juan = float(input("Ingrese la cantidad de dinero que tiene Juan: "))

juan, camila, ricardo = calcular_dinero(juan)

print(f"Juan tiene {juan} pesos.")
print(f"Camila tiene {camila} pesos.")
print(f"Ricardo tiene {ricardo} pesos.") '''

#Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, mas una comisión de 1500000 por cada licencia de software vendida menos el (5% del salario total + comisiones de deducciones) por impuestos. Codifica un programa que calcule e imprima el salario mensual de un vendedor dado recibiendo el numero de ventas realizadas

''' def calcular_salario(num_ventas):
    salario_base = 3500000
    comision_por_venta = 1500000
    comision_total = comision_por_venta * num_ventas
    salario_total = salario_base + comision_total
    impuestos = 0.05 * salario_total
    salario_final = salario_total - impuestos
    return salario_final

num_ventas = int(input("Ingrese el número de ventas realizadas por el vendedor: "))

salario_final = calcular_salario(num_ventas)

print(f"El salario mensual del vendedor es: {salario_final:.2f} pesos.") '''

