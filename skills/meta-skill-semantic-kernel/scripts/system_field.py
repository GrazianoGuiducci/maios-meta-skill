"""Read-only, query-independent orientation from host-selected public-to-agent files.

Never crawl arbitrary workspace files: the host manifest identifies sources and
skill entry directories. Output is retrieval evidence, not capability activation.
"""
import argparse
import json
import re
from pathlib import Path


def read_source(path, limit):
    record = {"path": str(path)}
    try:
        body = path.read_text(encoding="utf-8-sig")
        record.update(status="read", excerpt=body[:limit],
                      omitted_characters=max(0, len(body) - limit))
        headings = re.findall(r"^#{1,3} .+$", body, flags=re.MULTILINE)
        record["outline"] = headings[:35]
        record["omitted_headings"] = max(0, len(headings) - 35)
        if path.suffix.lower() == ".json":
            try:
                document = json.loads(body)
                if isinstance(document, dict):
                    record["top_level_keys"] = list(document)
                    if isinstance(document.get("nodes"), list):
                        record["relational_nodes"] = [
                            {key: node[key] for key in ("id", "label", "kind", "definition", "source_refs") if key in node}
                            for node in document["nodes"] if isinstance(node, dict)
                        ]
            except json.JSONDecodeError:
                record["structured_status"] = "invalid_json"
    except (OSError, UnicodeError) as exc:
        record.update(status="unavailable", reason=type(exc).__name__)
    return record


def collect(root, manifest, excerpt_chars=1400):
    result = {
        "coverage": "Only configured sources and immediate skill entries; not the whole system.",
        "interpretation": "Read excerpts as source claims. Follow owner sources; absence is not impossibility.",
        "sources": [], "competences": [], "gaps": [],
    }
    for item in manifest.get("sources", []):
        record = read_source((root / item["path"]).resolve(), excerpt_chars)
        record["function"] = item["function"]
        result["sources"].append(record)
    for relative in manifest.get("skill_roots", []):
        directory = (root / relative).resolve()
        if not directory.is_dir():
            result["gaps"].append({"path": str(directory), "reason": "missing_skill_root"})
            continue
        for path in sorted(directory.glob("*/SKILL.md")):
            record = read_source(path, 1600)
            excerpt = record.pop("excerpt", "")
            # Retain frontmatter, including multiline descriptions, without a YAML dependency.
            if excerpt.startswith("---") and "\n---" in excerpt[3:]:
                metadata = excerpt.split("\n---", 1)[0][3:].strip()
                record["entry_metadata"] = metadata
                record["entry_metadata_complete"] = True
            else:
                record["entry_excerpt"] = excerpt
                record["entry_metadata_complete"] = False
            result["competences"].append(record)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--excerpt-chars", type=int, default=1400)
    args = parser.parse_args()
    if args.excerpt_chars < 1:
        parser.error("--excerpt-chars must be positive")
    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    print(json.dumps(collect(args.workspace.resolve(), manifest, args.excerpt_chars),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
