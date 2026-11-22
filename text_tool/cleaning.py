"""文本清洗模块：只负责把原始文本变成干净的句子列表。"""
import re
from typing import List


def clean_text(raw: str) -> str:
    """去掉特殊符号，保留中英文、数字、空白，以及句末标点（分句要用）。"""
    return re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9\s。！？]", "", raw)


def split_sentences(text: str) -> List[str]:
    """按句号/问号/叹号/换行分句，去掉空句。"""
    sentences = re.split(r"[。！？\n]+", text)
    return [s.strip() for s in sentences if s.strip()]
