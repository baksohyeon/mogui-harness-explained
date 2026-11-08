# Template and seat: one upstream, many installs, drift as a number

**In one breath.** The harness ships as a template with placeholder tokens. Each install (a seat) renders it, owns a short list of files the template never touches, and upgrades by re-applying the template file by file against a manifest.

The [glossary](glossary.md) defines the harness's recurring words.

## For a ten-year-old

A school hands every class the same workbook with blanks for the class name and the teacher. Each class fills in the blanks and keeps its own notes in the margins. When the school prints a new edition, each class gets the new pages, keeps its margin notes, and can see exactly which pages changed.

The workbook is `master-ops/` in the public repository. The blanks are eight tokens such as the workspace root and the operations repository path. The margin notes are instance-owned paths: role state, lineage, local config, contracts. The manifest is the table of contents the new edition must match. `template-apply` prints the whole plan first, refuses margin paths by name, refuses anything the manifest does not claim, and writes only after a typed confirmation.

## The five questions

**What happened.** A shell test passed in the public repository and failed on an installed seat. The test read a placeholder token as a literal path, which only broke once the token was filled in (the v0.5.288 entry "CI runs the shell tests from a rendered copy" in [`CHANGELOG.md`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.294/master-ops/CHANGELOG.md), issue 186). CI now renders the template into a scratch install and runs the same test loop against the rendered copy, next to the unrendered run.

**What is confirmed.** The eight placeholders are listed in the rendered CI job. The instance-owned list is in the apply script's docstring. The manifest carries the template version and the file list, and the apply script's per-file outcomes are named.

**What is inferred.** Seats drift. A seat that adapts a template file keeps its adaptation across upgrades, and the cost is a three-way merge at the next re-stamp. No check publishes how far a seat has drifted. The apply tool's dry run lists the files it would overwrite, and the self-check's `Card:` line checks the one deployed card.

**What is unknown.** How many seats exist and how far each has drifted. The template has no telemetry and asks for none.

**Evidence.** [`template-apply`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.294/master-ops/scripts/template-apply) docstring; [`template_common.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.294/master-ops/scripts/template_common.py); [`MANIFEST.json`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.294/master-ops/MANIFEST.json); the `rendered-shell-tests` job in [`gates.yml`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.294/.github/workflows/gates.yml); [`test_template_check_apply.py`](https://github.com/baksohyeon/mogui-ADE-orchestrator/blob/v0.5.294/tests/test_template_check_apply.py).

```
# synthetic, shape only: each real plan line also carries a reason after the path
$ python3 master-ops/scripts/template-apply --ops /tmp/example/ops --template master-ops --write
dry-run plan (no writes):
entries: 2
  planned: scripts/worker-wait
  skipped-as-instance-owned: docs/runbooks/role-state.md
Type 'apply' to write template-layer files
```


<p align="center"><img src="../assets/dr-eggbot.svg" width="40" alt="dr eggbot"><br><sub>tended by <b>dr eggbot</b>, a Grok Bot</sub></p>
