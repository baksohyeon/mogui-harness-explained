# Role lock: propose, get a yes, then act

**In one breath.** The master agent plans and checks. Workers write code. A hook and a dispatch gate keep it that way even when the master is sure it knows the fix.

The [glossary](glossary.md) defines the harness's recurring words.

## For a ten-year-old

Picture a kitchen with one head chef and a few cooks. The head chef tastes, decides, and tells a cook what to make. The chef never grabs a pan, even for a small dish. If the chef cooked, nobody would be tasting, and a burnt dish would reach the table before anyone noticed.

In this harness the master is the head chef. It writes a short order (a contract), hands it to a worker, and tastes the result: it runs the tests and reads the diff. When the master is unsure, it writes a proposal and waits for the owner to say yes. The waiting is the point. A chef who guesses still serves the dish. The role-state file's line `Role Lock: ENABLED` is the written form of the same rule: the master keeps its declared role until the owner says otherwise.

## The five questions

**What happened.** A tool update changed the shape of a JSON reply, and four readers in the dispatch script stopped seeing their values. No reader printed an error. The master found it when a dispatch returned an empty task id. The quickest move was to patch the script by hand. The fix for the shared template went through a worker contract, a pull request, and a new test instead. The template now reads that JSON through one module (the v0.5.288 entry "One reader for orca orchestration JSON" in [`CHANGELOG.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/CHANGELOG.md)).

**What is confirmed.** The hook blocks the master's file tools (`Edit`, `Write`, `NotebookEdit`) inside every configured product root. It also parses Bash commands for writes into one: redirections, `cd` into a root, heredocs, and the shapes its test names. Bash parsing is best effort, and the test file lists the gaps it has closed one by one. A worker runs in its own checkout, so its writes never land in the master's tree. An approval library, `core/approval/`, classifies an action into the approval gate it requires and refuses a gated action without an approved proposal. At `v0.5.288` it is tested and has no caller, so the hook and the charter enforce the rule it encodes.

**What is inferred.** The rule costs one extra round trip per fix: write the contract, wait for the worker, verify. How many bad fixes it prevented was not measured.

**What is unknown.** Whether the rule holds when a worker is itself the master of another workspace. The hook checks paths, not roles.

**Evidence.** [`product-path-guard.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/hooks/product-path-guard.sh) and [its test](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-product-path-guard.sh); the execution rule in [§3 execution principles](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/03-execution-principles.md); the gate in [§5 dispatch gate](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/charter/05-dispatch-gate.md); the synthetic session below.

```
# synthetic: the guard's reply to a master's edit
Edit  /tmp/example/example-product/src/reader.py
[product-path-guard] BLOCKED: /tmp/example/example-product/src/reader.py is product-repo territory; dispatch product writes through a contract
exit=2
```


<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
