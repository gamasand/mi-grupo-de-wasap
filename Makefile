.PHONY: help setup lab register-raw

help:
	@echo "setup         Instala el entorno con uv"
	@echo "lab           Abre JupyterLab"
	@echo "register-raw  Copia una exportacion sin alterarla: make register-raw FILE=ruta PLATFORM=whatsapp"

setup:
	uv sync

lab:
	uv run jupyter lab

register-raw:
	uv run python scripts/register_export.py "$(FILE)" --platform "$(PLATFORM)"
