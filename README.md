# Sistema de Traducción de PDFs

Este proyecto permite traducir el contenido de un archivo PDF de un idioma a otro, utilizando la API de Google Translate para realizar la traducción. Los archivos PDF se extraen, se traducen y luego se guardan como nuevos archivos PDF con el contenido traducido.

## Requisitos

- Python 3.x
- Librerías:
  - `PyPDF2` para la extracción de texto de PDFs.
  - `googletrans` para la traducción automática del texto.
  - `fpdf` para generar archivos PDF.

## Intalacion
```bash
git clone https://github.com/alovidal/Sistema_traduccion.git
```

Puedes instalar las librerias usando `pip`:

```bash
pip install -r requerimientos.txt
```
## Uso

```bash
python tra_pdf.py
```
```bash
Ingresa la ruta del PDF en inglés:
C:/Users/alons/Downloads/HTB-Fawn.pdf
Ingresa el idioma de destino ('es' para español, 'en' para inglés):
es
```
