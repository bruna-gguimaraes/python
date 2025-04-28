def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def menu():
    print("Escolha a opção de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")

def main():
    menu()
    
    escolha = int(input("Digite o número da opção desejada: "))
    temperatura = float(input("Digite a temperatura: "))
    
    if escolha == 1:
        print(f"{temperatura}°C é igual a {celsius_para_fahrenheit(temperatura)}°F")
    elif escolha == 2:
        print(f"{temperatura}°C é igual a {celsius_para_kelvin(temperatura)} K")
    elif escolha == 3:
        print(f"{temperatura}°F é igual a {fahrenheit_para_celsius(temperatura)}°C")
    elif escolha == 4:
        print(f"{temperatura}°F é igual a {fahrenheit_para_kelvin(temperatura)} K")
    elif escolha == 5:
        print(f"{temperatura} K é igual a {kelvin_para_celsius(temperatura)}°C")
    elif escolha == 6:
        print(f"{temperatura} K é igual a {kelvin_para_fahrenheit(temperatura)}°F")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
