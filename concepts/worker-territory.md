# Worker territory: one checkout, one contract, a different runtime

**In one breath.** A worker gets its own checkout, one contract that names what it may write, and by default a runtime (the agent CLI that runs its model) different from the master's. The master keeps the verification and the merge.

The [glossary](glossary.md) defines the harness's recurring words.

## For a ten-year-old

Three friends build a treehouse. One holds the drawing and checks each board. The others each get a corner, a list of boards for that corner, and their own toolbox. Nobody reaches into another corner. When a corner is done, the friend with the drawing climbs up and pulls on every board before anyone sits on it.

The corner is a Git worktree. The list of boards is the contract: branch, allowed files, the proof it must paste into the pull request. The toolbox is a separate runtime, chosen so the master and the worker do not drain the same quota while one waits on the other. The pull on every board is the master's own verification: tests run again, diff compared against the allowed files, review threads counted.

## The five questions

**What happened.** On one day two dispatches failed in ways that looked like worker mistakes. One stopped at staging because it never saw the clause requiring a pull request. One asked for a line the contract quoted word for word. The contract had reached the gate and never reached the worker; only the one-line spec had been sent. Both were rescued by pasting the contract into the worker's terminal by hand, which made an unrecorded hand step load-bearing. The wrapper now copies the contract to a delivery directory, checks the copy byte for byte, and appends a token the worker must quote back.

**What is confirmed.** The contract delivery block and its token are in the dispatch script with that history in its comment. The runtime choice defaults to one other than the master's, and the ledger records each same-runtime choice with its reason. The reaper refuses to remove a worktree that is dirty, unmerged, or holds ignored media.

**What is inferred.** Separate runtimes cost a little setup per worker. The expected gain is a master that keeps dispatching while a worker burns through a long test run; that gain was not measured.

**What is unknown.** Whether the delivered contract should also live on the worker's own branch. It does not today, and the comment in the script says why.

**Evidence.** Sections "1.5 deliver the contract" and "1.6 append standing rules" in [`dispatch`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/dispatch); [worker host diversity runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/worker-host-diversity.md); [`worker_reap.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/src/master_runtime/core/worker_reap.py); [contract conventions](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/contract-conventions.md).

```
# synthetic: two lines of the wrapper's output
📄 contract delivered · /tmp/example/dispatch-contracts/1a2b3c4d-fix-reader.md · read-token required
📎 standing rules · headless ack-token placement voice pr-house
```


<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
