# Fail closed: "I cannot decide" is its own answer

**In one breath.** Every gate in this harness has three outputs, and the third one is "I could not tell". A gate that cannot tell stops the work. It never rounds up to "fine".

## For a ten-year-old

A lifeguard watches a pool. Green flag means swim, red flag means out of the water. One day the fog rolls in and the lifeguard cannot see the deep end. A lazy lifeguard leaves the green flag up, because nobody has drowned yet. This lifeguard raises a third flag that means "I cannot see", and everyone gets out until the fog lifts.

The harness is full of that third flag. The redaction scanner exits with 0 when clean, 1 when it found something, and 2 when it could not decide, for example when its engine is missing. The product-path guard has a strict mode that admits only commands on a read-only list and blocks everything it cannot parse. A retirement that measured only two of its three signs reports `CLOSED_PARTIAL`, never `CLOSED`.

## The five questions

**What happened.** The dispatch script used to pick a worker's transcript by taking the newest file across every account. When two workers started close together, the newest file could belong to the wrong one, and the model check would pass for a worker it never looked at. The script now snapshots the files before launch and accepts only the one file that appears afterward. If none appears, or more than one, it reports `PROBE_STATE=unavailable` instead of guessing.

**What is confirmed.** The three exit codes of the scanner are stated in its header and tested. The strict guard mode is a documented switch. `CLOSED_PARTIAL` is a named status in the succession module, with a test.

**What is inferred.** Fail-closed gates cost more interruptions. In the chat logs of one seat, most of those interruptions were a missing tool or an unset variable, fixed in a minute. That count was not kept as a number.

**What is unknown.** How often a gate's "cannot decide" hides a real failure behind a boring cause. Nobody has classified the exit-2 events.

**Evidence.** [`redaction-scan.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/scripts/redaction-scan.sh) header lines; [product-path-guard runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/product-path-guard.md); [`succession.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/src/master_runtime/core/succession.py) (`CLOSED_PARTIAL`, `DISAPPEARANCE_MEASURED`); the rollout snapshot entry under v0.5.288 in [`CHANGELOG.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/CHANGELOG.md).

```
$ scripts/redaction-scan.sh --range origin/main..HEAD
redaction-scan: cannot decide (gitleaks not found on PATH)        exit=2
```

## Glossary

- **fail closed**: when a check cannot run, treat the result as a block.
- **exit 2**: the scanner's code for "could not decide"; it is never a pass.
- **strict mode**: the guard setting that admits only read-only commands it recognizes.
- **CLOSED_PARTIAL**: a retirement where one of the three disappearance checks was skipped.
