# Succession: a master is replaced, and the handoff is measured

**In one breath.** Masters come in generations. A successor is spawned on purpose, proves it landed in the right place, retires its predecessor by three measured disappearances, and writes one lineage entry.

The words this page uses are in the [glossary](glossary.md).

## For a ten-year-old

Lighthouse keepers change shifts. The new keeper does not walk straight in. The old keeper checks the new one is standing in the right lighthouse, hands over the logbook, and leaves. The new keeper then checks three things: the old keeper's chair is empty, the old keeper's boat is gone, and the old keeper's lamp is off. Only then does the new keeper write "shift changed" in the logbook.

Here the lighthouse is a workspace. The spawn command carries an expected placement, and a successor that lands in another worktree is closed with exit code 26. Retirement measures three disappearances: the pane, the process, and the tty. If one check was skipped, the status is `CLOSED_PARTIAL`, which can never be mistaken for a full close. The logbook is the lineage file, one entry per generation.

## The five questions

**What happened.** The harness's rule is continue-and-compact: a long session is summarized and goes on. Succession happens only when the owner says so. One seat reports reaching its twentieth generation this way (a seat report, not a public record). Each boot checks the same list: role state, the model answering, the three placement facts, the predecessor's three disappearances, and a lineage entry with the measured values.

**What is confirmed.** The charter defines the clean-spawn procedure and forbids automatic succession. The spawn exit code for a placement mismatch is a named constant. The three-way retirement and the partial status are in the succession module with tests. The boot card records one timed run: 17 minutes from spawn to `CLOSED` on 2026-10-01, with a test and drift sweep included.

**What is inferred.** The ceremony on its own costs a few minutes per generation; it was not timed apart from the sweep. Whether it prevented a duplicate master was never measured.

**What is unknown.** Whether a successor can verify its predecessor's pid on every machine. Orca's terminal record sometimes reports no process id, and the procedure then needs the pid measured by hand.

**Evidence.** [§6 succession](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/06-succession.md); [`succession.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/src/master_runtime/core/succession.py) (`SPAWN_PLACEMENT_MISMATCH`, `retire_predecessor`); [`master-succeed`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/scripts/master-succeed); [`test_succession.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_succession.py).

```
$ scripts/master-succeed retire --self-handle term_new01 --target-handle term_old01 \
    --target-pid 4242 --target-tty ttys011 --execute
# JSON report, abridged to the keys this note discusses
{"status":"CLOSED","closed":true,"disappearances":{"pane":"measured","process":"measured","tty":"measured"}}
```

