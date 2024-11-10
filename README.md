# Sistema de Traducción de PDFs

Este proyecto permite traducir el contenido de un archivo PDF de un idioma a otro, utilizando la API de Google Translate para realizar la traducción. Los archivos PDF se extraen, se traducen y luego se guardan como nuevos archivos PDF con el contenido traducido.

## Requisitos

- Python 3.x
- Librerías:
  - `PyMuPDF` para extraer el contenido del PDF.
  - `deep_translator` para realizar la traducción.
  - `reportlab` para generar archivos PDF.
  - `tqdm` para mostrar la barra de progreso.

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
Ingresa el idioma de destino:
af, sq, de, am, ar, hy, az, bn, bg, ca, ceb, cs, zh-CN, zh-TW, ht, hr, da, nl, en, et, tl, fi, fr, gl, ka,
de-CH, el, gu, ht, he, hu, id, is, it, ja, jw, kn, kk, km, ko, ku, lo, lv, lt, mk, ms, ml, mr, mn, ne, no,
ps, fa, pl, pt, ro, ru, sr, sd, so, sw, sv, ta, te, th, tr, uk, ur, vi, cy, yi, zu
```


