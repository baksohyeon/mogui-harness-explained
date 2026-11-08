# 25. Bounded loop over tracker items

**In one breath.** With the owner's approval and a budget, the master carries several tracker items from ready to done in one stretch, one dispatch per round, without being prompted each time. A progress file records every round, and one script reads that file and says continue or stop, with the reason, against six stop conditions.

**When it runs.** During a run the owner has approved by name, between rounds. The loop is a procedure inside the master's own session, with no new agent and no background process. Every round still goes through the contract, the dispatch, and the verification of [one dispatch](../../walkthroughs/01-one-dispatch.md).

**Mechanism.** The owner approves a budget, `rounds=<n> hours=<h>` (defaults 3 and 4), and the master writes that sentence into the progress file under `docs/loop/`. Eligible tracker items are labeled `loop-ok` by hand; the loop never labels an item itself. Each row of the file is one item in one state: `picked`, `contracted`, `dispatched`, `dispatched: relaunched`, `verifying`, `bot-round(<n>)`, `merge-ready`, `failed`, or `blocked`. `loop-check` reads only the file and its arguments, never Orca, the tracker, Git, or GitHub, and prints one verdict line. `continue round=<n> pick` means take the next item; `continue round=<n> item=<id> state=<state>` means resume that row. `stop reason=<k>` names one of six conditions: round budget spent, wall-clock budget spent, no eligible item, two consecutive failures, a worker question or escalation or a stop file, and a compaction passed. Exit 0 is continue, 3 is stop, 2 is a malformed file with the line number on stderr. Retries are fixed: one relaunch for a worker that dies without `worker_done`, at most three bot rounds per item, no retry on a clone verification failure. Merges stay outside the loop; at stop the master reports the merge-ready pull requests and the owner approves them in one answer.

**Failure it prevents.** A master that spends its context on being prompted once per item instead of on verification. A loop that runs past its budget, past a compaction, or through a worker's question because nothing was counting.

## Example (synthetic)

```
$ master-ops/scripts/loop-check docs/loop/2026-11-07-example.md --now 2026-11-07T14:00:00Z
stop reason=4: two consecutive failures (ex-101, ex-102)
exit=3
```

## Verified in mogui

- Implementation: [`master-ops/scripts/loop-check`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/loop-check), [loop runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/loop.md)
- Tests: [`master-ops/scripts/test-loop-check.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-loop-check.sh)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
