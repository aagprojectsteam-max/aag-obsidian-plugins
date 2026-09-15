# AAG GitHub Portfolio Documentation Audit — 2026-09-15

## Scope

The original authenticated review covered all 15 repositories then visible under `aagprojectsteam-max`. That repository-only scope is no longer considered sufficient. The authoritative portfolio audit now reconciles four evidence classes: visible GitHub repositories, prior engineering history, retained handoff/evidence documents, and live Ubuntu/Windows project inventories when available.

The goal is durable engineering continuity: every material AAG engineering effort must be classified as an AAG repository, an upstream contribution/fork, a private/non-publishable project with an explicit reason, or an unverified candidate awaiting source capture. Nothing should disappear merely because it was never published as a standalone repository.

## Host environment convention

Where relevant, handoffs must state that the principal development workstation is a single physical dual-boot machine with Ubuntu 26.04 LTS and Windows 11 Pro. OS-specific validation must say which boot environment was actually used. CI, VM/WinBoat validation and physical-host validation must remain distinct; cross-platform support must never be inferred merely from dual boot.

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

## Reconciliation backlog discovered outside the original 15 repositories

These are material engineering efforts evidenced outside the original repository list. They must not be silently treated as published or complete. Source capture and publication/privacy review come before creating public repositories.

| Candidate / workstream | Evidence/status | Required portfolio action |
|---|---|---|
| AAG USB Clone / Dummy USB / `dummy_hcd` | Substantial Ubuntu + Windows/WinBoat engineering; Kingston profile, kernel-specific `dummy_hcd`, self-heal service, QMP/QEMU passthrough and Windows guest validation are documented in retained handoffs. Separate Windows `AAGUsbClone` / AAG USB Clone driver work is also evidenced. | HIGH PRIORITY. Capture canonical live source, profiles, build/install logic, Windows-side source where applicable, hashes and licenses. Decide repository boundary between reusable USB Clone platform and Otzar-specific integration. Do not publish device-specific/private/licensing material blindly. |
| WinBoat / Otzar integration and recovery | Extensive clean-room handoffs exist for storage COW/NBD, systemd lifecycle, RemoteApp/RAIL, XSizeHints, GNOME behavior, Touch/FreeRDP routing and USB integration. Latest retained handoff explicitly distinguishes validated baseline from transitional/unverified state. | HIGH PRIORITY. Treat as a system/integration project, not as proof that third-party Otzar/WinBoat code is ours. Publish only AAG-authored integration code/documentation that is legally/privacy safe. Preserve historical vs canonical states. |
| AAG Ubuntu Agent | Distinct local project previously evidenced at `/mnt/data/AI/Agents/AAG-Ubuntu-Agent`, including agent/host bridge and staged artifacts. | Capture source/history/tests and determine whether it is publishable as a standalone AAG project. |
| BlueZ HIDP Ubuntu fix | Engineering/backport work and Ubuntu contribution were performed around BlueZ 5.85/HIDP reconnection. | Document as upstream/distribution contribution unless there is independently useful AAG tooling worth a repository. Do not present BlueZ as AAG-authored. |
| AAG LockLock | Distinct local project previously evidenced at `/mnt/data/MyProjects/AAG - LockLock`, with production acceptance/checkpoints and later thermal/recovery work. | HIGH PRIORITY. Reconcile local Git state, privacy-sensitive incident evidence, release/channel design and publication status before public release. |
| Obsidian AnkiBridge | One of six local Obsidian plugin repositories; deliberately not published in the earlier public portfolio. | Preserve as private candidate until companion/licensing/installability/publication boundaries are resolved. |
| Obsidian Blocks | Local plugin candidate previously identified in portfolio audit. | Capture current repository and resolve provenance + GUI/replacement acceptance before publication. |
| Obsidian SnapShots | Local plugin candidate previously identified in portfolio audit. | Capture current repository and resolve provenance + GUI/replacement acceptance before publication. |
| AnkiSuit | Large private cross-platform Anki add-on with extensive Linux/Windows work and stable checkpoints. | Keep private unless explicitly cleared for publication; create/maintain a complete private handoff and inventory even if no public repository is created. |
| WinBoat Windows backup/rotation automation | Prior evidence identifies automation around WinBoat Windows `data.img` snapshots. | Determine whether this belongs inside WinBoat/Otzar integration docs or merits a reusable backup-tool repository. |
| Windows USB/IP proof-of-concept | Prior work includes a Windows USB/IP/usbipdcpp proof-of-concept. | Capture exact source/repository provenance and classify as original tooling vs fork/experiment before publication. |
| OCR / Surya worktree | Prior evidence identifies a Surya repository/worktree used for OCR engineering. | Classify carefully as upstream/fork/integration work; do not publish third-party source as original AAG work. |
| Knowledge Engine | Large local AAG knowledge/retrieval project with ingestion, retrieval, reranking, verification, provider gateway and UI phases. | Reconcile source/privacy/data licensing before deciding public vs private repository. Corpus/private data must not be published with code. |

