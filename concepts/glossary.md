# Glossary

Seventy-three entries for the words the unit, concept, and walkthrough pages use without stopping to explain them; an entry covers one word or a few that mean the same thing. Each line says what the word means in this harness and where to read more. Words marked (Orca) come from Orca, the terminal program the harness runs inside; Orca's own documentation is the authority on them.

## People and roles

- **owner**: the person the master works for. The owner approves proposals and merges. See [role lock](role-lock.md).
- **master**: the one agent the owner talks to in a workspace. It plans, dispatches, verifies, and never writes product code itself. See [role lock](role-lock.md).
- **coordinator** (Orca): Orca's name for the session that holds a Run and reads the mailbox. In this harness that session is the master.
- **worker**: an agent the master starts to do one contract in its own checkout. See [worker territory](worker-territory.md).
- **generation**: one master session, from boot to retirement. See [succession](succession.md).
- **predecessor**, **successor**: the retiring master and the one that replaces it. See [one master generation](../walkthroughs/02-one-master-generation.md).
- **Role Lock**: the hook-enforced form of "the master does not write product code". See [role lock](role-lock.md).

## Places

- **workspace**: the directory tree one master is responsible for: an operations repository plus one or more product repositories.
- **product repository**, **product root**: a repository that holds the software being built. Only workers write there. See [unit 09](../units/09-product-path-write-guard-hook/).
- **operations repository**: the master's own repository: contracts, runbooks, lineage, local config. The template renders into it.
- **worktree**: a second checkout of a repository on its own branch in its own directory; every worker gets one. See [unit 06](../units/06-worker-wait-and-reap/).
- **pane**, **terminal**, **handle** (Orca): one terminal session, and the id Orca gives it. A worker runs in a pane; the master reads and closes panes by handle. A handle begins with `term_` and lasts only as long as the Orca app runs.
- **selector** (Orca): how a command names a place: `path:<absolute path>` for a checkout, `id:folder:<workspace selector>` for a folder workspace. See the [Orca primer](orca-primer.md).
- **runtime**, **agent CLI**: the program that runs a model inside a pane, named in a contract's front matter (`codex`, `claude`, and others).
- **runtime diversity**: running the worker on a runtime other than the master's; the runbook that sets the default calls it host diversity. See [worker territory](worker-territory.md).
- **machine**: the computer a seat runs on. The runbooks call it a host, and a measurement from one machine says so.

## Units of work

- **Run** (Orca): the orchestration session a master owns; tasks and worker messages bind to it.
- **task** (Orca): one dispatched piece of work with a `task_` id and a status.
- **dispatch** (Orca): injecting a task into a worker's pane, and the record of that injection, with a `ctx_` id.
- **preamble** (Orca): the text Orca writes into the worker's prompt ahead of the task: its task id, its dispatch id, and how to ask and finish. See [one dispatch](../walkthroughs/01-one-dispatch.md).
- **contract**: the file the master writes for one worker: what to change, which paths it may write, what done means, and the proof to paste into the pull request. See [unit 12](../units/12-contract-delivery-read-token/).
- **spec**: the short task text the worker sees first; the contract is its authority.
- **standing rules**: named rule blocks a contract's front matter pulls in by name, appended to the spec. See [unit 12](../units/12-contract-delivery-read-token/).
- **read token**, **acknowledgement token**: a short string appended to the delivered contract; a worker that quotes it proves it opened the file. The standing rule about it is named `ack-token`. See [unit 12](../units/12-contract-delivery-read-token/).
- **FIRST ACTION**, **placement verdict**: the three lines a worker reports before any work: in the expected worktree or not, in the master's checkout or not, branch and head. See [one dispatch](../walkthroughs/01-one-dispatch.md), step 11.
- **ask**, **reply** (Orca): a worker asks a question with `ask` and ends its turn; the master answers with `reply`, which wakes the worker. See the [Orca primer](orca-primer.md).
- **worker_done** (Orca): the message a worker sends when its task is finished, with an outcome of succeeded or failed.
- **check**, **batch** (Orca): the master reads its mail with `check`; a batch is what one `check` returns, acknowledged as a whole by its delivery id. See the [Orca primer](orca-primer.md).
- **settled**: a dispatch whose status is terminal: completed, accepted, failed, or abandoned. The reaper acts only on a settled dispatch. See [unit 06](../units/06-worker-wait-and-reap/).

