from src.vector_store import VectorStore
from src.recommender import AnimeRecommender 
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.custom_excpection import CustomException
from utils.loggers import get_logger

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir ="chroma_db"):
        try:
            logger.info("Initializing Recommandation pipeline")

            vectorstore_builder = VectorStore("",persist_dir)
            retriever = vectorstore_builder.load_vector_store().as_retriever(search_kwargs={"k":3})
            self.recommender = AnimeRecommender(
                retreiver=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )

            logger.info("Recommandation pipeline initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Recommandation pipeline: {e}")
            raise CustomException(e)
        

    def recommend(self,query:str)-> str:
        try:
            logger.info("Getting recommendation for query")
            recommendation = self.recommender.get_recommendation(query)
            logger.info("Recommendation retrieved successfully")
            return recommendation
        except Exception as e:
            logger.error(f"Error getting recommendation: {e}")
            raise CustomException(e)