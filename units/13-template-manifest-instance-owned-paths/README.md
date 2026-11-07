# 13. Template manifest and instance-owned paths

**Mechanism.** `template-apply` builds a manifest-based dry-run plan, refuses instance-owned and unclaimed paths, and asks for the phrase `apply` before writing. It replaces each file atomically after preflighting the planned sources and destinations.

**Failure it prevents.** An upgrade can leave `workspace-card/LOCAL.md` untouched and reject a path the manifest does not claim. Missing template files and unresolved placeholders stop the write before confirmation.

<p align="center"><img src="../../assets/units/13-template-manifest-instance-owned-paths.svg" alt="the template manifest controls dry-run, refusal, confirmation, and atomic writes" width="100%"></p>

## Example (synthetic)

```sh
python3 /tmp/ops/scripts/template-apply --ops /tmp/instance --template /tmp/template --attempt workspace-card/LOCAL.md --json
"action": "skipped-as-instance-owned"
```

## Verified in mogui

- Implementation: [`scripts/template-apply`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/template-apply), [`scripts/template_common.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/template_common.py), [`MANIFEST.json`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/MANIFEST.json), [`TEMPLATE-VERSION`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/TEMPLATE-VERSION)
- Tests: [`tests/test_template_check_apply.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_template_check_apply.py), [`tests/test_template_apply_card_extension.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_template_apply_card_extension.py)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
