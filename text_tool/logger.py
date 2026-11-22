"""统一的日志配置：所有模块都从这里拿 logger。"""
import logging


def get_logger(name: str = "text_tool") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:  # 防止重复添加 handler
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        logger.addHandler(handler)
    return logger
