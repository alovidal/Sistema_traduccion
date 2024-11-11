import fitz  # PyMuPDF
import os
import re
from deep_translator import GoogleTranslator
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from tqdm import tqdm


# Extraer texto y formato del PDF
def extraer_texto_y_formato(ruta_pdf):
    documento = fitz.open(ruta_pdf)
    contenido = []

    for pagina in documento:
        bloques = pagina.get_text("dict")["blocks"]
        for bloque in bloques:
            if "lines" in bloque:
                for linea in bloque["lines"]:
                    texto_linea = ""
                    estilo_linea = {
                        "font": "",
                        "size": 12,
                        "bold": False,
                        "italic": False
                    }
                    for span in linea["spans"]:
                        texto_linea += span["text"]
                        estilo_linea["font"] = span["font"]
                        estilo_linea["size"] = span["size"]
                        estilo_linea["bold"] = "Bold" in span["font"]
                        estilo_linea["italic"] = "Italic" in span["font"]

                    contenido.append((texto_linea.strip(), estilo_linea))

    documento.close()
    return contenido


# Dividir texto
def dividir_texto(texto, max_length=3000):
    texto = re.sub(r'\s+', ' ', texto).strip()
    partes = []

    while len(texto) > max_length:
        corte = texto[:max_length].rfind('.')
        if corte == -1:
            corte = max_length
        partes.append(texto[:corte + 1].strip())
        texto = texto[corte + 1:].strip()

    if texto:
        partes.append(texto)

    return partes


# Traducir el texto
def traducir_contenido(contenido, destino):
    traductor = GoogleTranslator(source='auto', target=destino)
    contenido_traducido = []
    total_parrafos = len(contenido)

    # Usamos tqdm para mostrar la barra de progreso mientras traducimos
    for idx, (texto, estilo) in enumerate(tqdm(contenido, desc="Creando PDF", total=total_parrafos, unit="parrafo")):
        partes = dividir_texto(texto)
        texto_traducido = ""
        for parte in partes:
            try:
                texto_traducido += traductor.translate(parte) + "\n"
            except Exception as e:
                print(f"Error al traducir una parte: {e}")
                texto_traducido += parte

        contenido_traducido.append((texto_traducido.strip(), estilo))

    return contenido_traducido


# Crear PDF con formato
def crear_pdf_con_formato(contenido, nombre_pdf):
    doc = SimpleDocTemplate(nombre_pdf, pagesize=A4, rightMargin=72,
                            leftMargin=72, topMargin=72, bottomMargin=18)
    estilos = getSampleStyleSheet()

    elementos = []

    for texto, estilo in contenido:
        estilo_parrafo = ParagraphStyle(
            'Custom',
            fontName='Helvetica-Bold' if estilo["bold"] else 'Helvetica-Oblique' if estilo["italic"] else 'Helvetica',
            fontSize=estilo["size"],
            leading=estilo["size"] + 2
        )
        elementos.append(Paragraph(texto, estilo_parrafo))
        elementos.append(Spacer(1, 12))

    doc.build(elementos)
    print(f"PDF traducido creado: {nombre_pdf}")

# Ejecutar
if __name__ == "__main__":
    ruta_pdf = input("Ingresa la ruta del PDF:\n")
    destino = input("Ingresa el idioma de destino:\n").lower()

    contenido = extraer_texto_y_formato(ruta_pdf)
    if not contenido:
        print("No se pudo extraer contenido del PDF.")
    else:
        contenido_traducido = traducir_contenido(contenido, destino)
        nombre_base = os.path.splitext(os.path.basename(ruta_pdf))[0]
        nombre_pdf_traducido = f"{nombre_base} - {destino}.pdf"

        crear_pdf_con_formato(contenido_traducido,
                              nombre_pdf=nombre_pdf_traducido)
