"""Contract checks for the frugal-coordinator skill package.

The repository ships an installable skill: SKILL.md frontmatter plus the
assets/, references/ and templates its documents link to. These tests fail
when that contract breaks (malformed frontmatter, missing required file,
relative link that no longer resolves).
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)")


def package_docs():
    docs = sorted(ROOT.rglob("*.md"))
    template = ROOT / "assets" / "CLAUDE.md.template"
    if template.is_file():
        docs.append(template)
    return docs


class SkillPackageTest(unittest.TestCase):
    def test_required_files_exist_and_are_nonempty(self):
        for rel in ("SKILL.md", "README.md", "LICENSE"):
            path = ROOT / rel
            self.assertTrue(path.is_file(), rel)
            self.assertGreater(path.stat().st_size, 0, rel)

    def test_skill_frontmatter_has_name_and_description(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(
            text.startswith("---\n"), "SKILL.md must open with YAML frontmatter"
        )
        frontmatter = text.split("---\n", 2)[1]
        fields = {
            line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip()
            for line in frontmatter.strip().splitlines()
            if ":" in line
        }
        self.assertEqual(fields.get("name"), "frugal-coordinator")
        self.assertTrue(fields.get("description"), "frontmatter description")

    def test_relative_links_resolve(self):
        broken = []
        for doc in package_docs():
            for target in MD_LINK.findall(doc.read_text(encoding="utf-8")):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                path = target.split("#", 1)[0]
                if path and not (doc.parent / path).resolve().exists():
                    broken.append(f"{doc.relative_to(ROOT)} -> {target}")
        self.assertEqual(broken, [])

    def test_referenced_directories_exist(self):
        for rel in ("assets", "references"):
            self.assertTrue((ROOT / rel).is_dir(), rel)


if __name__ == "__main__":
    unittest.main()
