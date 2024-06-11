#!/usr/bin/python3

from os import environ
from huggingface_hub import login
from transformers import AutoTokenizer
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

def Llama3(locally = False):
  login(token = config.huggingface_token)
  tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3-8B-Instruct')
  if locally:
    llm = HuggingFacePipeline.from_model_id(
      model_id = "meta-llama/Meta-Llama-3-8B-Instruct",
      task = "text-generation",
      device = 0,
      pipeline_kwargs = {
        "max_length": 8192,
        "do_sample": False,
        "temperature": 0.6,
        "top_p": 0.9,
        "eos_token_id": [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|eot_id|>")],
        "use_cache": True,
        "return_full_text": False
      }
    )
  else:
    environ['HUGGINGFACEHUB_API_TOKEN'] = config.huggingface_token
    llm = HuggingFaceEndpoint(
      endpoint_url = "meta-llama/Meta-Llama-3-8B-Instruct",
      task = "text-generation",
      #max_length = 8192,
      do_sample = False,
      temperature = 0.6,
      top_p = 0.9,
      #eos_token_id = [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|eot_id|>")],
      #use_cache = True,
    )
  return tokenizer, llm

def CodeLlama(locally = False):
  login(token = config.huggingface_token)
  tokenizer = AutoTokenizer.from_pretrained('meta-llama/CodeLlama-7b-Instruct-hf')
  if locally:
    llm = HuggingFacePipeline.from_model_id(
      model_id = 'meta-llama/CodeLlama-7b-Instruct-hf',
      task = 'text-generation',
      device = 0,
      pipeline_kwargs = {
        "max_length": 16384,
        "do_sample": False,
        "temperature": 0.8,
        "top_p": 0.8,
        "use_cache": True,
        "return_full_text": False
      }
    )
  else:
    environ['HUGGINGFACEHUB_API_TOKEN'] = config.huggingface_token
    llm = HuggingFaceEndpoint(
      endpoint_url = 'meta-llama/CodeLlama-7b-Instruct-hf',
      task = 'text-generation',
      #max_length = 16384,
      do_sample = False,
      temperature = 0.8,
      top_p = 0.8,
      use_cache = True
    )
  return tokenizer, llm
