import random
import string

print("=" * 45)
print("  🔐 GENERADOR DE CONTRASEÑAS SEGURAS 🔐  ")
print("=" * 45)

# 1. Le pedimos al usuario la longitud de la contraseña
longitud = int(input("¿Cuántos caracteres quieres que tenga tu contraseña?: "))

# 2. Definimos los componentes de una contraseña segura
letras = string.ascii_letters  # abc...ABC...
numeros = string.digits        # 0123456789
simbolos = string.punctuation  # !@#$...

# Combinamos todos los caracteres disponibles
todos_los_caracteres = letras + numeros + simbolos

# 3. Mezclamos los caracteres al azar para crear la contraseña
contrasena_lista = [random.choice(todos_los_caracteres) for _ in range(longitud)]
contrasena_final = "".join(contrasena_lista)

# 4. Mostramos el resultado profesional en pantalla
print("\n" + "-" * 45)
print(f"✔️ ¡Contraseña generada con éxito!")
print(f"👉 Tu nueva contraseña es: {contrasena_final}")
print("-" * 45)
print("¡Cópiala y guárdala en un lugar seguro!")

