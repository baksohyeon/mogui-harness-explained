# 24. Instance runtime config and workspace descriptor

**In one breath.** Facts about one installation, which CLI hosts the master, where each runtime keeps its transcripts, which repositories are in the workspace and what may not be done to them, live in two instance-owned JSON files that onboarding writes. Every reader resolves a value the same way: environment override, then the file, then an honest "unconfigured". Nothing invents a default.

**When it runs.** Before dispatch, when the wrapper and the model probe need the host runtime, the transcript location, and the list of runtimes a seat has declared unavailable. Also whenever a script asks whether an action, such as a direct commit to `main`, is prohibited for a repository.

**Mechanism.** `instance_runtime_config.py` loads `config/instance-runtime.json`, or the path in `INSTANCE_RUNTIME_CONFIG`. Each fact has an environment override (`MOGUI_MASTER_HOST_RUNTIME`, `MOGUI_TRANSCRIPT_GLOB`, `MOGUI_PRODUCT_REPO`), then the file, then `unconfigured`. The template ships only an example file; the real one is instance-owned and the template never overwrites it. The same file carries `unavailable_runtimes`, a map of runtimes the seat has declared out of service with a reason and an until-date, which the dispatch wrapper validates in one pass and refuses to dispatch to. For the codex runtime the same file may set `codex_reasoning_effort` and `codex_bypass_approvals_and_sandbox`; an effort value the wrapper does not know is refused, because the start-screen check would wait for a footer that never appears. `workspace_descriptor.py` loads `config/workspace-descriptor.json`, the inventory of sibling repositories under the workspace root: each one's path, role (`product` or `ops`), capabilities (`pr`, `dispatch-target`), and prohibited actions (`direct-main-commit`, `force-push`, and any local name). `workspace-descriptor-check <path> <action>` answers whether the action is prohibited: exit 0 allowed, 1 prohibited, 2 could not decide because the descriptor is unconfigured or invalid.

A third module, `context/`, resolves a workspace manifest against the filesystem into a descriptor of declared and observed repositories. At `v0.5.288` it is a tested library with no caller.

**Failure it prevents.** A template that bakes one machine's username, CLI, or repository list into every install. A wrapper that guesses a transcript path and probes the wrong worker's model. A direct commit to a repository's `main` that the workspace had declared off limits.

## Example (synthetic)

```
$ scripts/workspace-descriptor-check ~/example-workspace/example-product direct-main-commit
prohibited: action=direct-main-commit repo=example-product path=~/example-workspace/example-product
exit=1
$ WORKSPACE_DESCRIPTOR=/nonexistent.json scripts/workspace-descriptor-check ~/example-workspace/example-product force-push
workspace-descriptor-check: descriptor file not found
exit=2
```

## Verified in mogui

- Implementation: [`src/master_runtime/core/instance_runtime_config.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/src/master_runtime/core/instance_runtime_config.py), [`src/master_runtime/core/workspace_descriptor.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/src/master_runtime/core/workspace_descriptor.py), [`scripts/workspace-descriptor-check`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/scripts/workspace-descriptor-check), [`src/master_runtime/core/context/`](https://github.com/baksohyeon/mogui-ADE-orchestrator/tree/v0.5.288/src/master_runtime/core/context/), the `unavailable_runtimes` section of [`master-ops/scripts/dispatch`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/dispatch)
- Tests: [`tests/test_instance_runtime_config.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_instance_runtime_config.py), [`tests/test_workspace_descriptor.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_workspace_descriptor.py), [`tests/test_context_resolver.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/tests/test_context_resolver.py), [`master-ops/scripts/test-dispatch-unavailable-runtime.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-dispatch-unavailable-runtime.sh), [`master-ops/scripts/test-dispatch-codex-instance-config.sh`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.288/master-ops/scripts/test-dispatch-codex-instance-config.sh)

<p align="center"><img src="../../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
