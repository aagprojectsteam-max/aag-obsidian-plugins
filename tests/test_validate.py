from copy import deepcopy
from pathlib import Path
import importlib.util
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog_validate", ROOT / "scripts" / "validate.py")
validate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate)
BASE = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
README = (ROOT / "README.md").read_text(encoding="utf-8")

class CatalogValidationTests(unittest.TestCase):
    def test_current_catalog(self):
        self.assertEqual(len(validate.validate_catalog(deepcopy(BASE), README)), 3)

    def assert_invalid(self, mutate):
        data = deepcopy(BASE)
        mutate(data)
        with self.assertRaises(ValueError):
            validate.validate_catalog(data, README)

    def test_wrong_release_url_is_rejected(self):
        self.assert_invalid(lambda data: data["plugins"][0].update(release="https://example.invalid/release"))

    def test_repository_for_another_plugin_is_rejected(self):
        self.assert_invalid(lambda data: data["plugins"][0].update(repository=data["plugins"][1]["repository"]))

    def test_duplicate_id_is_rejected(self):
        self.assert_invalid(lambda data: data["plugins"][1].update(id=data["plugins"][0]["id"]))

    def test_missing_required_field_is_rejected(self):
        self.assert_invalid(lambda data: data["plugins"][0].pop("description"))

    def test_unknown_field_is_rejected(self):
        self.assert_invalid(lambda data: data["plugins"][0].update(unexpected="x"))

    def test_invalid_semver_is_rejected(self):
        self.assert_invalid(lambda data: data["plugins"][0].update(version="1.2"))

    def test_policy_minimum_is_rejected_when_changed_silently(self):
        self.assert_invalid(lambda data: data["plugins"][0].update(minAppVersion="1.5.0"))

    def test_readme_must_contain_exact_release_link(self):
        with self.assertRaises(ValueError):
            validate.validate_catalog(deepcopy(BASE), README.replace(BASE["plugins"][0]["release"], ""))

if __name__ == "__main__":
    unittest.main()
