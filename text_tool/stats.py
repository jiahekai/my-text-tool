"""统计模块：只负责数词频。"""
import re
from collections import Counter
from typing import List, Tuple


def count_words(sentences: List[str]) -> Counter:
    words: List[str] = []
    for s in sentences:
        words.extend(re.findall(r"[a-zA-Z\u4e00-\u9fa5]+", s))
    return Counter(words)


def top_words(word_count: Counter, n: int = 10) -> List[Tuple[str, int]]:
    return word_count.most_common(n)
