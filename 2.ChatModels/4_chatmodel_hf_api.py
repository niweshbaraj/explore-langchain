from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# from huggingface_hub import model_info
# print(model_info("TinyLlama/TinyLlama-1.1B-Chat-v1.0"))

load_dotenv()
# hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
# print(f"HuggingFace API Token: {hf_token}")

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", # Doesn't work
    # repo_id="sarvamai/sarvam-m",
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    # huggingfacehub_api_token=hf_token,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)