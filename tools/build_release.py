"""Package a selected competence without private infrastructure or dependencies."""
import hashlib
import json
import argparse
import subprocess
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]


def build(selected=None, source_ref=None):
    def read(path):
        if source_ref:
            return subprocess.check_output(['git','-C',str(ROOT),'show',source_ref+':'+path])
        return (ROOT/path).read_bytes()
    catalog = json.loads(read('catalog.json'))
    previous_path = ROOT / 'dist/manifest.json'
    previous = json.loads(previous_path.read_text(encoding='utf-8')) if previous_path.exists() else {'packages': []}
    known = {item['id']: item for item in previous['packages']}
    ids = {resource['id'] for resource in catalog['resources']}
    if selected and not set(selected) <= ids:
        raise ValueError('Unknown resource in selected release')
    packages = []
    for resource in catalog["resources"]:
        if selected and resource['id'] not in selected:
            if resource['id'] not in known:
                raise ValueError('Missing previous package: ' + resource['id'])
            packages.append(known[resource['id']])
            continue
        folder = (ROOT / resource["skill"]).parent
        destination = ROOT / resource["package"]
        destination.parent.mkdir(exist_ok=True)
        if source_ref:
            sources = sorted(subprocess.check_output(['git','-C',str(ROOT),'ls-tree','-r','--name-only',source_ref,'--',folder.relative_to(ROOT).as_posix()],text=True).splitlines())
        else:
            sources = sorted(path.relative_to(ROOT).as_posix() for path in folder.rglob('*') if path.is_file())
        files = {}
        with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
            for source in sources:
                name = resource["id"] + "/" + Path(source).relative_to(folder.relative_to(ROOT)).as_posix()
                content = read(source)
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
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps([{"id": p["id"], "version": p["version"],
                      "files": len(p["files"]), "sha256": p["sha256"]}
                     for p in packages]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--resource', action='append', help='Build only selected resources; retain other published packages')
    parser.add_argument('--source-ref', help='Package one selected Git commit or tree, excluding unrelated working changes')
    args = parser.parse_args()
    build(args.resource,args.source_ref)
