<p align="center"><img src="assets/map.svg" alt="map of the 15 units by lifecycle" width="100%"></p>

# mogui harness, explained

This repo splits the mogui-ADE-orchestrator harness into 15 small units, each explaining one mechanism in about 5 minutes and linking to its tested implementation.

**Start here.** Three reading paths, each about half an hour.

- New to the harness: [role lock](concepts/role-lock.md), [worker territory](concepts/worker-territory.md), [fail closed](concepts/fail-closed.md), then units 02, 09, and 12.
- Running an install: units 13, 14, 11, and 15, then [template and seat](concepts/template-and-seat.md).
- Debugging a stuck worker: units 06, 07, 03, and 10, then [measured, confirmed, inferred](concepts/measured-not-assumed.md).

A word you do not know is in the [glossary](concepts/glossary.md).

| Unit | Mechanism |
|---|---|
| [01 harness change acceptance loop](units/01-harness-change-acceptance-loop/) | Keep a change only when combined visible+holdout passes strictly rise. |
| [02 dispatch tier fan-out gate](units/02-dispatch-tier-fanout-gate/) | Gate each dispatch on budget, routing, model tier, and per-tier fan-out. |
| [03 transcript model identity probe](units/03-transcript-model-identity-probe/) | Measure the model that answered and find mid-session switches. |
| [04 master succession placement check](units/04-master-succession-placement-check/) | Close a successor terminal that lands in the wrong worktree. |
| [05 read-only recovery flow](units/05-read-only-recovery-flow/) | Run recovery steps 0 to 6 as reads, fail-closed after a charter miss. |
| [06 worker wait and reap](units/06-worker-wait-and-reap/) | Label dead or stalled workers; close only settled, unoccupied panes. |
| [07 dispatch timeline join](units/07-dispatch-timeline-join/) | Join ledger, event log, and live record; name sources with no rows. |
| [08 scope-stating redaction scan](units/08-scope-stating-redaction-scan/) | Scan repo and conversation surfaces; exit 2 means cannot decide. |
| [09 product path write guard hook](units/09-product-path-write-guard-hook/) | Block tool writes into a configured product repository root. |
| [10 orca JSON shape normalizer](units/10-orca-json-shape-normalizer/) | Normalize old and new orchestration JSON shapes in one module. |
| [11 rendered shell-test lane](units/11-rendered-shell-test-lane/) | Run shell tests against a rendered master-ops scratch install. |
| [12 contract delivery and read token](units/12-contract-delivery-read-token/) | Deliver contracts byte-for-byte with a hash-derived read token. |
| [13 template manifest and instance-owned paths](units/13-template-manifest-instance-owned-paths/) | Apply manifest-owned files while protecting instance-owned paths. |
| [14 workspace card scope and LOCAL.md](units/14-workspace-card-scope-local-file/) | Scope the master card and preserve its local extension. |
| [15 changelog fragment gate](units/15-changelog-fragment-gate/) | Require dated fragments before release-time changelog folding. |

**Verified implementation:** [mogui-ADE-orchestrator](https://github.com/baksohyeon/mogui-ADE-orchestrator), with 54 Python test files in [`tests/`](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/v0.5.288/tests), 26 shell tests under [`master-ops/scripts/test-*`](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/v0.5.288/master-ops/scripts), measured at v0.5.288, 2026-11-07 ([release](https://github.com/baksohyeon/mogui-ADE-orchestrator/releases/tag/v0.5.288)), and CI in [`gates.yml`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/.github/workflows/gates.yml).

**Concepts:** six short notes on the ideas behind the units (role lock, fail closed, measured versus inferred, worker territory, template and seat, succession), each answering the same five questions with evidence links at `v0.5.288`, plus the twelve chat response rules a master follows when it writes to its owner. Start at [`concepts/`](concepts/).

**What is not here:** no transcripts, work data, internal paths, or organization redaction rules. Examples are synthetic.

<p align="center"><img src="assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
