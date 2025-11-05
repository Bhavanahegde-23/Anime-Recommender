from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt
from langchain_classic.chains import RetrievalQA
class AnimeRecommender:
    def __init__(self,retreiver , api_key:str,model_name:str):
        self.llm = ChatGroq(api_key=api_key, model_name=model_name,temperature=0,top_p=1)
        self.prompt = get_anime_prompt()
        self.retrieval_qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retreiver,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommendation(self,query:str):
        result = self.retrieval_qa({"query": query})
        return result['result']