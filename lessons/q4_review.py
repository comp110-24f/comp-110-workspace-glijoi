"""Dog110"""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Determine if all dogs were good in daycare."""
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = len(scores) == idx + 1

    # let python deal with edge cases
    if is_good:
        if is_last:
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    else:
        return False


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]
print(all_good(pack, 8, 0))

# Mem Diagram in notes
