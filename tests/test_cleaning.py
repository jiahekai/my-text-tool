#""""测试cleaning模块的两个函数"""
from text_tool.cleaning import clean_text,split_sentences


def test_clean_text_removes_symbols():
 #   """普通的特殊符号应该被删除"""
    assert clean_text("你好@#@世界")=="你好世界"

def test_clean_text_keeps_sentence_marks():
#   """句末的标点需要保留，因为后面分句要用。"""
    assert clean_text("你好！世界。")=="你好！世界。"

def test_split_sentences():
#   """按三种标点分局，且不留空句"""
    assert split_sentences("第一句。第二局！第三句？")==["第一句","第二局","第三句"]
