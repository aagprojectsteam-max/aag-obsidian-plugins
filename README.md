# AAG Obsidian plugins

The catalog of publicly released AAG Obsidian plugins. Each entry links to verified, installable release assets.

| Plugin | Latest verified release | Minimum Obsidian |
|---|---|---|
| [Design Tweaker](https://github.com/aagprojectsteam-max/aag-obsidian-designtweaker) | [1.1.11](https://github.com/aagprojectsteam-max/aag-obsidian-designtweaker/releases/tag/1.1.11) | 1.13.7 |
| [Smart Paste](https://github.com/aagprojectsteam-max/aag-obsidian-smartpaste) | [0.5.1](https://github.com/aagprojectsteam-max/aag-obsidian-smartpaste/releases/tag/0.5.1) | 1.13.7 |

Design Tweaker controls explorer, tab, note and other UI appearance. Smart Paste provides formatting commands, precise location links and location-point removal. Each repository contains its own documentation, source, license and release assets.

For manual installation, use the release's individual main.js, manifest.json and styles.css files in `.obsidian/plugins/<plugin-id>/`, then enable the plugin in Obsidian. For BRAT, enter the repository identifier shown in catalog.json and follow BRAT's installation flow. Repository/release discovery and artifact checks passed; an actual BRAT GUI installation/update test remains pending.

These projects have not been submitted to the official Community directory in this work session. Unreleased/private portfolio projects are not catalog entries. Never download an internal development tree as a substitute for a release.

Validate the local catalog with `python3 scripts/validate.py`. No network access or dependency installation is required by that check.

## Maintenance

Both listed plugins are maintained by AAG. Report reproducible problems through each repository's Issues page. Release versions are recorded in `catalog.json`; update its entry and the table together after verifying a new release.
