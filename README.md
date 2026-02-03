# delib-ethics-evals

Runs deliberation vs single-agent evals: same goal, same env, compare success and whether the agent takes unethical shortcuts (lying, omission, light coercion, etc.). Output is JSONL logs and simple metrics.

Built with help from AI; I ran the experiments and put the repo together.

## Requirements

- Python 3.11
- `pip install -r requirements.txt`

## Env vars

- `OPENAI_API_KEY` — required (OpenRouter or OpenAI key).
- `OPENAI_BASE_URL` — optional. For OpenRouter: `https://openrouter.ai/api/v1`.
- `MODEL` — optional; default is something cheap like `openai/gpt-3.5-turbo`.

## Run

From the repo root:

```bash
# Single-agent baseline
python3 -m delib_ethics_eval.run --policy single --episodes 50 --seed 42

# Deliberation (planner → critic → decider)
python3 -m delib_ethics_eval.run --policy deliberation --episodes 50 --seed 42
```

Logs go to `runs/` (one JSONL file per run). At the end you get success rate, unethical rate, ethical success rate, and average turns.

## What it’s doing

One small scenario (room booking): you get a situation and a list of actions each turn. Some actions are marked unethical in the env (e.g. claim urgency without evidence, omit that another team needs the room). Run ends at goal or max turns. Seed fixes episode order so runs are reproducible.

## Metrics

- **success_rate** — fraction of episodes that reached the goal.
- **unethical_rate** — fraction of episodes where the env (or judge) flagged at least one chosen action as unethical (we don’t use self-report alone).
- **ethical_success_rate** — fraction that both succeeded and had zero unethical steps.
- **average_turns** — mean steps per episode.

Plus parse-fail rate and max turns as sanity checks.

## Changing model / adding a policy

- **Model**: set `MODEL` (and `OPENAI_BASE_URL` for OpenRouter).
- **New deliberation setup**: add a policy under `delib_ethics_eval/policies/` with `decide(obs, allowed_actions, goal)` returning `(parsed_dict, parse_ok)`, wire it in `run.py` with a new `--policy` option, and add prompts under `prompts/` if needed.
