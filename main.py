#!/usr/bin/python3

from absl import flags, app
from os.path import splitext
from langchain.document_loaders import UnstructuredPDFLoader, UnstructuredHTMLLoader, TextLoader
from summarize import summarize
from models import Llama3, CodeLlama

FLAGS = flags.FLAGS

def add_options():
  flags.DEFINE_string('input', default = None, help = 'path to input document')
  flags.DEFINE_enum('model', default = 'llama3', enum_values = {'llama3', 'codellama'}, help = 'model name')
  flags.DEFINE_boolean('locally', default = False, help = 'run model locally')
  flags.DEFINE_float('detail', default = 0.5, help = 'percentage of detail')
  flags.DEFINE_boolean('recursively', default = False, help = 'summary multiple chunks into one summary')
  flags.DEFINE_string('instruction', default = None, help = 'extra instruction')

def main(unused_argv):
  if FLAGS.model == 'llama3':
    tokenizer, llm = Llama3(FLAGS.locally)
  elif FLAGS.model == 'codellama':
    tokenizer, llm = CodeLlama(FLAGS.locally)
  else:
    raise Exception('unknown model!')
  stem, ext = splitext(FLAGS.input)
  if ext == '.txt':
    loader = TextLoader(FLAGS.input)
  elif ext == '.pdf':
    loader = UnstructuredPDFLoader(FLAGS.input, mode = 'single', strategy = "hi_res")
  elif ext in [".htm", ".html"]:
    loader = UnstructuredHTMLLoader(FLAGS.input)
  else:
    raise Exception('unknown format!')
  docs = list()
  docs.extend(loader.load())
  text = ''.join([doc.page_content for doc in docs])
  summary = summarize(text, detail = FLAGS.detail, llm = llm, tokenizer = tokenizer, summarize_recursively = FLAGS.recursively, additional_instructions = FLAGS.instruction)
  print(summary)

if __name__ == "__main__":
  add_options()
  app.run(main)

