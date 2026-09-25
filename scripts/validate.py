from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
EXPECTED_REPOSITORIES = {
    "aag-design-tweaker": "aagprojectsteam-max/aag-obsidian-designtweaker",
    "aag-smart-paste": "aagprojectsteam-max/aag-obsidian-smartpaste",
    "context-aware-paragraph-notes": "aagprojectsteam-max/aag-obsidian-sidenotes",
}
REQUIRED_STRING_FIELDS = {
    "name", "id", "repository", "version", "minAppVersion",
    "description", "maintenance", "release",
}

def validate_catalog(data: object, readme_text: str) -> list[dict]:
    if not isinstance(data, dict) or set(data) != {"plugins"}:
        raise ValueError("catalog must contain only a plugins array")
    plugins = data["plugins"]
    if not isinstance(plugins, list):
        raise ValueError("plugins must be an array")
    if len(plugins) != len(EXPECTED_REPOSITORIES):
        raise ValueError("unexpected catalog entry count")

    ids: set[str] = set()
    repositories: set[str] = set()
    for index, plugin in enumerate(plugins):
        if not isinstance(plugin, dict):
            raise ValueError(f"plugin {index} must be an object")
        missing = REQUIRED_STRING_FIELDS - plugin.keys()
        extra = plugin.keys() - REQUIRED_STRING_FIELDS
        if missing or extra:
            raise ValueError(f"plugin {index} fields invalid: missing={sorted(missing)} extra={sorted(extra)}")
        for field in REQUIRED_STRING_FIELDS:
            if not isinstance(plugin[field], str) or not plugin[field].strip():
                raise ValueError(f"plugin {index} field {field} must be a non-empty string")

        plugin_id = plugin["id"]
        repository = plugin["repository"]
        if plugin_id in ids:
            raise ValueError(f"duplicate plugin id: {plugin_id}")
        if repository in repositories:
            raise ValueError(f"duplicate repository: {repository}")
        ids.add(plugin_id)
        repositories.add(repository)

        if repository != EXPECTED_REPOSITORIES.get(plugin_id):
            raise ValueError(f"repository does not match canonical id {plugin_id}")
        if not SEMVER.fullmatch(plugin["version"]):
            raise ValueError(f"invalid version for {plugin_id}")
        if not SEMVER.fullmatch(plugin["minAppVersion"]):
            raise ValueError(f"invalid minAppVersion for {plugin_id}")
        if plugin["minAppVersion"] != "1.13.7":
            raise ValueError(f"unexpected minAppVersion policy for {plugin_id}")

        expected_release = f"https://github.com/{repository}/releases/tag/{plugin['version']}"
        if plugin["release"] != expected_release:
            raise ValueError(f"release URL does not match repository/version for {plugin_id}")
        if expected_release not in readme_text:
            raise ValueError(f"README is missing release link for {plugin_id}")

    if ids != set(EXPECTED_REPOSITORIES):
        raise ValueError("catalog canonical ID set changed")
    return plugins

def load_and_validate(root: Path = ROOT) -> list[dict]:
    data = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    readme = (root / "README.md").read_text(encoding="utf-8")
    return validate_catalog(data, readme)

if __name__ == "__main__":
    plugins = load_and_validate()
    print(f"CATALOG=PASS; ENTRIES={len(plugins)}")
