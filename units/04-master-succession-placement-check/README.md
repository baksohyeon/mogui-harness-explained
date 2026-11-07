# 04. Master succession placement check

**Mechanism.** When a successor master is spawned, the terminal's reported worktree must match the requested and expected placement, or the new terminal is closed.

**Failure it prevents.** A successor that lands in the wrong worktree would run with the wrong cwd. The [succession boot card](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/succession-boot-card.md) requires the cwd to be the workspace root or an approved orchestrator root.

<p align="center"><img src="../../assets/units/04-master-succession-placement-check.svg" alt="successor spawning flows through worktree placement verification" width="100%"></p>

## Example (synthetic)

Expected placement `X`, terminal reports `Y`:

```
spawn placement mismatch; closed terminal <handle>: expected X, got Y
```
`SuccessionError` carries an exit code (default 2) that `master-succeed` returns.

Relevant tests: `test_spawn_successor_expected_placement_mismatch_closes_terminal`, `test_cli_spawn_dry_run_outputs_expected_placement`.

## Verified in mogui

- Implementation: [`src/master_runtime/core/succession.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/src/master_runtime/core/succession.py), [`scripts/master-succeed`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/scripts/master-succeed), [`master-ops/docs/runbooks/succession-boot-card.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/master-ops/docs/runbooks/succession-boot-card.md)
- Tests: [`tests/test_succession.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/tests/test_succession.py), [`tests/test_succession_scenario.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/tests/test_succession_scenario.py)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
