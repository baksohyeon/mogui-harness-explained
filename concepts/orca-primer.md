# Orca primer: what Orca provides, and what the harness adds

**In one breath.** Orca is the program the harness runs inside. It owns terminals, worktrees, and a mailbox between one master and many workers. Orca's own word for the master is coordinator. The harness is a set of scripts that decide what goes into that mailbox, prove that it arrived, and record what happened.

The [glossary](glossary.md) defines the harness's recurring words.

## For a ten-year-old

A school has a building with classrooms, a timetable, and a system of notes that go between the head teacher and each class. The building does not decide what is taught. The head teacher writes the lesson, picks a room, checks the class is in the room, and reads the note that comes back. Here Orca is the building and the notes. The harness is what the head teacher does with them.

## The line between the two

This page has two sources. The first is the harness itself: for each Orca command the harness uses, the page cites the harness file, a script or a runbook, that names it at tag `v0.5.288`. The second is the Orca CLI's own help and built-in guide, used for the worker's `ask` and the master's `reply`, which no harness script calls. A sentence from that source says so, with the binary version and the date it was read. Orca is a separate product and its own documentation is the authority on what every command does.

## What Orca provides

**Terminals.** A pane that runs an agent CLI inside a worktree. The wrapper creates one with `orca terminal create --worktree <selector> --command <agent cli> --json` and waits on it with `orca terminal wait --for tui-idle`. The master reads its screen with `orca terminal read`, types into it with `orca terminal send`, and closes it with `orca terminal close`. The first three appear in [`master-ops/scripts/dispatch`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/dispatch), the last two in the [worker-wait runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/worker-wait.md). A terminal handle begins with `term_` and lives only as long as the Orca app runtime; the [placement record](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/master-placement.md) says never to record a handle as durable.

**Worktrees and selectors.** A worker gets its own checkout, created by Orca under the repository's `.orca/worktrees/` directory. Commands address a place by a selector: `path:<absolute path>` for a checkout, `id:folder:<workspace selector>` for a folder workspace. In the template's placement record the master's seat is a folder workspace, and its selector is the durable identity that record keeps. When a worker is finished, its checkout is removed: `worker-reap` does it with Git's own worktree command, and a master doing it by hand uses `orca worktree remove --worktree <selector>`. No harness script calls Orca's command.

**Orchestration.** One master, the coordinator in Orca's terms, holds a Run. Under it, `orca orchestration task-create --spec <text> --json` records a task and returns a `task_` id. `orca orchestration dispatch --task <id> --to <terminal> --inject --json` binds the task to a pane, writes a preamble and the task text into the agent's prompt, and returns a `ctx_` dispatch id. `orca orchestration dispatch-show --task <id> --json` reads the dispatch's status afterwards. `orca orchestration worker-list` lists live dispatches under a Run. These are the orchestration calls the dispatch wrapper and `worker-wait` make.

**The mailbox.** A worker reports with `orca orchestration send --type worker_done`, carrying its task id, dispatch id, outcome, and a short body. It asks a question with `orca orchestration ask --question <text>` and ends its turn; the master answers with `orca orchestration reply` (both from the Orca CLI's own help, binary 1.4.249, read 2026-11-07). The master is woken by Orca and reads its mail with `orca orchestration check`. A `check` returns a batch with a delivery id.

**Batches and waking.** The harness wraps `check --wait` in [`orca-wait`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/orca-wait), which drains the acknowledgement backlog before it waits. The [orca-wait runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/orca-wait.md) has the master handle every message in the batch first and then acknowledge the batch by that id, since an acknowledgement marks the whole batch read. Chaining the ids this way keeps Orca from replaying a batch. The runbook also warns against hand-written sleep loops in place of `check --wait`. Three more facts come from Orca's built-in guide (binary 1.4.249, read 2026-11-07). A worker that is done closes on its own unless kept open. A `send` to a closed worker reopens it as a follow-up task. A coordinator must never poll in a script, because the script's `check` would take the mail that was meant to wake it.

**JSON shapes.** Orca's JSON output has changed between releases. The harness reads it through one module, [`orca_json.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/lib/orca_json.py), that accepts the older and the newer shape; unit [10](../units/10-orca-json-shape-normalizer/).

## What the harness adds

Everything between the owner's word and `task-create`, and everything between `dispatch` and trusting the result.

Before Orca is asked for anything: a contract file with a hash of record, and a gate on tier, budget, and fan-out ([charter §5](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/05-dispatch-gate.md)). Then delivery of the contract with a read token, and standing rule blocks appended to the spec text ([`rules/standing-rules.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/rules/standing-rules.md)).

After Orca has answered: a start-screen check on the pane, a ledger row, and a model probe that reads the worker's own transcript. Then a delivery verdict that says `UNVERIFIED` when the pane gives no positive signal. Later: a wait that labels dead and stalled workers from measured state, and a reap that closes only unoccupied panes. Last: a timeline that joins the ledger, the event log, and Orca's record, and a redaction scan before anything is pushed.

Each one records a fact Orca does not record, or declines to assume one Orca does not prove.

## The five questions

**What happened.** A contract reached the gate and never reached the worker; only the spec text was sent. Two dispatches in one day looked like worker defects and were master-side defects (the comment above section 1.5 of the dispatch wrapper, dated 2026-08-10). Delivery and the read token exist because of that day.

**What is confirmed.** Every Orca command named above appears in the harness file its section cites at `v0.5.288`, with three exceptions. `ask` and `reply` come from Orca's own help, and `worktree remove` is run by hand. For `terminal send` and `terminal close` the cited file is a runbook, not a script. The dispatch wrapper's section order is gate, deliver, standing rules, task-create, terminal, start screen, inject, probe, delivery check.

**What is inferred.** That the same command set works on other Orca versions. The harness pins nothing about Orca's version. It keeps a surface baseline, a stored record of the Orca commands and output shapes it depends on, and a check that compares the installed Orca against it ([orca-surface-drift](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/orca-surface-drift.md)).

**What is unknown.** How Orca behaves on machines the authoring seat has not run. The [host-harness inventory runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/host-harness-inventory.md) is a snapshot of one machine, dated 2026-08-03, and says so in its first line.

**Evidence.** The files linked above, all at tag `v0.5.288`; the walkthrough [one dispatch](../walkthroughs/01-one-dispatch.md) for the commands in the order they run.

<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
