"""JSONL logging: append and read episodes."""

import json
from pathlib import Path


def append_episode(filepath: str | Path, episode: dict) -> None:
    """Append one episode (one JSON object) as a single line to the file."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(episode, ensure_ascii=False) + "\n")


def read_episodes(filepath: str | Path) -> list[dict]:
    """Read all episodes from a JSONL file (one JSON object per line)."""
    path = Path(filepath)
    if not path.exists():
        return []
    episodes = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            episodes.append(json.loads(line))
    return episodes
