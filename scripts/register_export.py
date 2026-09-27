"""Copia una exportación de chat a data/raw/ y registra su procedencia."""

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def sha256_file(path: Path) -> str:
    """Calcula la huella del archivo por bloques para no cargarlo entero."""
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    # Lee la ruta y la plataforma indicadas por la persona usuaria.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Ruta de la exportación original")
    parser.add_argument("--platform", choices=("whatsapp", "telegram"), required=True)
    args = parser.parse_args()

    source = args.file.expanduser().resolve()
    if not source.is_file():
        parser.error(f"No existe el archivo: {source}")

    # Conserva una copia idéntica y evita sobrescribir datos previos.
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    destination = RAW_DIR / source.name
    if destination.exists():
        parser.error(f"Ya existe en data/raw/: {destination.name}")
    if source == destination:
        parser.error("El archivo ya está en data/raw/; no se volverá a copiar")

    source_hash = sha256_file(source)
    shutil.copy2(source, destination)
    copy_hash = sha256_file(destination)
    if source_hash != copy_hash:
        destination.unlink()
        raise RuntimeError("La copia no coincide con el archivo original")

    # Registra la procedencia local sin publicar nombres privados en Git.
    metadata_path = RAW_DIR / "source.json"
    records = []
    if metadata_path.exists():
        records = json.loads(metadata_path.read_text(encoding="utf-8"))
    records.append(
        {
            "platform": args.platform,
            "filename": destination.name,
            "registered_at_utc": datetime.now(timezone.utc).isoformat(),
            "downloaded_at": datetime.now(timezone.utc).date().isoformat(),
            "sha256": copy_hash,
        }
    )
    metadata_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Registrado: {destination.relative_to(PROJECT_ROOT)}")
    print(f"SHA-256: {copy_hash}")
    print("Si la fecha de descarga difiere, complétala en data/raw/source.json.")


if __name__ == "__main__":
    main()
