import asyncio
from gllm_inference.lm_invoker import OpenAILMInvoker
from gllm_inference.model import OpenAILM

lm_invoker = OpenAILMInvoker(OpenAILM.GPT_5_NANO)
response = asyncio.run(lm_invoker.invoke("What is the capital city of Indonesia?"))
print(f"Response: {response}")
