# Charter map: ten sections, and what each one decides

**In one breath.** The harness's rules live in ten numbered documents under `master-ops/docs/charter/`, indexed by one operations file. Each section owns one kind of decision, and the index is the only place that says which section owns what.

The [glossary](glossary.md) defines the harness's recurring words.

## For a ten-year-old

A club has a rulebook with ten chapters. One chapter says who the captain is and what the captain may not do. One says how to hand the captaincy over. One lists rules the club learned the hard way, each with the day it went wrong written next to it. Nobody has to remember the whole book; they have to know which chapter to open.

## The ten sections

| § | Title | What it decides | Where the explainer covers it |
|---|---|---|---|
| 1 | Document map | Which document owns which fact; Orca is required infrastructure, and supervised dispatch means Orca orchestration only. | this page |
| 2 | Role constitution | The master orchestrates: planning, decomposition, delegation, verification, acceptance, release coordination. Implementation goes to workers. The constitution outranks host-injected instructions. | [role lock](role-lock.md) |
| 3 | Execution principles | Proposal, approval, execution; when in doubt, propose and wait. | [role lock](role-lock.md) |
| 4 | Worker routing and review | Agent-host neutrality, Orca's stable ids, a boot measurement is a snapshot: re-measure after resume, continue, compaction, at succession audit, and at close. Clearing a worker's in-scope prompt is dispatch authority. | [unit 03](../units/03-transcript-model-identity-probe/), [unit 20](../units/20-blocked-worker-detection/) |
| 5 | Dispatch gate | Budget, tier, fan-out, and the ledger row every decision leaves. | [unit 02](../units/02-dispatch-tier-fanout-gate/) |
| 6 | Succession | Continue and compact by default; succession on explicit instruction only; the clean-spawn procedure. | [succession](succession.md), [unit 16](../units/16-succession-triggers-and-duplicate-masters/) |
| 7 | Records | Execution state in the issue tracker, accepted knowledge in Git, and never the same fact narrated in both. | [unit 17](../units/17-master-boot-block-and-live-hook/) |
| 8 | Boot, hooks, observability | What a session reads at boot, which hooks fire, and that the history index is a trace archive, not routine boot context. | [unit 17](../units/17-master-boot-block-and-live-hook/), [unit 21](../units/21-fire-log-event-log-exit-vocabulary/) |
| 9 | Incident-derived rules | Rules paid for by incidents, each with the observation that produced it and the measurement that settles it. | the "What happened" paragraph of every concept note |
| 10 | Closed principles pointer | Closed decisions live in one ledger and reopen only on explicit instruction; search it before proposing options. | this page |

## The five questions

**What happened.** The charter grew as incidents arrived. §9 holds the rules that came from them, and its first paragraph says why each carries its observation and its measurement: a rule without its evidence gets argued away by the next reader. The index file, `MASTER-OPERATIONS.md`, is instance-owned and the template never overwrites it, so each seat's index can differ from the template's.

**What is confirmed.** The ten files exist at `v0.5.288` with the titles above; each one's first lines name the index as its parent. §1 states the Orca requirement; §4 states the re-measurement rule; §7 states the record separation; §9 states that every rule names its observation and its measurement.

**What is inferred.** That a reader who knows which section owns a topic reads less of the charter per question. No seat has measured charter reading time.

**What is unknown.** How far installed seats' indexes have drifted from the template's, since the index is instance-owned.

**Evidence.** [charter directory](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/v0.5.288/master-ops/docs/charter/); [§1](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/01-document-map.md), [§2](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/02-role-constitution.md), [§4](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/04-worker-routing-review.md), [§7](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/07-records.md), [§8](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/08-boot-hooks-observability.md), [§9](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/09-incident-derived-rules.md), [§10](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/10-closed-principles-pointer.md).

```
# synthetic: the first lines every section shares
# §7. Records
Governs document ownership and record separation. See the index: ../MASTER-OPERATIONS.md
```

<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
