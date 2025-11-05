import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from utils.custom_excpection import CustomException
from utils.loggers import get_logger
from dotenv import load_dotenv

logger = get_logger(__name__)

st.set_page_config(page_title="Anime Recommendation System", layout="wide")
load_dotenv()

@st.cache_resource

def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommendation System")

query = st.text_input("Enter your anime preferences or description:")

col1,spacer,col2 = st.columns([2, 4, 1])

# if "show_recommendations" not in st.session_state:
#     st.session_state.show_recommendations = False

# with col1:

if st.button("Get Recommendations"):
    try:
        if not query.strip():
            st.warning("Please enter a valid query.")
        else:
            with st.spinner("Fetching recommendations..."):
                recommendation = pipeline.recommend(query)
            st.markdown("Recommended Anime:")
            st.write(recommendation)
                # st.session_state.show_recommendations = True
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
        st.error(f"An error occurred: {ce}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        st.error("An unexpected error occurred. Please try again later.")

# with col2:

if st.button("Clear"):
    query = ""
    st.rerun()
    # st.session_state.show_recommendations = False

# if st.session_state.show_recommendations:
#     try:
#         recommendation = pipeline.recommend(query)
#         st.markdown("### Recommended Anime:")
#         st.write(recommendation)
#     except CustomException as ce:
#         logger.error(f"Custom exception occurred: {ce}")
#         st.error(f"An error occurred: {ce}")
#     except Exception as e:
#         logger.error(f"Unexpected error occurred: {e}")
#         st.error("An unexpected error occurred. Please try again later.")
# else:
#     query = ""
#     st.rerun()
