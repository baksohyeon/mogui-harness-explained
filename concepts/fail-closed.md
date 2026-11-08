# Fail closed: "I cannot decide" is its own answer

**In one breath.** Several gates in this harness have a third output, "I could not tell". A gate that reaches it stops the work. It never rounds up to "fine".

The [glossary](glossary.md) defines the harness's recurring words.

## For a ten-year-old

A lifeguard watches a pool. Green flag means swim, red flag means out of the water. One day the fog rolls in and the lifeguard cannot see the deep end. A lazy lifeguard leaves the green flag up, because nobody has drowned yet. This lifeguard raises a third flag that means "I cannot see", and everyone gets out until the fog lifts.

The harness is full of that third flag. The redaction scanner exits with 0 when clean, 1 when it found something, and 2 when it could not decide, for example when its engine is missing. Other tools in the harness return 2 for a bad invocation, and the product-path guard returns it to block, so a 2 is read against the script that returned it. The product-path guard has a strict mode that admits only commands on a read-only list and blocks everything it cannot parse. A retirement that measured only two of its three signs reports `CLOSED_PARTIAL`, never `CLOSED`.

## The five questions

**What happened.** The dispatch script used to pick a worker's transcript by taking the newest file across every account. When two workers started close together, the newest file could belong to the wrong one, and the model check would pass for a worker it never looked at. The script now snapshots the files before launch and accepts only the one file that appears afterward. If none appears, or more than one, it reports `PROBE_STATE=unavailable` instead of guessing.

**What is confirmed.** The three exit codes of the scanner are stated in its header and tested. The strict guard mode is a documented switch. `CLOSED_PARTIAL` is a named status in the succession module, with a test.

**What is inferred.** Fail-closed gates cost more interruptions. In the chat logs of one seat, most of those interruptions were a missing tool or an unset variable, fixed in a minute. That count was not kept as a number.

**What is unknown.** How often a gate's "cannot decide" hides a real failure behind a boring cause. Nobody has classified the exit-2 events.

**Evidence.** [`redaction-scan.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/scripts/redaction-scan.sh) header lines; [product-path-guard runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/product-path-guard.md); [`succession.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/src/master_runtime/core/succession.py) (`CLOSED_PARTIAL`, `DISAPPEARANCE_MEASURED`); the rollout snapshot entry under v0.5.288 in [`CHANGELOG.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/CHANGELOG.md).

```
# synthetic: a bad invocation, which the scanner also reports with exit 2
$ scripts/redaction-scan.sh --range main
redaction-scan: --range requires A..B
exit=2
```


<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
