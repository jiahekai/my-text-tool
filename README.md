# my-text-tool

一个用于练习 Python 工程化的小项目：把一段长脚本拆成职责清晰的模块，并加上日志与异常处理。

## 项目结构

```
my-text-tool/
├── text_tool/
│   ├── __init__.py     # 包标识
│   ├── cleaning.py     # 模块1：文本清洗、分句
│   ├── stats.py        # 模块2：词频统计
│   ├── logger.py       # 模块3：日志配置
│   └── main.py         # 入口：串联流程 + 参数校验 + 异常处理
├── data/input.txt      # 示例输入
├── pyproject.toml      # 项目元信息
└── README.md
```

## 运行

```bash
uv venv
uv run python -m text_tool.main data/input.txt
```

## 设计说明

- **模块拆分**：清洗、统计、日志各自独立，改一处不影响其他地方。
- **日志**：统一走 `logger.py`，带时间戳和级别，方便排查问题。
- **异常处理**：文件不存在、编码错误时给出人能看懂的提示，而不是抛堆栈。
- **类型标注**：函数签名标注参数与返回类型，IDE 可提示，代码可读性更强。
