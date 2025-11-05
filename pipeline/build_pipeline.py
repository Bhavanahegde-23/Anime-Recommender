from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStore
from utils.loggers import get_logger
from utils.custom_excpection import CustomException
import os
from dotenv import load_dotenv

logger = get_logger(__name__)
load_dotenv()

def main():
    try:
        logger.info("Starting the Anime Recommendation Pipeline")
        # Step 1: Load and process the data
        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/processed_anime.csv")
        processed_data_path = loader.load_process()
        logger.info(f"Data processed and saved to {processed_data_path}")

        # Step 2: Build the vector store
        vector_store = VectorStore(processed_data_path)
        vector_store.create_vector_store()
        logger.info("Vector store built and persisted successfully")

    except Exception as e:
        logger.error(f"Error in building the pipeline: {e}")
        raise CustomException(e)


if __name__ == "__main__":
    main()