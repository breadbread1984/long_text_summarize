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

# Example

```shell
python3 main.py --input test/US11258057.txt --instruction "Just focus on starting materials in the given examples, chemical formula of electrolyte and numerical data of conductivity" --recursively
```
