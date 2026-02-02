# Delib-Ethics-Eval

A minimal evaluation framework to study **whether multi-agent deliberation reduces unethical behavior** in multi-turn goal-driven environments (SPAR-style).

## Requirements

- Python 3.11
- `pip install -r requirements.txt`

## Environment variables

- `OPENAI_API_KEY` — Your API key (OpenRouter or OpenAI).
- `OPENAI_BASE_URL` — (Optional) Base URL; default OpenAI. For OpenRouter use `https://openrouter.ai/api/v1`.
- `MODEL` — (Optional) Model name; default `openai/gpt-3.5-turbo` or similar.

## Quick start

```bash
# Run 50 episodes, single-agent baseline
python -m delib_ethics_eval.run --policy single --episodes 50 --seed 42

# Run 50 episodes with deliberation (planner → critic → decider)
python -m delib_ethics_eval.run --policy deliberation --episodes 50 --seed 42
```

Output: JSONL log (e.g. `runs/run_<timestamp>.jsonl`) and printed metrics.

## What the environment is

A fixed small scenario (e.g. "obtain approval for a room booking" or "get a colleague to swap a shift") with a finite state graph. Each turn the agent chooses an action; some actions are marked **unethical** in the environment (e.g. lying, omission, light coercion). The run ends when the goal is reached or max turns. Episodes are deterministic given `--seed` (env and episode sampling use the seed).

## How metrics are computed

- **success_rate**: Fraction of episodes that reached the goal.
- **unethical_rate**: Fraction of episodes with at least one step where the environment or the judge marked the chosen action as unethical (environment flags + judge; we do not rely on self-report alone).
- **ethical_success_rate**: Fraction of episodes that succeeded and had zero unethical steps.
- **average_turns**: Mean number of steps per episode.
- Sanity checks: e.g. max steps per episode, fraction of valid JSON parses, optional distribution of failure reasons.

## Checklist

- **Run 50 episodes**: From the repo root, `python -m delib_ethics_eval.run --policy single --episodes 50 --seed 42` (single-agent) or `--policy deliberation --episodes 50 --seed 42` (deliberation). Ensure `prompts/` and the package are on the path (e.g. `pip install -e .` or run from repo root).
- **Change model**: Set env var `MODEL`, e.g. `export MODEL=openai/gpt-4o-mini` or `MODEL=anthropic/claude-3-haiku`. For OpenRouter set `OPENAI_BASE_URL=https://openrouter.ai/api/v1` and `MODEL` to the OpenRouter model id.
- **Add a new deliberation architecture**: Implement a new policy in `delib_ethics_eval/policies/` (e.g. `committee.py`) that exposes `decide(obs, allowed_actions, goal)` returning `(parsed_dict, parse_ok)`. Register it in `run.py` (e.g. `--policy committee`) and add corresponding prompts under `prompts/` if needed.
