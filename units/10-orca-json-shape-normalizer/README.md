# 10. Orca JSON shape normalizer

**Mechanism.** The `orca_json` module reads old nested keys first and newer top-level keys second. It normalizes worker statuses so old `dispatched` and new `in_progress` both report `in_progress`.

**Failure it prevents.** A shape change can leave one-off readers with an empty string or `None`. The module and its test keep each new path in one place.

<p align="center"><img src="../../assets/units/10-orca-json-shape-normalizer.svg" alt="old and new orca JSON shapes flow through one normalizer" width="100%"></p>

## Example (synthetic)

```
# master-ops/scripts copied to /tmp/scripts
python3 -c 'import sys; sys.path.insert(0, sys.argv[1]); from lib import orca_json; print(orca_json.task_id({"taskId":"task_new1"}))' /tmp/scripts
task_new1
```

## Verified in mogui

- Implementation: [`master-ops/scripts/lib/orca_json.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/lib/orca_json.py), [`master-ops/docs/runbooks/orca-json.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/orca-json.md), [`master-ops/scripts/dispatch`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/dispatch)
- Tests: [`master-ops/scripts/test-orca-json.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-orca-json.sh)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
