from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
class VectorStore:
    def __init__(self,processed_csv:str,vector_store_path:str ="chroma_db"):
        self.processed_csv = processed_csv
        self.vector_store_path = vector_store_path
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def create_vector_store(self):
        # Load the processed CSV file
        loader = CSVLoader(file_path=self.processed_csv, encoding='utf-8',metadata_columns=[])
        documents = loader.load()

        # Split the documents into smaller chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=0,
            length_function=len
        )
        texts = text_splitter.split_documents(documents)


        # Create and persist the Chroma vector store
        vector_store = Chroma.from_documents(
            documents=texts,
            embedding=self.embeddings,
            persist_directory=self.vector_store_path
        )
        vector_store.persist()

        return vector_store
    
    def load_vector_store(self):
        # Load the existing Chroma vector store
        vector_store = Chroma(
            persist_directory=self.vector_store_path,
            embedding_function=self.embeddings
        )
        return vector_store