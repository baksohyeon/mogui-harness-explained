# mogui harness, explained

**One agent in charge of the others, and the evidence for every rule it follows.**

You have several coding agents open in terminal panes. One of them is supposed to be in charge: it hands out the work, checks what comes back, and keeps its seat when its own context runs out. The mogui harness is the set of scripts that makes that true. It runs on Orca, a terminal program with an orchestration layer, and it answers to one human owner. These pages explain each of its mechanisms to a reader who has never run it, and every evidence link points at the tested code at tag `v0.5.288`.

Every mechanism here exists because something measurable went wrong once. A contract reached the gate and never reached the worker, so the wrapper now delivers it with a token the worker must quote back. A successor master was seated in the wrong worktree and found from two phone screenshots, so a spawn now proves its placement or closes. A worker sat on an approval prompt while the inbox and the pull request stayed quiet, so a sweep now classifies every pane. Four commands were read without their exit status in one day, so a wrapper now prints the status first. The pages name the incident behind each mechanism and what one seat measured afterwards.

What is here: three walkthroughs that follow a procedure from start to end, twenty-seven units that each explain one mechanism, eight concept notes on the ideas behind them, a glossary, and a [roadmap](ROADMAP.md) built from the public record. The map below is the whole of it on one page.

<p align="center"><img src="assets/map.svg" alt="map of the three walkthroughs, the 27 units by lifecycle with an install group, and the concept notes" width="100%"></p>

## How to read this

Seven reading paths.

- The whole shape, once: the [Orca primer](concepts/orca-primer.md), then the walkthrough [one dispatch](walkthroughs/01-one-dispatch.md).
- New to the harness: [role lock](concepts/role-lock.md), [worker territory](concepts/worker-territory.md), [fail closed](concepts/fail-closed.md), then units 02, 09, and 12, then [one dispatch](walkthroughs/01-one-dispatch.md).
- Running an install: [one template upgrade](walkthroughs/03-one-template-upgrade.md), then units 13, 14, 24, 11, and 15, then [template and seat](concepts/template-and-seat.md).
- Reading the rules: [charter map](concepts/charter-map.md), then units 25 and 27.
- Taking over a seat: [one master generation](walkthroughs/02-one-master-generation.md), then units 04, 16, 17, and 03, then [succession](concepts/succession.md).
- Installing a workspace: unit 18, then unit 19, then [one template upgrade](walkthroughs/03-one-template-upgrade.md).
- Debugging a stuck worker: units 20, 06, 07, 03, 21, and 10, then [measured, confirmed, inferred](concepts/measured-not-assumed.md).

The [glossary](concepts/glossary.md) defines the words the pages use without stopping to explain them.

## Walkthroughs

Three procedures in the order they run, about fifteen minutes each, with the Orca commands and the harness output lines named where a step runs them. Index at [`walkthroughs/`](walkthroughs/).

| Walkthrough | Steps | From, to |
|---|---|---|
| [One dispatch](walkthroughs/01-one-dispatch.md) | 15 | The owner's word, to a closed worker pane. |
| [One master generation](walkthroughs/02-one-master-generation.md) | 11 | A promotion audit, to the owner's word to succeed. |
| [One template upgrade](walkthroughs/03-one-template-upgrade.md) | 12 | A release tag, to a redeployed session card. |

## Units

Twenty-seven mechanisms, each explained in about five minutes and linked to its tested implementation. Twenty-five of them run inside a dispatch, a master's life, or an install. Unit 01 is the loop that decides whether a change to the harness itself is kept. Unit 19 is the layer that keeps vendor flags out of the core. The number in front of a unit is its id, the number that starts its directory name; it carries no rank and no reading order. The map above groups the units by when they act in the harness's life, from install to succession, which is why the numbers there are out of sequence.

