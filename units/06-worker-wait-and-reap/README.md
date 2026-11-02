# 06. Worker wait and reap

**Mechanism.** `worker-wait` waits on a Run's live dispatches and labels dead or stalled workers; `worker-reap` closes a settled dispatch's terminal and cleans its worktree.

**Failure it prevents.** Closing a pane where a worker is still working, or treating a failed listing as an empty Run. A pane is closed only when it is listed, not claimed by a dispatched worker, and no agent CLI process has its cwd in the worktree.

```mermaid
flowchart LR
  W[worker-wait] --> V{measured state}
  V -- pid gone, no worker_done --> D[DEAD]
  V -- output stale, idle --> S[STALL]
  R[worker-reap task] --> Q{dispatch settled?}
  Q -- no --> E3[exit 3]
  Q -- yes --> P{agent process in worktree?}
  P -- yes or unmeasured --> L[leave pane]
  P -- no --> C[close pane, remove worktree]
```

## Example (synthetic)

`worker-reap` exit codes from the module docstring:

```
2 invalid invocation   3 not settled   4 malformed RPC JSON   5 no dispatch for task
```
`worker-wait` exits 2 when `orca` cannot produce an authoritative listing.

## Verified in mogui

- Implementation: [`src/master_runtime/core/worker_reap.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/src/master_runtime/core/worker_reap.py), [`scripts/worker-reap`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/scripts/worker-reap), [`master-ops/scripts/worker-wait`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/master-ops/scripts/worker-wait)
- Tests: [`tests/test_worker_reap.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/tests/test_worker_reap.py), [`tests/test_worker_wait.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/tests/test_worker_wait.py)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
