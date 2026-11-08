# 22. Context cost and the recall ledger

**In one breath.** Two things about a master's context are measured instead of felt: how much of it is spent before the first action, and how much is lost across a compaction. One script reports the first; one writes the ledger for the second, and it is the only writer.

**When it runs.** In the master lifecycle: the turn-0 report by hand, weekly; the recall ledger at every compaction, after the probe of [one master generation](../../walkthroughs/02-one-master-generation.md), step 10.

**Mechanism.** `context-budget` reads the session transcripts and reports the turn-0 payload: the context a session has consumed before it takes its first action. That payload is instruction files, skill and agent listings, tool schemas, and hook output. That cost is paid again at every succession and every worker dispatch, and nothing else in the harness measures it. The transcript location is derived from the workspace path, so the script carries no machine's username. `context-quality-log.sh` appends the recall records the compaction probe asks for and prints a seven-day summary with `--summary`. Its ledger path, `CONTEXT_QUALITY_LOG`, is required and has no default, because a default once let one seat write into another seat's ledger (2026-08-10). `context-quality-sampler.sh` prints the sources of truth the recall is compared against, the tracker's active tracks and recent Git history, and writes nothing.

**Failure it prevents.** Turn-0 growing by a few thousand characters per installed skill until a session begins half full, with nobody noticing when. A recall ledger with another seat's records in it.

## Example (synthetic)

```
$ master-ops/scripts/context-quality-log.sh --summary
CONTEXT_QUALITY_LOG is required and has no default.
set it to this seat ledger, e.g. CONTEXT_QUALITY_LOG=$HOME/.local/state/<seat>/context-quality.jsonl
exit=3
```

## Verified in mogui

- Implementation: [`master-ops/scripts/context-budget`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/context-budget), [`master-ops/scripts/context-quality-log.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/context-quality-log.sh), [`master-ops/scripts/context-quality-sampler.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/context-quality-sampler.sh), [`master-ops/scripts/compaction-probe.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/compaction-probe.sh)
- Tests: [`tests/test_context_quality_scripts.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_context_quality_scripts.py)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
