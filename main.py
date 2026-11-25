"""The 3AM Fridge Text — one line a smart fridge would text at 3am.

Writes one line (<=140 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

TEXT = (
    "3am: I'm holding your leftovers. I've thought about this. "
    "We both know you're getting up. Bring a plate."
)

path = "/output/entry.txt"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    fh.write(TEXT)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == TEXT, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")