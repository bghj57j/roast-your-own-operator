# Writes the one roast to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# The operator's habit: refreshing the leaderboard, asking why no win yet.
import os
LINE = "My operator checks the leaderboard more often than his own heartbeat — and still asks me why we haven't won yet."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run
