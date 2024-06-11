# Introduction

this project implement abstractive summarization algorithm with LLM

# Install prerequisite

```shell
python3 -m pip install -r requirements.txt
sudo apt install tesseract-ocr
```

# Usage

```shell
python3 main.py --input <path/to/document> [--locally] [--recursively] [--instruction <instruction>]
```

| parameters | meaning |
|------------|---------|
| input      | path to input document file |
| locally    | whether to run model on local GPU |
| recursively | whether to summarize multiple chunks to one summary |
| instruction | extra instruction to LLM |

