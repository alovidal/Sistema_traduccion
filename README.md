# Proyecto de Traducción de PDFs

Este proyecto permite extraer texto de un archivo PDF y traducirlo a un idioma diferente utilizando Google Translator, y luego crear un nuevo archivo PDF con el texto traducido. Además, incluye una barra de progreso para mostrar el estado de la creación del PDF.

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
Asegúrate de tener un archivo PDF del cual deseas extraer el contenido y traducirlo.
Ejecuta el script en tu terminal con el siguiente comando:

```bash
python tra_pdf.py
```

Ingresa la ruta del PDF y el idioma al que se traducira. Espera a que el script complete el proceso: El script mostrará una barra de progreso durante la creación del nuevo PDF.
Después de completar el proceso, se generará un nuevo archivo PDF con el contenido traducido. El archivo se guardará con el nombre nombre_original_del_pdf - idioma.pdf.

### Ejemplo

```bash
python tra_pdf.py
```

```bash
Ingresa la ruta del PDF:
/ruta/de/tu/archivo.pdf
Ingresa el idioma de destino:
af, sq, de, am, ar, hy, az, bn, bg, ca, ceb, cs, zh-CN, zh-TW, ht, hr, da, nl, en, et, tl, fi, fr, gl, ka,
de-CH, el, gu, ht, he, hu, id, is, it, ja, jw, kn, kk, km, ko, ku, lo, lv, lt, mk, ms, ml, mr, mn, ne, no,
ps, fa, pl, pt, ro, ru, sr, sd, so, sw, sv, ta, te, th, tr, uk, ur, vi, cy, yi, zu
```

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## Notas

Este proyecto utiliza la API de Google Translator a través de la biblioteca deep-translator, lo que significa que necesitarás una conexión a Internet para realizar la traducción.
La barra de progreso mostrada en la terminal indica el avance de la traducción y la creación del archivo PDF.

### Instrucciones para usar el README:
1. **Instalación de dependencias**: El archivo `README.md` explica cómo instalar las dependencias necesarias para ejecutar el script.
2. **Ejecución**: Describe cómo ejecutar el script y qué entrada se espera del usuario.
3. **Licencia y contribuciones**: Se menciona la licencia (MIT) y cómo contribuir al proyecto.


