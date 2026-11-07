# Glossary

Thirty-six words the unit pages use without stopping to explain them. Each line says what the word means in this harness and where to read more. The harness runs on Orca, a terminal host with an orchestration layer; the words marked (Orca) come from it.

## People and roles

- **owner**: the person the master works for. The owner approves proposals and merges. See [role lock](role-lock.md).
- **master**: the one agent the owner talks to in a workspace. It plans, dispatches, verifies, and never writes product code itself. See [role lock](role-lock.md).
- **worker**: an agent the master starts to do one contract in its own checkout. See [worker territory](worker-territory.md).
- **generation**: one master session, from boot to retirement. See [succession](succession.md).

## Places

- **workspace**: the directory tree one master is responsible for: an operations repository plus one or more product repositories.
- **product repository**, **product root**: a repository that holds the software being built. Only workers write there. See [unit 09](../units/09-product-path-write-guard-hook/).
- **operations repository**: the master's own repository: contracts, runbooks, lineage, local config. The template renders into it.
- **worktree**: a second checkout of a repository on its own branch in its own directory; every worker gets one. See [unit 06](../units/06-worker-wait-and-reap/).
- **pane**, **terminal**, **handle** (Orca): one terminal session, and the id Orca gives it. A worker runs in a pane; the master reads and closes panes by handle.

## Units of work

- **Run** (Orca): the orchestration session a master owns; tasks and worker messages bind to it.
- **task** (Orca): one dispatched piece of work with an id and a status.
- **dispatch** (Orca): injecting a task into a worker's pane, and the record of that injection.
- **contract**: the file the master writes for a worker: branch, files it may write, verification to paste into the pull request. See [unit 12](../units/12-contract-delivery-read-token/).
- **spec**: the short task text the worker sees first; the contract is its authority.
- **standing rules**: named rule blocks a contract can pull in by name, appended to the spec. See [unit 12](../units/12-contract-delivery-read-token/).
- **read token**, **acknowledgement token**: a short string appended to the delivered contract; a worker that quotes it proves it opened the file. See [unit 12](../units/12-contract-delivery-read-token/).
- **worker_done**: the message a worker sends when its task is finished, with an outcome of succeeded or failed.

## Gates and checks

- **dispatch gate**: the check every dispatch passes: budget, routing, model tier, fan-out. See [unit 02](../units/02-dispatch-tier-fanout-gate/).
- **tier policy**, **fan-out**: the table that says which model tiers workers may use, and how many workers of one tier may run at once. See [unit 02](../units/02-dispatch-tier-fanout-gate/).
- **ledger**: the append-only file where each dispatch decision is recorded. See [unit 07](../units/07-dispatch-timeline-join/).
- **model probe**, **rollout**: reading the model name out of the worker's own transcript file (a rollout, in the codex host's terms) instead of trusting the declared name. See [unit 03](../units/03-transcript-model-identity-probe/).
- **product-path guard**: the hook that blocks a master's writes into a product root. See [unit 09](../units/09-product-path-write-guard-hook/).
- **redaction scan**: the pre-push scan for secrets and internal identifiers; exit 2 means it could not decide. See [unit 08](../units/08-scope-stating-redaction-scan/).
- **fail closed**: when a check cannot run, treat the result as a block. See [fail closed](fail-closed.md).
- **self-check**: the boot script that prints one measured line per harness layer. See [measured, confirmed, inferred](measured-not-assumed.md).
- **hook**: a small script the agent host runs before or after a tool call; the guard and the role-state injector are hooks.

## Template, upgrade, lineage

- **template**: the `master-ops/` tree in the public repository, with placeholder tokens. See [template and seat](template-and-seat.md).
- **seat**: one rendered install of the template, with its own instance-owned files.
- **placeholder**: a `{{TOKEN}}` the render fills in, such as the workspace root.
- **manifest**: the list of files the template owns, with the template version. See [unit 13](../units/13-template-manifest-instance-owned-paths/).
- **instance-owned path**: a file the template never overwrites: role state, lineage, local config, contracts, `LOCAL.md`. See [unit 13](../units/13-template-manifest-instance-owned-paths/).
- **re-stamp**: applying a newer template onto a seat, file by file.
- **workspace card**: the two identical files at the workspace root that tell a session what role it holds. See [unit 14](../units/14-workspace-card-scope-local-file/).
- **changelog fragment**: one dated file per change, folded into the changelog at release time. See [unit 15](../units/15-changelog-fragment-gate/).
- **placement**: proof that a session sits in the intended workspace, worktree, and session namespace. See [unit 04](../units/04-master-succession-placement-check/).
- **lineage**: the append-only file with one entry per master generation. See [succession](succession.md).
