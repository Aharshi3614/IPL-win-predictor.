🏏 IPL Win Predictor
An end-to-end Machine Learning project that predicts the live win probability of an IPL match based on real-time inputs like current score, overs completed, wickets lost, and run rates. Built with Scikit-learn for the model and Streamlit for the interactive web app.

📌 What This Project Does
During a live IPL match (second innings), you can enter the current match situation and the app will instantly predict:

Win probability (%) for the batting team
Win probability (%) for the bowling team

The model is trained on historical IPL match and delivery data using Logistic Regression, achieving ~82% accuracy.

📁 Project Structure
IPL-win-predictor-main/
│
├── ipl.ipynb            # Jupyter Notebook — full ML pipeline (EDA → training → export)
├── ipl_predictor.py     # Streamlit web app (the main app to run)
├── pipe.pkl             # Pre-trained model saved as a pickle file
├── matches.csv          # Dataset: IPL match-level data
├── deliveries.csv       # Dataset: Ball-by-ball delivery data
├── requirements.txt     # Python dependencies
└── README.md            # This file
File Descriptions
FilePurposeipl.ipynbStep-by-step notebook: data loading, preprocessing, feature engineering, model training, and saving the modelipl_predictor.pyThe Streamlit app — run this to launch the web interfacepipe.pklThe pre-trained ML pipeline (already included — no need to retrain unless you want to)matches.csvMatch-level IPL data (teams, venues, results, etc.)deliveries.csvBall-by-ball delivery data used to compute features like run raterequirements.txtAll Python libraries needed to run the project

⚙️ Prerequisites

Python 3.8 or higher — Download Python
pip — comes bundled with Python

To check if Python and pip are installed, run:
bashpython --version
pip --version

🚀 How to Run the App
Step 1 — Download / Extract the Project
If you downloaded the ZIP file, extract it. You should see the IPL-win-predictor-main/ folder.
Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and navigate into the project folder:
bashcd path/to/IPL-win-predictor-main
Step 2 — (Recommended) Create a Virtual Environment
A virtual environment keeps your project dependencies isolated from other Python projects.
bash# Create the virtual environment
python -m venv venv

# Activate it — on Mac/Linux:
source venv/bin/activate

# Activate it — on Windows:
venv\Scripts\activate
You'll know it's active when you see (venv) at the start of your terminal prompt.
Step 3 — Install Dependencies
Install all required libraries at once using the requirements.txt file:
bashpip install -r requirements.txt
This will install:

streamlit — for the web app interface
pandas — for data manipulation
numpy — for numerical operations
scikit-learn — for the ML model
matplotlib — for data visualization
altair — for interactive charts in Streamlit


⏳ This may take a minute or two depending on your internet speed.

Step 4 — Run the Streamlit App
bashstreamlit run ipl_predictor.py
After a few seconds, your browser will automatically open at:
http://localhost:8501
If it doesn't open automatically, copy that URL and paste it into your browser.

🖥️ Using the App
Once the app is open in your browser:

Select the Batting Team — the team currently batting in the second innings
Select the Bowling Team — the team that batted first
Select the Host City — where the match is being played
Enter the Target — runs scored by the team that batted first
Enter the Current Score — runs scored so far in the second innings
Enter Overs Completed — how many overs have been bowled (e.g. 12.3)
Enter Wickets Out — how many wickets the batting team has lost
Click Predict Probability

The app will display the win probability percentage for both teams.

⚠️ Note: Predictions are for the second innings only. The app is designed to simulate live in-match conditions.


📓 Exploring the Notebook (Optional)
The Jupyter Notebook ipl.ipynb walks through the full ML pipeline:

Loading matches.csv and deliveries.csv
Merging and preprocessing the data
Feature engineering (runs left, balls left, current run rate, required run rate, etc.)
Filtering for valid second-innings situations
Training a Logistic Regression model inside a Scikit-learn Pipeline
Evaluating accuracy (~82%)
Saving the trained model to pipe.pkl

To open the notebook, first install JupyterLab:
bashpip install jupyterlab
Then launch it:
bashjupyter lab
Open ipl.ipynb from the file browser on the left. You can run all cells to retrain the model from scratch, or just explore the analysis.

🤖 Model Details
DetailValueAlgorithmLogistic RegressionFrameworkScikit-learn Pipeline with ColumnTransformerAccuracy~82%OutputWin probability for both teams (via predict_proba)
Features used by the model:
FeatureDescriptionbatting_teamWhich team is batting in the second inningsbowling_teamWhich team is bowling (batted first)cityMatch venueruns_leftRuns still needed to winballs_leftBalls remaining in the inningswicketsWickets in hand (10 − wickets lost)total_runs_xTarget set by the first teamcurrentrrCurrent run raterequiredrrRequired run rate

🛠️ Troubleshooting
pipe.pkl not found warning in the app
Make sure you are running the app from inside the IPL-win-predictor-main/ folder, not a parent directory.
bashcd IPL-win-predictor-main
streamlit run ipl_predictor.py
ModuleNotFoundError
You haven't installed dependencies yet, or your virtual environment isn't active. Run:
bashpip install -r requirements.txt
streamlit: command not found
Streamlit isn't installed or your environment isn't active. Try:
bashpython -m streamlit run ipl_predictor.py
Port already in use
If port 8501 is busy, Streamlit will automatically pick the next available port and show you the URL in the terminal.

🔧 Tech Stack
ToolPurposePythonCore languagePandas & NumPyData processingScikit-learnML model and preprocessing pipelineMatplotlibVisualization in the notebookStreamlitInteractive web appPickleModel serialization

🚀 Future Improvements

Improve model accuracy using advanced ensemble methods (XGBoost, Random Forest)
Add historical season-by-season comparison
Include more recent IPL seasons in the dataset
Add an over-by-over win probability chart inside the app