#!/usr/bin/python3

from langchain_core.prompts.prompt import PromptTemplate

def summarize_template(tokenizer, accumulated = False):
  messages = [
    {'role': 'system', 'content': 'Rewrite this text in summarized form.'},
    {'role': 'user', 'content': "{chunk}" if accumulated == False else "Previous summaries:\n\n{accumulated_summaries_string}\n\n{chunk}"}
  ]
  prompt = tokenizer.apply_chat_template(messages, tokenize = False, add_generating_prompt = True)
  template = PromptTemplate(template = prompt, input_variables = ['chunk'] if accumulated == False else ['chunk', 'accumulated_summaries_string'])
  return template