## Gates and checks

- **dispatch wrapper**, **wrapper**: `master-ops/scripts/dispatch`, the script the master runs to dispatch a contract; it owns the gate, the delivery, the standing rules, the Orca calls, and the delivery verdict. See [one dispatch](../walkthroughs/01-one-dispatch.md).
- **dispatch gate**: the check every dispatch passes: budget, routing, model tier, fan-out. See [unit 02](../units/02-dispatch-tier-fanout-gate/).
- **tier**, **tier policy**, **fan-out**: a tier is a named group of models in the policy file; the shipped policy has `top` and `efficient`. The policy can also cap how many workers of one tier run at once; the shipped policy caps none. A top-tier dispatch is refused until the master passes the owner's approval. See [unit 02](../units/02-dispatch-tier-fanout-gate/).
- **pre-trust**: marking the worker's worktree as trusted for its runtime before launch, so the worker does not stop on a trust prompt. See [one dispatch](../walkthroughs/01-one-dispatch.md), step 2.
- **start screen**: what the pane shows after the runtime starts. The wrapper reads it and stops when it is a menu or a notice instead of a prompt. See [one dispatch](../walkthroughs/01-one-dispatch.md), step 7.
- **prepared prompt**: a pane state the wrapper recognizes as the runtime waiting for input; a pane that matches none is reported as `UNVERIFIED`. See [one dispatch](../walkthroughs/01-one-dispatch.md), step 10.
- **delivery verdict**: the wrapper's last line about a dispatch: what the pane and Orca's status proved, or `UNVERIFIED` with the command to run next. See [one dispatch](../walkthroughs/01-one-dispatch.md), step 10.
- **ledger**: the append-only file where each dispatch decision is recorded. See [unit 07](../units/07-dispatch-timeline-join/).
- **model probe**, **rollout**: reading the model name out of the worker's own transcript file (a rollout, in the codex runtime's terms) instead of trusting the declared name. See [unit 03](../units/03-transcript-model-identity-probe/).
- **reasoning effort**: the codex runtime's setting for how long it reasons before it answers. The wrapper launches workers at `xhigh`, and the start screen shows the value after the model name. See [one dispatch](../walkthroughs/01-one-dispatch.md), step 7.
- **reaper**: `worker-reap`, the script that closes a finished worker's pane and removes its worktree, and refuses when the pane is occupied or the worktree is dirty, unmerged, or holds ignored media. See [unit 06](../units/06-worker-wait-and-reap/).
- **product-path guard**: the hook that blocks a master's writes into a product root. See [unit 09](../units/09-product-path-write-guard-hook/).
- **strict mode**: the guard setting that admits only read-only commands it recognizes and blocks everything it cannot parse. See [fail closed](fail-closed.md).
- **redaction scan**: the pre-push scan for secrets and internal identifiers. See [unit 08](../units/08-scope-stating-redaction-scan/).
- **exit 2**: the code the redaction scan, the drift audit, and the self-check return for "could not decide"; it is never a pass. The same number is the bad-invocation code of several command-line tools and the block code of the product-path guard, so each script's header says what its 2 means. See [fail closed](fail-closed.md).
- **fail closed**: when a check cannot run, treat the result as a block. See [fail closed](fail-closed.md).
- **self-check**: the boot script that prints one measured line per harness layer. See [measured, confirmed, inferred](measured-not-assumed.md).
- **adoption ledger**: the file in which a seat records its progress adopting the template. The self-check's first `Template:` line reads `adoption ledger missing` when the seat has none. See [one template upgrade](../walkthroughs/03-one-template-upgrade.md), step 2.
- **surface baseline**: a stored record of the Orca commands, flags, and output shapes the harness depends on; `orca-surface-check.sh` compares the installed Orca against it. See the [Orca primer](orca-primer.md).
- **twins**: the two workspace-card files, `CLAUDE.md` and `AGENTS.md`, which must stay byte-identical; the self-check's `Twins:` line compares them. See [unit 14](../units/14-workspace-card-scope-local-file/).
- **hook**: a small script the runtime runs before or after a tool call; the guard and the role-state injector are hooks.
- **measured**, **confirmed**, **inferred**: the three labels a claim carries. Measured is read from the machine by the script that reports it; confirmed is stated by a source the reader can open; inferred is reasoned by the author from the other two. See [measured, confirmed, inferred](measured-not-assumed.md).

