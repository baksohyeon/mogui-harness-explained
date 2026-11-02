<p align="center"><img src="assets/how-it-fits.svg" width="760" alt="mogui-ADE-orchestrator holds the verified implementation; this repo is a small explanatory sample"></p>

# agent-harness-change-ledger

A small explanatory sample of one idea from [mogui-ADE-orchestrator](https://github.com/baksohyeon/mogui-ADE-orchestrator), where it is implemented and tested:

> every harness change is a prediction, and the next run decides whether it stays.

```mermaid
flowchart LR
    P["change + predicted fixes / regressions"] --> R["run evals"] --> S{"predictions hit?"}
    S -->|yes| K["keep"]
    S -->|no| V["revert"]
```

Verified version: [acceptance loop](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/main/src/master_runtime/core/acceptance), [tests](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/main/tests), [CI gates](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/main/.github/workflows/gates.yml).

Here: [`manifest.schema.json`](manifest.schema.json) and should-fire / should-not-fire eval pairs in `evals/behavioral/`. Synthetic data only.

Background: [AHE paper](https://arxiv.org/abs/2604.25850).

---

<p align="center"><img src="assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
