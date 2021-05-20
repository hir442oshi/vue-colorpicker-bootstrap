import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def evaluate_educational_rag(query, vector_store):
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
    return qa.run(query)