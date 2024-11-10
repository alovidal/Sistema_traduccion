# Sistema de Traducción de PDFs

Este proyecto permite traducir el contenido de un archivo PDF de un idioma a otro, utilizando la API de Google Translate para realizar la traducción. Los archivos PDF se extraen, se traducen y luego se guardan como nuevos archivos PDF con el contenido traducido.

## Requisitos

- Python 3.x
- Librerías:
  - `PyMuPDF` para extraer el contenido del PDF.
  - `deep_translator` para realizar la traducción.
  - `reportlab` para generar archivos PDF.

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
Ingresa la ruta del PDF:
C:/ruta/archivo.pdf
Ingresa el idioma de destino ('es' para español, 'en' para inglés):
es
```


