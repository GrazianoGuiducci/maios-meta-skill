"""Package a selected competence without private infrastructure or dependencies."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]


def build():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    packages = []
    for resource in catalog["resources"]:
        folder = (ROOT / resource["skill"]).parent
        destination = ROOT / resource["package"]
        destination.parent.mkdir(exist_ok=True)
        sources = sorted(path for path in folder.rglob("*") if path.is_file())
        files = {}
        with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
            for source in sources:
                name = resource["id"] + "/" + source.relative_to(folder).as_posix()
                content = source.read_bytes()
                entry = ZipInfo(name, date_time=(2026, 10, 19, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o644 << 16
                archive.writestr(entry, content)
                files[name] = hashlib.sha256(content).hexdigest()
        packages.append({
            "id": resource["id"],
            "version": resource["version"],
            "package": resource["package"],
            "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
            "files": files,
        })
    manifest = {"schema_version": 1, "packages": packages}
    (ROOT / "dist/manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps([{"id": p["id"], "version": p["version"],
                      "files": len(p["files"]), "sha256": p["sha256"]}
                     for p in packages]))


if __name__ == "__main__":
    build()
