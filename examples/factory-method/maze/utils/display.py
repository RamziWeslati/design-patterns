from typing import List


def grid_to_str(grid: List[List[str]]):
    return "\n".join(" ".join(line) for line in grid)
