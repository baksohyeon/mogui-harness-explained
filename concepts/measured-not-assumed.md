# Measured, confirmed, inferred: say which one it is

**In one breath.** Every report in this harness marks each claim as something it measured, something a source confirmed, or something it inferred. A number without its instrument and date is a guess with good posture.

The words this page uses are in the [glossary](glossary.md).

## For a ten-year-old

Two kids report the temperature outside. One says "it is cold". The other says "the thermometer by the door read 4 degrees at eight this morning". If you need a coat, the second kid helped you. If the thermometer was broken, you can find out.

The harness writes like the second kid. The self-check prints what it measured and where: the Python it found, the version of the terminal tool, how many hooks are wired, whether the deployed session card matches the canonical copy. The dispatch wrapper reads the model name off the worker's own transcript, and the gate records the reason code `MODEL_UNVERIFIED` when it could not. The runbook for the JSON shapes marks two rows as "peer-seat report, not independently re-measured" because the author could not run those commands from where it sat.

## The five questions

**What happened.** A terminal tool changed its JSON keys with no notice. Every reader that assumed the old keys returned an empty string, and every script treated the empty string as a normal value. The fix added a module that reads both shapes, and one line to the self-check: the tool's version, with "changed since" and the old version when the previous run recorded a different one.

**What is confirmed.** The self-check prints those lines. The wrapper's model probe reports either a transcript measurement or `unavailable`, and the gate turns the second into `MODEL_UNVERIFIED`. The JSON runbook's table labels each row by how it was measured.

**What is inferred.** Labeling claims slows writing down. One seat found the labels paid for themselves the first time a "confirmed" fact turned out to be an inference, because the label made the correction a one-line edit.

**What is unknown.** Whether readers outside the harness read the labels or skip them.

**Evidence.** [`harness-selfcheck.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/harness-selfcheck.sh) and [its runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/harness-selfcheck.md); the model probe section of [`dispatch`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/dispatch) and the reason codes in [`dispatch_gate.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/src/master_runtime/core/dispatch_gate.py); the measured-shapes table in [`orca-json.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/orca-json.md).

```
# synthetic: the shape of `bash master-ops/scripts/harness-selfcheck.sh` output
Orca: 1.4.249 (last install 2026-11-04T23:41:48), changed since 1.4.247
Template: v0.5.288 stamped, adoption ledger missing
Hooks: 16 wired
Card: deployed copy matches canonical
```

