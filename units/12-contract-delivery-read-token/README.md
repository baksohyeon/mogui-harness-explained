# 12. Contract delivery and read token

**Mechanism.** With `--contract`, dispatch copies the contract to a delivery directory, compares the copy byte for byte, appends `ack-${SHA:8:12}`, and writes the delivered path into the spec. It then appends each standing-rule block the contract's front matter names.

**Failure it prevents.** The token gives the worker a value that proves the delivered copy was opened. A missing standing-rules file exits 10 before dispatch, and a missing named block exits 3 during append.

<p align="center"><img src="../../assets/units/12-contract-delivery-read-token.svg" alt="contract delivery verifies the copy, adds a token, and appends standing rules" width="100%"></p>

## Example (synthetic)

```
SHA=abcdef0123456789beef; printf 'ack-%s\n' "${SHA:8:12}"
ack-23456789beef
```

## Verified in mogui

- Implementation: [`master-ops/scripts/dispatch`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/dispatch), [`master-ops/rules/standing-rules.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/rules/standing-rules.md), [`master-ops/docs/runbooks/contract-conventions.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/docs/runbooks/contract-conventions.md)
- Tests: [`master-ops/scripts/test-dispatch-runtime.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-dispatch-runtime.sh), [`master-ops/scripts/test-dispatch-smoke.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-dispatch-smoke.sh)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
