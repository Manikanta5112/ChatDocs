import os
import streamlit as st
from tika import parser
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS #facebook AI similarity search
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

def main():
    
    st.set_page_config(page_title="Query your PDF")
    st.header("Query Your PDF")

    uploaded_file = st.file_uploader("Upload your pdf",type="pdf")

    if uploaded_file is not None:

        pdf_parser = parser.from_file(uploaded_file)
        text = pdf_parser['content']

        # spilit ito chuncks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # create embedding
        embeddings = OpenAIEmbeddings(openai_api_key="sk-") # replace with your own open ai key


        knowledge_base = FAISS.from_texts(chunks,embeddings)

        user_question = st.text_input("Ask Question about your PDF:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            llm = OpenAI(
                openai_api_key="sk-" # replace with your own open ai key
            )
            chain = load_qa_chain(llm,chain_type="stuff")
            response = chain.run(input_documents=docs,question=user_question)

            st.write(response)



        # st.write(chunks)

if __name__ == '__main__':
    main()