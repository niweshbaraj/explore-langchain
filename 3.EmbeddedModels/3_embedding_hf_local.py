from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "What is the capital of India?"

text_vector = embedding.embed_query(text)
print(str(text_vector))

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

doc_vector = embedding.embed_documents(documents)

print(str(doc_vector))