This backlog is intentionally conservative: existence in prior engineering history is enough to require reconciliation, but not enough to assert that the current local source is complete, publishable or identical to historical evidence.

## USB Clone / Dummy USB evidence boundary

The retained 2026-08-24 master handoff is the newest supplied system-level source for the WinBoat/Otzar USB chain. It documents the reusable host-side architecture `USB Clone assets/profile -> dummy_hcd/dummy_udc -> Linux USB 0951:1666`, kernel-update self-heal, and a validated QMP passthrough baseline. It also marks the later Compose/QEMU permanent-injection experiment as transitional and requiring re-verification. Therefore future GitHub documentation must not replace the validated QMP baseline with the later experiment unless new evidence closes that gap.

Older 2026-08-14 material is historical evidence, not canonical current state. In particular, historical workspace-guard and USB environment details were superseded by later handoffs. Conflicts must be resolved chronologically and retained as history rather than silently overwritten.

## Portfolio-wide standard adopted

Every original AAG project should have a discoverable long-form handoff. The handoff should answer: why the project started; hardware/software environment where relevant; chronological investigation; failed hypotheses/approaches; root causes; accepted architecture; exact operational/install/remove path; tests and what they do/do not prove; release/publication state; known limitations; privacy/security/legal boundaries; rollback/recovery; repository map; maintenance/release procedure; and a historical-integrity rule preventing later success from erasing earlier evidence.

Forks and upstream work are different: their handoff must explain why the fork/contribution exists, the AAG patch scope, upstream PR/bug relationship, validation and synchronization/retirement strategy. They must not be presented as AAG-authored products.

Private projects are also first-class portfolio records. They require a handoff/inventory and an explicit non-publication reason; `not public` must never mean `undocumented`.

## Minimum repository/document set

Use judgment rather than creating empty boilerplate, but every substantial original project should normally expose: `README.md`; a long-form `HANDOFF.md` or `docs/HANDOFF.md`; architecture; installation/uninstallation; testing/acceptance; troubleshooting/known limitations; rollback/recovery; changelog/release history; security/privacy boundary; license/provenance; and CI/release automation where meaningful. README must link to the handoff. Publication allowlists/build kits must include the handoff when source documentation is part of the release.

## Evidence rules

1. Never convert mock/unit/CI success into a physical-hardware claim.
2. Never convert “application opened” into exact workflow acceptance when the requirement is more specific.
3. Preserve failed experiments when they explain current architecture.
4. Mark unsupported/unverified states explicitly instead of guessing.
5. Do not publish private hardware IDs, coordinates, credentials, private documents, vault/database contents, proprietary third-party binaries/data or copyrighted test samples merely to make a public handoff look complete.
6. Keep release/tag/asset verification separate from runtime acceptance.
7. Keep old version-specific verification reports as historical evidence.
8. Distinguish Ubuntu-host, Windows-host, WinBoat/Windows-guest and CI validation explicitly.
9. Never infer publication readiness from historical chat alone; reconcile against live source before public release.

## Completion gates

The portfolio is not `COMPLETE` until all of the following are true:

1. Every visible GitHub repository has current handoff documentation and passing publication/CI gates appropriate to that repository.
2. Every material project found in history or local inventory is classified: public repository, upstream contribution, private/non-publishable, merged into a parent project, or intentionally retired with reason.
3. Ubuntu and Windows local inventories have been compared against this ledger, including Git repositories and meaningful non-Git source trees/scripts/services.
4. Dummy USB/USB Clone canonical source has been captured and reconciled rather than reconstructed from documentation alone.
5. README/handoff/release/tag/CI consistency is checked after all documentation changes.
6. No secrets, private identifiers, proprietary data or third-party code are accidentally published.
7. A final portfolio audit records remaining unknowns as explicit blockers rather than silently omitting them.

## Remaining recurring obligations

On every future material release, update the relevant HANDOFF, CHANGELOG/release notes, validation/acceptance evidence and support boundary. Re-run CI/publication checks after documentation changes and ensure new handoff files are included in any publication/file-allowlist logic where such allowlists exist.

## Audit conclusion

The earlier conclusion that “all 15 visible repositories are documented” remains true only for the repository-visible subset. It is no longer the completion criterion for the AAG engineering portfolio. The broader reconciliation has identified substantial missing/non-public workstreams, especially Dummy USB/USB Clone, WinBoat/Otzar integration, LockLock, Ubuntu Agent, private Obsidian/Anki projects and upstream contributions. The portfolio remains **IN PROGRESS** until those workstreams are reconciled against live Ubuntu/Windows source and classified without overclaiming authorship or validation.