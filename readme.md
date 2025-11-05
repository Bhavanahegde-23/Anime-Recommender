#For activating .venv (should find the permanent soution)
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#activate the venv
-  & C:/Users/holla/Desktop/MyProjects/.venv/Scripts/Activate.ps1
#Run setup file for initial setup
- pip install -e .
#Run buildpipeline for creating the db
- python .\pipeline\build_pipeline.py
#Run the application
- streamlit run .\app\app.py