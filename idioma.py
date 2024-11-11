from deep_translator import GoogleTranslator

text = input("Ingresa el texto a traducir en todos losde idiomas soportados:\n")

# Obtener los idiomas soportados
supported_languages = GoogleTranslator.get_supported_languages()

# Traducir a cada idioma
for lang in supported_languages:
    try:
        translator = GoogleTranslator(source='auto', target=lang)  # Crear un nuevo traductor para cada idioma
        translation = translator.translate(text)
        print(f"Idioma: {lang}, Traducción: {translation}")
    except Exception as e:
        print(f"Error al traducir a {lang}: {e}")