## Template, upgrade, lineage

- **template**: the `master-ops/` tree in the public repository, with placeholder tokens. See [template and seat](template-and-seat.md).
- **seat**: one installed copy of the template, rendered with its own values, with its own instance-owned files. A measurement "from one seat" comes from one such install.
- **placeholder**: a `{{TOKEN}}` the render fills in, such as the workspace root.
- **manifest**: the list of files the template owns, with the template version. See [unit 13](../units/13-template-manifest-instance-owned-paths/).
- **instance-owned path**: a file the template never overwrites: role state, lineage, local config, contracts, `LOCAL.md`. See [unit 13](../units/13-template-manifest-instance-owned-paths/).
- **drift**: the difference between a seat's copy of a template file and the template's current one. The apply tool's dry run lists the files it would overwrite, and the self-check's `Card:` line checks the one deployed card; no check publishes whole-seat drift. See [template and seat](template-and-seat.md).
- **dry run**: the plan pass of `template-apply`: it prints every file it would write, with a reason, and writes nothing. See [one template upgrade](../walkthroughs/03-one-template-upgrade.md).
- **re-stamp**: applying a newer template onto a seat, file by file. See [one template upgrade](../walkthroughs/03-one-template-upgrade.md).
- **workspace card**, **session card**: the two identical files at the workspace root that tell a session what role it holds. See [unit 14](../units/14-workspace-card-scope-local-file/).
- **changelog fragment**: one dated file per change, folded into the changelog at release time. See [unit 15](../units/15-changelog-fragment-gate/).
- **placement**: proof that a session sits where it was meant to. A master proves it with three measured facts (selector, working directory, session namespace); a worker reports it as the three-line placement verdict. See [unit 04](../units/04-master-succession-placement-check/) and [one dispatch](../walkthroughs/01-one-dispatch.md), step 11.
- **promotion audit**: the step before a spawn in which the sitting master moves what must survive into Git, the issue tracker, and the lineage. See [one master generation](../walkthroughs/02-one-master-generation.md), step 1.
- **handshake**: the moment a successor gives its predecessor the three things retirement needs: the successor's identity, the operations repository's `main` sha, and the Run binding. See [one master generation](../walkthroughs/02-one-master-generation.md), step 3.
- **three disappearances**: pane, process, and tty of the predecessor, each measured gone, in that order. See [succession](succession.md).
- **CLOSED_PARTIAL**: a retirement in which one of the three disappearances was not measured; a full close is `CLOSED`. See [succession](succession.md).
- **compaction**: the runtime summarizing a long session and continuing with the summary. The harness's rule is continue-and-compact. See [one master generation](../walkthroughs/02-one-master-generation.md), step 9.
- **compaction recall probe**: the hook that fires after a compaction and has the master write what it remembers before it opens any source of truth. See [one master generation](../walkthroughs/02-one-master-generation.md), step 10.
- **charter**: the numbered documents under `master-ops/docs/charter/` that state the harness's rules: execution principles, the dispatch gate, succession, and the rest.
- **boot card**: the succession boot card, the runbook a successor master follows at boot: placement, role state, the model, the predecessor's retirement, and the lineage entry. See [one master generation](../walkthroughs/02-one-master-generation.md).
- **Recovery Flow**: the numbered procedure, steps 0 to 6, a master follows after an abnormal end; `master-recover` runs it as reads only. See [unit 05](../units/05-read-only-recovery-flow/).
- **Trace Archive**: the history index of past sessions. Charter §8 has a master query it only when the handoff, the ledger, and Git together do not answer a question. See [unit 05](../units/05-read-only-recovery-flow/).
- **lineage**: the append-only file with one entry per master generation. See [succession](succession.md).

<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
