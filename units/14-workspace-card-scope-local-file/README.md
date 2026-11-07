# 14. Workspace card scope and LOCAL.md

**Mechanism.** The session card opens with a sentence for the owner-appointed master and dispatched workers. It keeps the two card files byte-identical and reads optional instance-owned `LOCAL.md` after the card without overriding its rules.

**Failure it prevents.** A dispatched worker or another workspace session can read a master card as its own role when the scope is unclear. The card keeps instance additions beside the installation while the template leaves them untouched.

<p align="center"><img src="../../assets/units/14-workspace-card-scope-local-file.svg" alt="the workspace card states scope and reads an optional local extension" width="100%"></p>

## Example (synthetic)

```
test -e /tmp/ops/workspace-card/LOCAL.md || echo 'When it is absent, nothing changes.'
When it is absent, nothing changes.
```

## Verified in mogui

- Implementation: [`workspace-card/CLAUDE.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/workspace-card/CLAUDE.md), [`workspace-card/AGENTS.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/workspace-card/AGENTS.md), [`workspace-card/README.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/workspace-card/README.md)
- Tests: [`scripts/test-workspace-card-scope.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-workspace-card-scope.sh), [`tests/test_template_apply_card_extension.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_template_apply_card_extension.py)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
