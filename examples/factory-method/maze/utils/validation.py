from typing import Dict, TypeVar
from itertools import chain

T = TypeVar("T")


def get_cycles(paths: Dict[T, T]):
    found_cycles = []
    for key in paths:
        is_in_cycle = key in chain(*found_cycles)
        if is_in_cycle:
            continue
        has_cycle = False
        seen_current_cycle = set()
        current_key = key
        while current_key is not None and not has_cycle:
            if current_key in seen_current_cycle:
                has_cycle = True
                found_cycles.append(seen_current_cycle)
            seen_current_cycle.add(current_key)
            current_key = paths.get(current_key)

    return found_cycles
