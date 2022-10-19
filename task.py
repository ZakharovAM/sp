from typing import Sequence, Any

s = "aabbbbbccс"

lst = [["a", "a"], ["b"], ["c"]]


def get_subseq_equal_items(
    sequence: Sequence[Any],
) -> list[list[Any], ...]:
    subseq = []
    result = [subseq]
    last_c = sequence[0]
    subseq.append(last_c)
    for c in sequence[1:]:
        if last_c == c:
            result[-1].append(c)
        else:
            result.append([])
            result[-1].append(c)

        last_c = c

    return result
