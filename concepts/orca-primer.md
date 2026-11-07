# Orca primer: what the host provides, and what the harness adds

**In one breath.** Orca is the program the harness runs inside. It owns terminals, worktrees, and a mailbox between one coordinator and many workers. The harness is a set of scripts that decide what goes into that mailbox, prove that it arrived, and record what happened.

## For a ten-year-old

A school has a building with classrooms, a timetable, and a system of notes that go between the head teacher and each class. The building does not decide what is taught. The head teacher writes the lesson, picks a room, checks the class is in the room, and reads the note that comes back. Here Orca is the building and the notes. The harness is what the head teacher does with them.

## The line between the two

This page describes only the Orca commands the harness scripts invoke, and cites the harness file that calls each one at tag `v0.5.288`. Orca is a separate product and its own documentation is the authority on what those commands do. Where a fact comes from Orca's built-in guide and not from a harness file, the sentence says so, with the binary version and the date it was read.

## What Orca provides

**Terminals.** A pane that runs an agent CLI inside a worktree. The wrapper creates one with `orca terminal create --worktree <selector> --command <agent cli> --json`, waits on it with `orca terminal wait --for tui-idle`, reads its screen with `orca terminal read`, types into it with `orca terminal send`, and closes it with `orca terminal close`. All five appear in [`master-ops/scripts/dispatch`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/dispatch) or the [worker-wait runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/worker-wait.md). A terminal handle begins with `term_` and lives only as long as the Orca app runtime; the [placement record](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/master-placement.md) says never to record a handle as durable.

**Worktrees and selectors.** A worker gets its own checkout, created by Orca under the repository's `.orca/worktrees/` directory. Commands address a place by a selector: `path:<absolute path>` for a checkout, `id:folder:<workspace selector>` for a folder workspace. In the template's placement record the master's seat is a folder workspace, and its selector is the durable identity that record keeps.

**Orchestration.** One coordinator holds a Run. Under it, `orca orchestration task-create --spec <text> --json` records a task and returns a `task_` id. `orca orchestration dispatch --task <id> --to <terminal> --inject --json` binds the task to a pane, writes a preamble and the task text into the agent's prompt, and returns a `ctx_` dispatch id. `orca orchestration dispatch-show --task <id> --json` reads the dispatch's status afterwards. `orca orchestration worker-list` lists live dispatches under a Run. These four are the calls the dispatch wrapper and `worker-wait` make.

**The mailbox.** A worker reports with `orca orchestration send --type worker_done`, carrying its task id, dispatch id, outcome, and a short body. It asks a question with `orca orchestration ask --question <text>` and ends its turn; the coordinator answers with `orca orchestration reply` (both from the Orca CLI's own help, binary 1.4.249, read 2026-11-07). The coordinator is woken by Orca and reads its mail with `orca orchestration check`. A `check` returns a batch with a delivery id, and the [orca-wait runbook](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/orca-wait.md) has the master acknowledge each batch by that id so Orca neither replays a message nor drops one, and warns against hand-written sleep loops in place of `check --wait`. From Orca's built-in guide (binary 1.4.249, read 2026-11-07): a worker that is done closes on its own unless kept open, `send` to a closed worker reopens it as a follow-up task, and a coordinator must never poll in a script, because the script's `check` would take the mail that was meant to wake the coordinator.

**JSON shapes.** Orca's JSON output has changed between releases. The harness reads it through one module, [`orca_json.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/lib/orca_json.py), that accepts the older and the newer shape; unit [10](../units/10-orca-json-shape-normalizer/).

## What the harness adds

Everything between the owner's word and `task-create`, and everything between `dispatch` and trusting the result.

Before Orca is asked for anything: a contract file with a hash of record, a gate on tier, budget, and fan-out ([charter §5](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/05-dispatch-gate.md)), delivery of the contract with a read token, and standing rule blocks appended to the spec text ([`rules/standing-rules.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/rules/standing-rules.md)).

After Orca has answered: a start-screen check on the pane, a ledger row, a model probe that reads the worker's own transcript, and a delivery verdict that says `UNVERIFIED` when the pane gives no positive signal. Later: a wait that labels dead and stalled workers from measured state, a reap that closes only unoccupied panes, a timeline that joins the ledger, the event log, and Orca's record, and a redaction scan before anything is pushed.

Each one records a fact Orca does not record, or declines to assume one Orca does not prove.

## The five questions

**What happened.** A contract reached the gate and never reached the worker; only the spec text was sent. Two dispatches in one day looked like worker defects and were coordinator defects (the comment above section 1.5 of the dispatch wrapper, dated 2026-08-10). Delivery and the read token exist because of that day.

**What is confirmed.** The Orca commands named above are the ones the harness scripts call at `v0.5.288`. The dispatch wrapper's section order is gate, deliver, standing rules, task-create, terminal, start screen, inject, probe, delivery check.

**What is inferred.** That the same command set works on other Orca versions. The harness pins nothing about Orca's version; it keeps a surface baseline and a drift check instead ([orca-surface-drift](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/orca-surface-drift.md)).

**What is unknown.** How Orca behaves on hosts the authoring seat has not run. The [host inventory](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/host-harness-inventory.md) is a snapshot of one machine, dated 2026-08-03, and says so in its first line.

**Evidence.** The files linked above, all at tag `v0.5.288`; the walkthrough [one dispatch](../walkthroughs/01-one-dispatch.md) for the commands in the order they run.

## Glossary

- **Run**: the coordinator's identity in Orca's orchestration; tasks and dispatches hang under it.
- **task**: one unit of work Orca records under a Run, with a `task_` id.
- **dispatch**: the binding of a task to a pane, with a `ctx_` id; the thing a worker reports against.
- **pane**: an Orca terminal running an agent CLI; its `term_` handle is not durable.
- **selector**: how a command names a place: `path:` for a checkout, `id:folder:` for a workspace.
- **`worker_done`**: the message type a worker sends when it finishes; it settles the task and wakes the coordinator.

<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
