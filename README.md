# Análisis de un grupo de WhatsApp

[![CCDS Project template](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org/)

Proyecto de análisis exploratorio de un chat de WhatsApp. La libreta principal es [`notebooks/analisis_grupo.ipynb`](notebooks/analisis_grupo.ipynb). El proyecto usa una estructura inspirada en Cookiecutter Data Science, adaptada a una sola libreta y a datos privados.

## Alcance

El análisis se centra en el historial conservado del **6 de noviembre de 2025 al 24 de septiembre de 2026**. Hay tres registros anteriores sobre la creación del grupo; no representan una serie continua desde 2022. Los remitentes aparecen con alias de los Pokémon de primera generación para evitar mostrar sus nombres en los resultados.

La libreta examina la calidad de la exportación, los tipos de mensajes, la participación, la actividad por día y hora, el vocabulario, las nubes de palabras y el contexto futbolístico de las diez fechas con más mensajes. La coincidencia entre actividad y eventos se describe sin atribuirles causalidad.

## Vista previa y estructura

GitHub muestra las celdas, tablas y figuras guardadas en [la libreta de análisis](notebooks/analisis_grupo.ipynb). Esta es la forma de consultar el proyecto: el chat y las listas de palabras no se publican, por lo que otra persona no podrá volver a calcular los resultados solo con el repositorio.

```text
mi-grupo-de-wasap/
├── README.md                       <- Descripción y guía del proyecto
├── .gitignore                      <- Archivos que no se suben a Git
├── Makefile                        <- Atajos opcionales para preparar y abrir JupyterLab
├── pyproject.toml                   <- Dependencias de Python
├── uv.lock                          <- Versiones fijadas de las dependencias
├── data/
│   ├── raw/
│   │   └── chat.txt                 <- Exportación original (solo local)
│   ├── interim/
│   │   ├── noimportantes.txt        <- Palabras excluidas (solo local)
│   │   └── altisonantes.txt         <- Palabras censuradas (solo local)
│   └── processed/                   <- Espacio para datos derivados (solo local)
├── notebooks/
│   └── analisis_grupo.ipynb         <- Análisis, visualizaciones y conclusiones
├── references/
│   ├── README.md                    <- Notas sobre fuentes y variables
│   └── siluetas/
│       ├── lickitung.png
│       ├── mewtwo.png
│       └── growlithe.png            <- Imágenes para las nubes de palabras
└── scripts/
    └── register_export.py          <- Registro opcional de la exportación original
```

Los archivos marcados «solo local» no aparecen en GitHub con la configuración actual de `.gitignore`.

## Ejecución local

Estos pasos son para quien tenga los archivos privados. Desde la carpeta del proyecto, en Git Bash o PowerShell:

```bash
uv sync
uv run python -m spacy download es_core_news_md
uv run jupyter lab
```

Además de instalar las dependencias, deben estar disponibles los tres archivos privados `data/raw/chat.txt`, `data/interim/noimportantes.txt` y `data/interim/altisonantes.txt`. Las listas usan una palabra por línea y pueden incluir comentarios que comiencen con `#`. El modelo `es_core_news_md` se instala por separado porque se utiliza para identificar adjetivos.

Abre `notebooks/analisis_grupo.ipynb` y ejecuta las celdas en orden desde un kernel nuevo. La libreta busca `data/raw/chat.txt` en la carpeta actual o en sus carpetas superiores, por lo que JupyterLab debe iniciarse desde el proyecto. En GitHub se pueden consultar las figuras y tablas guardadas; volver a ejecutar el análisis requiere los archivos privados.

## Privacidad

`.gitignore` excluye `data/raw/`, `data/interim/` y `data/processed/`. La libreta y sus salidas pueden revelar patrones del grupo incluso cuando se usan alias. Antes de publicar o compartir el repositorio, revisa `git status`, los archivos preparados para el commit y la privacidad del repositorio remoto.
