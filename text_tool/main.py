"""入口模块：把清洗、统计串起来，负责参数检查和异常处理。"""
import sys
from pathlib import Path

from text_tool.cleaning import clean_text, split_sentences
from text_tool.logger import get_logger
from text_tool.stats import count_words, top_words

# Windows 控制台默认 GBK，强制用 utf-8 输出，避免中文乱码
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

logger = get_logger()


def main(file_path: str) -> None:
    logger.info("开始处理文件: %s", file_path)

    path = Path(file_path)
    if not path.exists():
        logger.error("文件不存在: %s", file_path)
        sys.exit(1)

    try:
        raw = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        logger.error("文件编码不是 utf-8，请先转码: %s", file_path)
        sys.exit(1)

    cleaned = clean_text(raw)
    sentences = split_sentences(cleaned)
    word_count = count_words(sentences)

    logger.info("清洗完成，句数=%d，词数=%d", len(sentences), sum(word_count.values()))
    for word, freq in top_words(word_count):
        print(f"{word}: {freq}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("用法: uv run python -m text_tool.main <文件路径>")
        sys.exit(1)
    main(sys.argv[1])
