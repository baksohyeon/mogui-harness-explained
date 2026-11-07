# 07. Dispatch timeline join

**Mechanism.** Join the dispatch ledger, the event log, and the live `dispatch-show` record for one dispatch into one time-ordered table.

**Failure it prevents.** Silence that looks the same as "nothing happened". A source with zero matching rows is named in `missing_sources`.

<p align="center"><img src="../../assets/units/07-dispatch-timeline-join.svg" alt="three dispatch sources join into a time-ordered table" width="100%"></p>

## Example (synthetic)

Empty ledger and event log, unknown id:

```
$ scripts/dispatch-timeline --ledger l.jsonl --event-log e.jsonl fake-id
TIMESTAMP   SOURCE   EVENT   OUTCOME   DETAIL
missing sources: ledger, event-log, dispatch-show
```

`--since` combined with an id exits 2.

## Verified in mogui

- Implementation: [`src/master_runtime/core/dispatch_timeline.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/src/master_runtime/core/dispatch_timeline.py), [`scripts/dispatch-timeline`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/scripts/dispatch-timeline)
- Tests: [`tests/test_dispatch_timeline.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/tests/test_dispatch_timeline.py)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
