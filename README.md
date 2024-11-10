# Sistema de Traducción de PDFs

Este proyecto permite traducir el contenido de un archivo PDF de un idioma a otro, utilizando la API de Google Translate para realizar la traducción. Los archivos PDF se extraen, se traducen y luego se guardan como nuevos archivos PDF con el contenido traducido.

## Requisitos

- Python 3.x
- Librerías:
  - `PyPDF2` para la extracción de texto de PDFs.
  - `googletrans` para la traducción automática del texto.
  - `fpdf` para generar archivos PDF.

Puedes instalar las dependencias usando `pip`:

```bash
pip install PyPDF2 googletrans fpdf

