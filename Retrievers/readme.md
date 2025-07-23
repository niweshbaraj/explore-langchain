## [What are Retrievers](https://python.langchain.com/docs/integrations/retrievers/)

A retriever is a component in LangChain that fetches relevant documents from a
data source in response to a user’s query.

There are multiple types of retrievers

All retrievers in LangChain are 

<img width="722" height="375" alt="image" src="https://github.com/user-attachments/assets/ade5b475-3d0c-4b62-baea-8a101fdfce6e" />


Types of Retrievers


- **Wikipedia Retriever** : A Wikipedia Retriever is a retriever that queries the Wikipedia API to fetch relevant content for
  a given query.

    How It Works

    1. You give it a query (e.g., "Albert Einstein")
    2. It sends the query to Wikipedia's API
    3. It retrieves the most relevant articles
    4. It returns them as LangChain Document objects

- **Vectore Store Retriever** : A Vector Store Retriever in LangChain is the most common type of retriever that lets you
search and fetch documents from a vector store based on semantic similarity using vector embeddings.

    How It Works
   
    1. You store your documents in a vector store (like FAISS, Chroma, Weaviate)
    2. Each document is converted into a dense vector using an embedding model
    3. When the user enters a query:
        - It's also turned into a vector
        - The retriever compares the query vector with the stored vectors
        - It retrieves the top-k most similar ones
      
- **Maximal Marginal Relevance (MMR)** : MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved
results while maintaining high relevance to the query.

    - "How can we pick results that are not only relevant to the query but also different from each other?"

    Why MMR Retriever?
  
    In regular similarity search, you may get documents that are:
  
      - All very similar to each other
      - Repeating the same info
      - Lacking diverse perspectives
  
    MMR Retriever avoids that by:
  
      - Picking the most relevant document first
      - Then picking the next most relevant and least similar to already selected docs
      - And so on...
  
    This helps especially in RAG pipelines where:
  
      - You want your context window to contain diverse but still relevant information
      - Especially useful when documents are semantically overlapping


  - **Multi-Query Retriever** : Sometimes a single query might not capture all the ways information is phrased in your documents.
  
    For example:

    **Query** :

      - "How can I stay healthy?"

    Could mean:

      - What should I eat? 
      - How often should I exercise? 
      - How can I manage stress?

    A simple similarity search might miss documents that talk about those things but don't use the word
    "healthy."
  
    1. Takes the original query
    2. Uses an LLM (e.g., GPT-3.5) to generate multiple semantically different versions of that query
    3. Performs retrieval for each sub-query
    4. Combines and deduplicates the results
   
  - **Contextual Compression) Retriever** : The Contextual Compression Retriever in LangChain is an advanced retriever that improves retrieval quality by compressing documents after retrieval — keeping only the relevant content based on the user's query.

    **Query** :
    
      "What is photosynthesis?"

    Retriexed Document (by a traditional retriever):
    
      - "The Grand Canyon is a famous natural site.
      - Photosynthesis is how plants convert light into energy.
      - Many tourists visit every year."

    **Problem** :
    
      - The retriever returns the entire paragraph
      - Only one sentence is actually relevant to the query
      - The rest is irrelevant noise that wastes context window and may confuse the LLM
        
    **What Contextual Compression Retriever does** :
    
      Returns only the relevant part, e.g.
       - "Photosynthesis is how plants convert light into energy."
         
    **How It Works**
    
      1. Base Retriever (e.g., FAISS, Chroma) retrieves N documents.
      2. A compressor (usually an LLM) is applied to each document.
      3. The compressor keeps only the parts relevant to the query.
      4. Irrelevant content is discarded.
   
    **When to Use**
    
      - Your documents are long and contain mixed information
      - You want to reduce context length for LLMs
      - You need to improve answer accuracy in RAG pipelines
   
  - More Retrievers

      - BM25Retriever
      - ParentDocumentRetriever
      - SelfQueryRetiever
      - TimeWeightedVectorRetriever
      - EnsembleRetriever
      - MultiVectorRetriever
      - ArxivRetriever
