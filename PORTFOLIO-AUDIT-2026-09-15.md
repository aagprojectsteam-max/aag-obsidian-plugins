# AAG GitHub Portfolio Documentation Audit — 2026-09-15

## Scope

Authenticated portfolio review covered all 15 repositories visible under `aagprojectsteam-max` on 2026-09-15. The primary audit goal was durable engineering handoff documentation: origin/problem, architecture, failed approaches, fixes, installation, testing/evidence, limitations, rollback/maintenance and publication context.

## Repository status

| Repository | Type | Handoff status after audit | Notes |
|---|---|---|---|
| canon-eos-4000d-linux-tether | AAG project | ADDED `docs/HANDOFF.md` | Existing README, findings, architecture, install, troubleshooting, source integrity, CI/release/tests retained. |
| iriscan-express4-linux | AAG project | ADDED `docs/HANDOFF.md` | Explicitly separates practical WinBoat solution from unfinished native C3 research. |
| AAG-AnythingLLM-Suite | AAG project | ADDED `HANDOFF.md` | Master index added because repository already contained extensive final/audit/inventory evidence. |
| fibocom-fm350-t700-gnss-linux | AAG project | ADDED `HANDOFF.md` | Connects port discovery, t7xx, userspace bridge, gpsd, resume, browser and rollback layers. |
| flutter_inappwebview | upstream fork | ADDED `AAG-FORK-HANDOFF.md` | Documents upstream-contribution purpose; not presented as AAG product. |
| otzaria | upstream fork | ADDED `AAG-FORK-HANDOFF.md` | Documents coordinated Linux upstream contribution and PR relationship. |
| aag-external-storage-safe-suspend-linux | AAG project | ADDED `docs/HANDOFF.md` | Connects suspend/hibernate, failures, fail-safe, acceptance and publication evidence. |
| intel-core-ultra-llama-linux | AAG project | ADDED `docs/HANDOFF.md` | Preserves benchmark/profile rationale and evidence boundary. |
| aag-obsidian-designtweaker | AAG plugin | ADDED `docs/HANDOFF.md` | Maintenance/publication/visual-validation model. |
| aag-obsidian-smartpaste | AAG plugin | ADDED `docs/HANDOFF.md` | Exact-block identity/navigation and integration history. |
| aag-obsidian-plugins | catalog | ADDED `HANDOFF.md` | Catalog-specific publication workflow; this audit is also stored here. |
| aag-obsidian-sidenotes | AAG plugin | ADDED `docs/HANDOFF.md` | Identity, migration, transaction and recovery maintenance story. |
| aag-hotspot-control | AAG project | ADDED `docs/HANDOFF.md` | Separates mock/staging evidence from real hardware/client claims. |
| aag-book2pdf | AAG project | ADDED `HANDOFF.md` | Decode-before-salvage, format/recovery architecture and evidence gaps. |
| aag-fm350-esim-linux | AAG project | EXISTING `docs/HANDOFF.md` | Already had a substantial long-form handoff plus architecture, safety and troubleshooting. |

## Portfolio-wide standard adopted

Every original AAG project should have a discoverable long-form handoff. The handoff should answer: why the project started; hardware/software environment where relevant; chronological investigation; failed hypotheses/approaches; root causes; accepted architecture; exact operational/install/remove path; tests and what they do/do not prove; release/publication state; known limitations; privacy/security/legal boundaries; rollback/recovery; repository map; maintenance/release procedure; and a historical-integrity rule preventing later success from erasing earlier evidence.

Forks are different: their handoff must explain why the fork exists, the AAG patch scope, upstream PR relationship, validation and synchronization/retirement strategy. They must not be presented as AAG-authored products.

## Evidence rules

1. Never convert mock/unit/CI success into a physical-hardware claim.
2. Never convert “application opened” into exact workflow acceptance when the requirement is more specific.
3. Preserve failed experiments when they explain current architecture.
4. Mark unsupported/unverified states explicitly instead of guessing.
5. Do not publish private hardware IDs, coordinates, credentials, private documents, vault/database contents or copyrighted test samples merely to make a public handoff look complete.
6. Keep release/tag/asset verification separate from runtime acceptance.
7. Keep old version-specific verification reports as historical evidence.

## Remaining recurring obligations

This audit establishes the documentation baseline; it does not freeze the repositories. On every future material release, update the relevant HANDOFF, CHANGELOG/release notes, validation/acceptance evidence and support boundary. Re-run CI/publication checks after documentation changes and ensure new handoff files are included in any publication/file-allowlist logic where such allowlists exist.

## Audit conclusion

All 15 visible repositories now have either a project handoff, a fork-specific handoff, or (for the eSIM repository) a pre-existing substantial handoff. The portfolio no longer relies solely on transient chat/development context to explain why the current implementations exist.