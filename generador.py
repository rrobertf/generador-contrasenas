"""Generador interactivo: muestra la contraseña sin guardarla en disco."""
import secrets
import string


def generar_contrasena(longitud: int, usar_numeros: bool = True,
                       usar_simbolos: bool = True) -> str:
    if isinstance(longitud, bool) or not isinstance(longitud, int) or not 8 <= longitud <= 4096:
        raise ValueError('La longitud debe estar entre 8 y 4096.')
    grupos = [string.ascii_lowercase, string.ascii_uppercase]
    if usar_numeros:
        grupos.append(string.digits)
    if usar_simbolos:
        grupos.append(string.punctuation)
    pool = ''.join(grupos)
    # Rejection sampling keeps the distribution uniform over valid passwords.
    while True:
        contrasena = ''.join(secrets.choice(pool) for _ in range(longitud))
        if all(any(c in grupo for c in contrasena) for grupo in grupos):
            return contrasena


def main() -> None:
    print('=== Generador de Contraseñas Seguras ===\n')
    try:
        while True:
            try:
                longitud = int(input('¿Qué tan larga quieres la contraseña? (8–4096): '))
            except ValueError:
                print('Ingresa un número entero.')
                continue
            if longitud < 8:
                print('Muy corta. Se usará 8 como mínimo.')
                longitud = 8
            if longitud <= 4096:
                break
            print('El máximo es 4096.')
        usar_numeros = input('¿Incluir números? (s/n): ').strip().lower() == 's'
        usar_simbolos = input('¿Incluir símbolos? (s/n): ').strip().lower() == 's'
        print(f'\nTu contraseña: {generar_contrasena(longitud, usar_numeros, usar_simbolos)}')
        print('No se guardó en disco. Guárdala en tu gestor de contraseñas.')
    except (EOFError, KeyboardInterrupt):
        print('\nCancelado.')


if __name__ == '__main__':
    main()
