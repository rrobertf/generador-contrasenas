# Generador de Contraseñas

CLI interactiva en Python 3.10+ sin dependencias externas.

```bash
python3 generador.py
python3 -m unittest discover -s tests -v
```

Elige longitud (8–4096), números y símbolos. Usa `secrets` para aleatoriedad criptográfica y garantiza minúsculas, mayúsculas y cada categoría seleccionada. Una longitud inferior a 8 se ajusta a 8; las entradas no numéricas se vuelven a solicitar.

La contraseña se muestra en la terminal **sin guardarse automáticamente**. Esto elimina el historial en texto plano de versiones anteriores. Los archivos `contrasenas.txt` que ya tengas se conservan sin cambios y quedan ignorados por Git: tras trasladar tus claves a un gestor de contraseñas, decide cómo custodiar o eliminar ese historial. Evita grabar o compartir la terminal cuando muestre contraseñas.

No incluye flags CLI, cálculo de entropía, generación por lotes ni portapapeles.

**Roberto Feliciano** — [GitHub](https://github.com/rrobertf)
