import pdfplumber # Utilizado para extraer texto de PDF
import os # Utilizado para obtener el nombre del archivo PDF original
from deep_translator import GoogleTranslator # Utilizado para traducir texto
from fpdf import FPDF # Utilizado para crear PDF

# Funciones para extraer y traducir texto de PDF
def extraer_texto_pdf(ruta_pdf):
    texto = ""
    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"
    return texto

# Funciones para dividir y traducir texto
def dividir_texto(texto, max_length=4000):
    partes = []
    while len(texto) > max_length:
        corte = texto[:max_length].rfind('.')
        if corte == -1:
            corte = max_length
        partes.append(texto[:corte + 1])
        texto = texto[corte + 1:]
    partes.append(texto)
    return partes

# Funciones para extraer y traducir texto
def traducir_texto(texto, destino='es'): # destino puede ser 'es' o 'en' dependiendo del idioma del PDF
    traductor = GoogleTranslator(source='auto', target=destino)
    partes = dividir_texto(texto)
    texto_traducido = ""
    for parte in partes:
        try:
            texto_traducido += traductor.translate(parte) + "\n"
        except Exception as e:
            print("Error al traducir una parte:", e)
    return texto_traducido

# Funciones para crear PDF
def crear_pdf(texto, nombre_pdf='traduccion.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    lineas = texto.split('\n')
    for linea in lineas:
        pdf.multi_cell(0, 10, linea)

    pdf.output(nombre_pdf)
    print(f"PDF creado: {nombre_pdf}")


if __name__ == "__main__":
    ruta_pdf = input("Ingresa la ruta del PDF en inglés:\n")
    idioma_destino = input("Ingresa el idioma de destino ('es' para español, 'en' para inglés):\n").lower()

    texto_extraido = extraer_texto_pdf(ruta_pdf)
    if not texto_extraido.strip():
        print("No se pudo extraer texto del PDF o el texto está en blanco.")
    else:
        print("\nTexto extraído del PDF:")
        print(texto_extraido[:500], "...")

        texto_traducido = traducir_texto(texto_extraido, destino=idioma_destino)
        if texto_traducido.strip():
            print("\nTexto traducido:")
            print(texto_traducido[:500], "...")

            # Obtener el nombre del archivo PDF original sin la extensión
            nombre_base = os.path.splitext(os.path.basename(ruta_pdf))[0]

            # Generar el nuevo nombre del PDF basado en el idioma
            if idioma_destino == 'es':
                nuevo_nombre_pdf = f"{nombre_base} - Español.pdf"
            elif idioma_destino == 'en':
                nuevo_nombre_pdf = f"{nombre_base} - Inglés.pdf"
            else:
                nuevo_nombre_pdf = f"{nombre_base} - Traducción.pdf"

            crear_pdf(texto_traducido, nombre_pdf=nuevo_nombre_pdf)
        else:
            print("No se pudo traducir el texto.")