| Unit | Mechanism |
|---|---|
| [01 harness change acceptance loop](units/01-harness-change-acceptance-loop/) | Keep a harness change only when its pass count over visible and held-out cases rises. |
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
| [16 succession triggers and duplicate masters](units/16-succession-triggers-and-duplicate-masters/) | Classify a succession signal as propose-only; find a second master in the seat. |
| [17 master boot block and live hook](units/17-master-boot-block-and-live-hook/) | Print role, tracks, and alerts at every boot; hold them back after a compaction. |
| [18 progressive onboarding and install checks](units/18-progressive-onboarding-and-install-checks/) | Install one step per turn; measure the machine before and the install after. |
| [19 adapter layer](units/19-adapter-layer-tool-neutral-profiles/) | Keep each runtime's CLI flags in one profile; probe installed tools for real. |
| [20 blocked-worker detection](units/20-blocked-worker-detection/) | Classify every live pane; tell the master when a worker waits on a prompt. |
| [21 fire log, event log, exit vocabulary](units/21-fire-log-event-log-exit-vocabulary/) | Record every hook firing and gate decision; 0 pass, 1 finding, 2 undetermined. |
| [22 context cost and recall ledger](units/22-context-cost-and-recall-ledger/) | Measure turn-0 context and recall loss across compactions. |
| [23 advisory Bash hooks](units/23-advisory-bash-hooks/) | Warn, never block, on bare cd, unfiltered output, oversized results, and poll loops. |
| [24 instance config and workspace descriptor](units/24-instance-config-and-workspace-descriptor/) | Resolve one install's facts: override, file, or an honest unconfigured. |
| [25 bounded loop over tracker items](units/25-bounded-loop-over-tracker-items/) | Carry approved items through rounds; stop on one of six measured conditions. |
| [26 stall watchdog, work ledger, digest loop](units/26-stall-watchdog-work-ledger-digest-loop/) | Label idle progress logs, replay tracks, triage changes as echo, expected, or unexplained. |
| [27 pull request stewardship](units/27-pull-request-stewardship/) | Require filled body sections with no home path; report merge state without guessing. |

## Concepts

Eight short notes on the ideas behind the units. Each answers the same five questions: what happened, what is confirmed, what is inferred, what is unknown, and where the evidence is. Next to them sit the chat response rules a master follows when it writes to its owner, and the glossary. Index at [`concepts/`](concepts/).

| Note | One line |
|---|---|
| [Orca primer](concepts/orca-primer.md) | Orca owns terminals, worktrees, and the mailbox; the harness decides what goes in and proves it arrived. |
| [Role lock](concepts/role-lock.md) | The master proposes and verifies; workers write code; a hook enforces it. |
| [Fail closed](concepts/fail-closed.md) | A gate that cannot decide stops the work; exit 2 is never a pass. |
| [Measured, confirmed, inferred](concepts/measured-not-assumed.md) | Every claim says how it was obtained. |
| [Worker territory](concepts/worker-territory.md) | One checkout, one contract, by default a different runtime, and a read token. |
| [Template and seat](concepts/template-and-seat.md) | One upstream, many installs, upgrades against a manifest. |
| [Succession](concepts/succession.md) | Generations of masters, placement proof, three measured disappearances. |
| [Charter map](concepts/charter-map.md) | Ten numbered sections; which one owns which decision. |
| [Chat response rules](concepts/chat-response-rules.md) | Twelve sentence rules for replies to the owner, most derived from ASD-STE100. |
| [Glossary](concepts/glossary.md) | Ninety-two entries for the words the pages use, one line each, with where to read more. |

## Where the evidence is

The implementation is [mogui-ADE-orchestrator](https://github.com/baksohyeon/mogui-ADE-orchestrator), with 54 Python test files in [`tests/`](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/v0.5.288/tests), 26 shell tests under [`master-ops/scripts/test-*`](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/v0.5.288/master-ops/scripts), measured at v0.5.288, 2026-11-07 ([release](https://github.com/baksohyeon/mogui-ADE-orchestrator/releases/tag/v0.5.288)), and CI in [`gates.yml`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/.github/workflows/gates.yml). Its five jobs are the Python tests on three operating systems, the shell tests, the rendered shell tests, the changelog fragment gate, and the redaction scan with its informational inventory. Three more workflows label pull requests ([`labeler.yml`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/.github/workflows/labeler.yml)) and issues ([`issue-os-labeler.yml`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/.github/workflows/issue-os-labeler.yml)) and lock old threads ([`lock.yml`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/.github/workflows/lock.yml)). The repository's own reference table of commands is pinned to the scripts that exist by [`tests/test_reference_command_table.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_reference_command_table.py). Measured results on these pages come from one seat, one installed copy of the harness, and say so.

## What is not here

No transcripts, work data, internal paths, or organization redaction rules. Identifiers in the examples are synthetic. What is unfinished or unmeasured in the harness is listed on the [roadmap](ROADMAP.md), from the public record only.

<p align="center"><img src="assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
