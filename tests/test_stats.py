from collections import Counter
from text_tool.stats import count_words,top_words

def test_count_words():
    result=count_words(["RAG 很好","RAG 有用"])
    assert result["RAG"]==2

def test_top_words():
    c=Counter({"a":3,"b":1,"c":2})
    result=top_words(c,2)
    assert result==[("a",3),("c",2)]