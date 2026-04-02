# IPL Win Predictor

An end-to-end Machine Learning project that predicts the **live win probability** of an IPL match based on real-time inputs like current score, overs completed, wickets lost, and run rates. Built with Scikit-learn for the model and Streamlit for the interactive web app.

---

## What This Project Does

During a live IPL match (second innings), you can enter the current match situation and the app will instantly predict:

- **Win probability (%)** for the batting team
- **Win probability (%)** for the bowling team

The model is trained on historical IPL match and delivery data using **Logistic Regression**, achieving **~82% accuracy**.

---

## Project Structure

```
IPL-win-predictor/
|-- .gitignore
|-- README.md
|-- ipl.ipynb
|-- ipl_predictor.py
|-- pipe.pkl
|-- matches.csv
|-- deliveries.csv
|-- requirements.txt
```

| File | Purpose |
|---|---|
| `ipl.ipynb` | Step-by-step notebook: data loading, preprocessing, feature engineering, model training, and saving the model |
| `ipl_predictor.py` | The Streamlit app - run this to launch the web interface |
| `pipe.pkl` | The pre-trained ML pipeline (already included - no need to retrain unless you want to) |
| `matches.csv` | Match-level IPL data (teams, venues, results, etc.) |
| `deliveries.csv` | Ball-by-ball delivery data used to compute features like run rate |
| `requirements.txt` | All Python libraries needed to run the project |

---

## Prerequisites

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - comes bundled with Python

To check if Python and pip are installed, run:
```bash
python --version
pip --version
```

---

## How to Run the App

### Step 1 - Download / Extract the Project

If you downloaded the ZIP file, extract it. You should see the project folder.

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and navigate into the project folder:

```bash
cd path/to/IPL-win-predictor
```

### Step 2 - (Recommended) Create a Virtual Environment

```bash
python -m venv venv

# Activate on Mac/Linux:
source venv/bin/activate

# Activate on Windows:
venv\Scripts\activate
```

You will know it is active when you see `(venv)` at the start of your terminal prompt.

### Step 3 - Install Dependencies

```bash
pip install -r requirements.txt
```

This will install: streamlit, pandas, numpy, scikit-learn, matplotlib, and altair.

> This may take a minute or two depending on your internet speed.

### Step 4 - Run the Streamlit App

```bash
streamlit run ipl_predictor.py
```

Your browser will automatically open at:
```
http://localhost:8501
```

---

## Using the App

Once the app is open in your browser:

1. **Select the Batting Team** - the team currently batting in the second innings
2. **Select the Bowling Team** - the team that batted first
3. **Select the Host City** - where the match is being played
4. **Enter the Target** - runs scored by the team that batted first
5. **Enter the Current Score** - runs scored so far in the second innings
6. **Enter Overs Completed** - how many overs have been bowled (e.g. 12.3)
7. **Enter Wickets Out** - how many wickets the batting team has lost
8. Click **Predict Probability**

> Note: Predictions are for the **second innings only**.

---

## Exploring the Notebook (Optional)

The Jupyter Notebook `ipl.ipynb` walks through the full ML pipeline:

1. Loading `matches.csv` and `deliveries.csv`
2. Merging and preprocessing the data
3. Feature engineering (runs left, balls left, current run rate, required run rate, etc.)
4. Training a Logistic Regression model inside a Scikit-learn Pipeline
5. Evaluating accuracy (~82%)
6. Saving the trained model to `pipe.pkl`

To open the notebook:

```bash
pip install jupyterlab
jupyter lab
```

---

## Model Details

| Detail | Value |
|---|---|
| Algorithm | Logistic Regression |
| Framework | Scikit-learn Pipeline with ColumnTransformer |
| Accuracy | ~82% |
| Output | Win probability for both teams |

**Features used:**

| Feature | Description |
|---|---|
| `batting_team` | Which team is batting in the second innings |
| `bowling_team` | Which team is bowling (batted first) |
| `city` | Match venue |
| `runs_left` | Runs still needed to win |
| `balls_left` | Balls remaining in the innings |
| `wickets` | Wickets in hand (10 - wickets lost) |
| `total_runs_x` | Target set by the first team |
| `currentrr` | Current run rate |
| `requiredrr` | Required run rate |

---

## Troubleshooting

**`pipe.pkl not found` warning in the app**
Make sure you are running the app from inside the project folder:
```bash
streamlit run ipl_predictor.py
```

**`ModuleNotFoundError`**
Run:
```bash
pip install -r requirements.txt
```

**`streamlit: command not found`**
Try:
```bash
python -m streamlit run ipl_predictor.py
```

**Port already in use**
Streamlit will automatically pick the next available port and show you the URL in the terminal.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | ML model and preprocessing pipeline |
| Matplotlib | Visualization in the notebook |
| Streamlit | Interactive web app |
| Pickle | Model serialization |

---

## Future Improvements

- Improve model accuracy using advanced ensemble methods (XGBoost, Random Forest)
- Add historical season-by-season comparison
- Include more recent IPL seasons in the dataset
- Add an over-by-over win probability chart inside the app# IPL Win Predictor

