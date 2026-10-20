"""Retrieval contracts: preserve unknowns and expose entries beyond the excerpt."""
import tempfile
import unittest
from pathlib import Path

from system_field import collect


class RetrievalTests(unittest.TestCase):
    def test_missing_source_is_reported_without_losing_other_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "known.md").write_text("# Existing source", encoding="utf-8")
            view = collect(root, {"sources": [
                {"function": "unknown", "path": "missing.md"},
                {"function": "known", "path": "known.md"}],
                "skill_roots": ["missing-skills"]})
            self.assertEqual([s["status"] for s in view["sources"]], ["unavailable", "read"])
            self.assertEqual(view["gaps"][0]["reason"], "missing_skill_root")

    def test_new_skill_is_discovered_without_topic_or_known_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "skills" / "unexpected-capacity"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: unexpected-capacity\ndescription: |\n  An unrelated useful function.\n---\nBody",
                encoding="utf-8")
            view = collect(root, {"skill_roots": ["skills"]})
            self.assertIn("An unrelated useful function", view["competences"][0]["entry_metadata"])
            self.assertTrue(view["competences"][0]["entry_metadata_complete"])

    def test_truncation_keeps_late_structure_visible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source.md").write_text("x" * 5000 + "\n## Hidden relation\n", encoding="utf-8")
            view = collect(root, {"sources": [{"function": "orientation", "path": "source.md"}]}, 20)
            source = view["sources"][0]
            self.assertGreater(source["omitted_characters"], 0)
            self.assertIn("## Hidden relation", source["outline"])


if __name__ == "__main__":
    unittest.main()
