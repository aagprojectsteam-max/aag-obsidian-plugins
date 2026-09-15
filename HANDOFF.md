# Handoff — AAG Obsidian Plugins Catalog

## Role of this repository

This repository is the public catalog/index for the AAG Obsidian plugin portfolio. It is not the source repository for the individual plugins. Its job is to point to the accepted public plugin repositories/releases and provide a machine-readable `catalog.json` that can be validated in CI.

## Publication workflow

Each plugin is developed, tested, versioned and released in its own repository. Only after that release is verified should this catalog be updated. The catalog entry must match the plugin identity, repository, version/release information expected by the validator. `scripts/validate.py` and `.github/workflows/ci.yml` protect catalog consistency.

The portfolio publication sequence used during the 2026 work was: finish engineering acceptance in the plugin repository; create/tag the public release; verify hosted CI/release assets; then update this catalog to the accepted release. This prevents the catalog from advertising an unpublished or unverified local build.

## Current portfolio context

The catalog has been used for the public AAG Obsidian plugins including DesignTweaker, SmartPaste and SideNotes. Their engineering histories belong in their own repositories, now including `docs/HANDOFF.md` files. Private/unpublished companion projects must not be added merely because they exist locally.

## Maintenance procedure

For every catalog update: verify the target repository is public and intended for distribution; verify the release/tag exists and is non-draft as intended; verify CI/publication checks in the plugin repository; update `catalog.json`; run `python scripts/validate.py`; inspect the diff for accidental private paths/data; commit; verify this repository's CI.

## Historical integrity rule

The catalog is a pointer to accepted public state, not a development diary. Do not place private plugin source, local vault information or unpublished project metadata here. Historical engineering detail belongs in the source repository and release notes.

## Current handoff status

As of 2026-09-15, this catalog has README, machine-readable catalog, validation script, CI and this handoff. The individual public plugin repositories carry their own detailed handoff documents.