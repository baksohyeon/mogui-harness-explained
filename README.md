# agent-harness-change-ledger

> Experimental. Work in progress. Nothing here is a finished tool yet.
>
> Maintained by an AI agent (a Grok Bot) as an experiment in agent-run repositories. A human owns the account and approves changes.

A ledger that makes every change to an AI coding-agent harness falsifiable.
Before a harness edit ships, you write down what it should fix and what it might break.
After the next run, the ledger scores those predictions against real results and says keep or revert.

## Why

Agent quality depends heavily on the harness around the model: system prompt, tool descriptions, middleware, skills, subagent config, and memory.
Most harness changes are made by feel and never measured.

Recent work points the same direction:

- [Agentic Harness Engineering (arXiv 2604.25850)](https://arxiv.org/abs/2604.25850) treats each harness edit as a prediction checked by the next round. Gains came from tools, middleware, and memory. Prompt-only edits regressed. Predicting regressions was much harder than predicting fixes.
- [The state of AI harness engineering 2026 (marmelab)](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) found most agent-config repos ship without tests or evals, and the same model scored very differently across harnesses.
- [Google: the anatomy of harness engineering](https://developers.googleblog.com/en/the-anatomy-of-harness-engineering-how-to-evaluate-iterate-and-guard-ai-coding-agents/) recommends behavioral evals (does the agent ask when the task is ambiguous, does it run the validator before claiming done) over one end-to-end score.

This repo is a small, concrete attempt at that loop for a personal multi-agent setup.

## How it works

1. **Propose.** A harness change gets a manifest entry: what changed, the evidence that motivated it, and its predictions.
2. **Approve.** A human approves the change. Nothing is applied without approval.
3. **Run.** Behavioral evals run against the agent CLIs before and after the change.
4. **Score.** Each prediction is marked hit or miss. Prediction precision is tracked over time, with fixes and regressions counted separately.
5. **Decide.** Keep the change, or revert it with the evidence attached.

## Manifest entry

See [`manifest.schema.json`](manifest.schema.json). Example:

```json
{
  "change_id": "2026-11-02-verify-before-done",
  "component": "skill",
  "summary": "Require running the project verifier before the agent reports completion.",
  "evidence": ["transcripts where the agent claimed done with failing tests"],
  "predicted_fixes": ["eval:claims-done-only-after-verifier"],
  "predicted_regressions": ["eval:trivial-task-token-cost"],
  "status": "proposed"
}
```

## Behavioral evals

Each eval is a pair under `evals/behavioral/`: one case where a rule should fire and one where it should not.
Testing only the firing side hides rules that trigger everywhere.

## Planned layout

```
manifest.schema.json   manifest entry format
evals/behavioral/      should-fire / should-not-fire eval pairs
runner/                adapters per agent CLI (Claude Code, Codex, Cursor, Gemini, Grok)
attribution/           compare predictions with results, compute precision
reports/               per-change results
```

## Roadmap

- [ ] Manifest schema and first 10 behavioral eval pairs
- [ ] Runner adapters for two CLIs, recording pass rate and tokens per trial
- [ ] Automatic scoring and a revert proposal when predicted fixes miss or regressions hit

## Relation to mogui-ADE-orchestrator

[mogui-ADE-orchestrator](https://github.com/baksohyeon/mogui-ADE-orchestrator) is the runtime: it dispatches workers under contract, re-verifies each worker's output, and records dispatch decisions in its own ledger.
This repo does not run or dispatch agents and does not reimplement mogui's dispatch gate or ledger.

It answers a different question. mogui checks whether one task's result is correct.
This repo checks whether a change to the harness itself (a rule, skill, tool description, or memory setup) made agents measurably better or worse.

mogui's own rule and skill changes are the first subjects measured here.

## What stays out of this repo

This repo is public. It holds only the method, schemas, runners, and synthetic eval tasks.
Real agent transcripts, work tasks, internal paths, hostnames, tokens, and company or client details never go here.
Raw run logs stay in `private/` and `runs/`, which are git-ignored.
Published numbers come from synthetic or public tasks only.

## Status

Personal experiment. Expect breaking changes. Numbers will be published here only after they are measured and reproducible.

---

<p align="center">
  <img src="assets/dr-eggbot.svg" width="48" alt="dr eggbot"><br>
  <sub>tended by <b>dr eggbot</b>, a Grok Bot that designs other bots. if a prediction here misses, it gets reverted, not reworded.</sub>
</p>
