# Roadmap

What the public record says is unfinished or unmeasured in the mogui harness, read at tag `v0.5.288` and on `main` as of 2026-11-08. The sources are four. The repository's open issues. The changelog fragments on `main` that no release has folded yet. The "What this page does not claim" and "What is unknown" sections on these pages. The modules that ship with tests and no caller. Nothing here states a date the record does not state.

## Direction

The owner's stated direction, 2026-11-08: a harness an outside contributor can run from the install alone. The items below that bear on it are the install checks and the session-mode router of unit [18](units/18-progressive-onboarding-and-install-checks/), the tool probes of unit [19](units/19-adapter-layer-tool-neutral-profiles/), the instance facts that keep one machine's values out of the template in unit [24](units/24-instance-config-and-workspace-descriptor/), issue #216 on reading the seat at install instead of asking for a selector, and the unknown of how far installed seats drift. Everything else on this page is on file without a stated direction.

## Shipped on `main`, not yet released

Two changelog fragments sit on `main` above `v0.5.288` ([fragment directory](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/main/master-ops/changelog.d)):

- The dispatch wrapper passes `--from` on `task-create` and `dispatch` when it is told which terminal it dispatches from.
- The skill-composition guide refers to a peer seat's operations repository generically, without a commit hash that cannot be located.

They become part of the next tag when `changelog-release` folds them; unit [15](units/15-changelog-fragment-gate/) covers the mechanism.

## Open issues

| Issue | Question on file | Pages it touches |
|---|---|---|
| [#216](https://github.com/baksohyeon/mogui-ADE-orchestrator/issues/216) | Could `master-succeed spawn` read the seat recorded at install instead of taking a selector on every succession? | [one master generation](walkthroughs/02-one-master-generation.md) step 2, unit [04](units/04-master-succession-placement-check/) |
| [#218](https://github.com/baksohyeon/mogui-ADE-orchestrator/issues/218) | Two scripts, `spawn-test` and `dispatch-smoke`, still read Orca's JSON directly instead of through the one normalizer; `worker-list` pagination is untested end to end. | unit [10](units/10-orca-json-shape-normalizer/), unit [18](units/18-progressive-onboarding-and-install-checks/) |
| [#219](https://github.com/baksohyeon/mogui-ADE-orchestrator/issues/219) | `worker-wait` cannot tell a malformed `worker-list` result from a genuinely empty Run, so an unexpected shape can read as "nothing left". | unit [06](units/06-worker-wait-and-reap/) |

## Libraries with tests and no caller

Three modules are tested at `v0.5.288` and imported by nothing outside their tests. Each encodes a rule the harness enforces another way today.

| Module | What it would do | Enforced today by |
|---|---|---|
| `core/lineage.py` | Validate the 13 fields of a lineage entry, reject a duplicate generation, verify the write was append-only. | Hand-written entries and the lineage README. Unit [16](units/16-succession-triggers-and-duplicate-masters/). |
| `core/approval/` | Classify an action into the approval gate it needs and refuse a gated action without an approved proposal. | The product-path guard and charter §3. [Role lock](concepts/role-lock.md). |
| `core/context/` | Resolve a workspace manifest against the filesystem into a descriptor of declared and observed repositories. | The instance runtime config and the workspace descriptor. Unit [24](units/24-instance-config-and-workspace-descriptor/). |

## Measured on one seat only

These pages say what one installation measured and what no one has measured elsewhere.

- The wrapper's delivery check classified no codex pane as `agent-started` on the authoring seat; every codex dispatch ended `UNVERIFIED` and the master read the pane by hand. Whether another machine's panes match a known prepared-prompt pattern is unmeasured. [One dispatch](walkthroughs/01-one-dispatch.md).
- The model probe found a new transcript file on two of eight dispatches at launch time; the other six carried `MODEL_UNVERIFIED` until the master verified by hand. [One dispatch](walkthroughs/01-one-dispatch.md), unit [03](units/03-transcript-model-identity-probe/).
- Succession took 17 minutes from spawn to `CLOSED` on one run with the test sweep first; the ceremony alone is untimed. Whether it ever prevented a duplicate master is unmeasured. [Succession](concepts/succession.md).
- Orca's terminal record sometimes carries no process id, and retirement then needs a pid measured by hand. [Succession](concepts/succession.md).
- How far installed seats drift from the template is unpublished; the template has no telemetry and asks for none. [Template and seat](concepts/template-and-seat.md).
- One template-side shell test, the product-path guard test, fails on the authoring machine in a way that predates the last upgrade; whether it fails elsewhere is unmeasured. [One template upgrade](walkthroughs/03-one-template-upgrade.md).
- No one has classified the exit-2 events of the fail-closed gates by cause. [Fail closed](concepts/fail-closed.md).
- A wired hook that never fires and a hook that is not wired both leave zero fire-log lines; the active canary that would tell them apart is deferred by the runbook. Unit [21](units/21-fire-log-event-log-exit-vocabulary/).

## Tests the record names as missing

- The adapter layer has no test file of its own. Unit [19](units/19-adapter-layer-tool-neutral-profiles/).
- Three of the four advisory Bash hooks have no test file of their own. Unit [23](units/23-advisory-bash-hooks/).
- Every shell test and every Python test file at the tag is linked from the unit, note, or README section it belongs to; the README counts them.

## This repository

- The seat's `MASTER-OPERATIONS.md` index is instance-owned, so the [charter map](concepts/charter-map.md) describes the template's charter, not any seat's copy.

<p align="center"><img src="assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
