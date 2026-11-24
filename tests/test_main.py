import pytest

from text_tool.main import main

def test_main_file_not_found():
    with pytest.raises(SystemExit)as exc_info:
        main("data/kkjkj.txt")
    assert exc_info.value.code==1

def test_main_decode_error(tmp_path):
    bad=tmp_path/"bad.txt"
    bad.write_bytes("你好".encode("gbk"))
    with pytest.raises(SystemExit)as exc_info:
        main(str(bad))
    assert exc_info.value.code==1

def test_main_normal(tmp_path,capsys):
    f=tmp_path/"a.txt"
    f.write_text("你好世界。你好大家！",encoding="utf-8")

    main(str(f))

    out=capsys.readouterr().out
    assert "你好世界" in out
    assert "你好大家" in out