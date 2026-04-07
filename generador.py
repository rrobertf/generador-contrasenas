import random
import string
import datetime

# ── 1. Definir los caracteres disponibles ──
letras = string.ascii_letters      # a-z y A-Z
numeros = string.digits            # 0-9
simbolos = string.punctuation      # !@#$%^&*...

# ── 2. Preguntar al usuario ──
print("=== Generador de Contraseñas Seguras ===\n")

longitud = int(input("¿Qué tan larga quieres la contraseña? (mínimo 8): "))

if longitud < 8:
    print("Muy corta. Se usará 8 como mínimo.")
    longitud = 8

usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

# ── 3. Construir el pool de caracteres ──
pool = letras

if usar_numeros:
    pool += numeros

if usar_simbolos:
    pool += simbolos

# ── 4. Generar la contraseña ──
contrasena = ''.join(random.choice(pool) for _ in range(longitud))

# ── 5. Mostrar resultado ──
print(f"\nTu contraseña: {contrasena}")

# ── 6. Guardar en archivo ──
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("contrasenas.txt", "a") as archivo:
    archivo.write(f"{fecha} | Longitud: {longitud} | {contrasena}\n")

print("✓ Guardada en contrasenas.txt")