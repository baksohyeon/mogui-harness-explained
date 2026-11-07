# 11. Rendered shell-test lane

**Mechanism.** The `rendered-shell-tests` job renders `master-ops` into a scratch install with `template-apply --write`. It runs every rendered `scripts/test-*.sh` file and reports each exit code and `SKIP` line.

**Failure it prevents.** A shell test can pass while `{{...}}` tokens remain and fail after rendering. The lane also records when an instance-owned file is absent from a template-only checkout.

<p align="center"><img src="../../assets/units/11-rendered-shell-test-lane.svg" alt="template rendering feeds the shell-test loop and reports results" width="100%"></p>

## Example (synthetic)

```
bash /tmp/ops/scripts/test-seat-check.sh
SKIP: ./scripts/harness-selfcheck.sh not found (instance-owned, not part of a template-only checkout)
```

## Verified in mogui

- Implementation: [`gates.yml`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/.github/workflows/gates.yml), [`scripts/template-apply`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/template-apply)
- Tests: [`scripts/test-seat-check.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-seat-check.sh), [`scripts/test-template-currency-line.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-template-currency-line.sh)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
