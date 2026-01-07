# 🎧 Spotify Extended Streaming History Analysis

A data analysis and visualization project built using **Python** and **Streamlit** to explore Spotify **Extended Streaming History** data. This app provides insights into listening behavior over time, favorite artists, albums, tracks, and detailed year-wise trends through interactive visualizations.
⚠️ Jupyter notebook maybe uploaded in the future but depends on my mood.

---

## 📌 Project Overview

Spotify Extended Streaming History offers a detailed record of your listening activity. This project transforms that raw data into meaningful insights by:

* Analyzing total listening time across different time periods
* Identifying top artists, albums, and tracks
* Exploring year-wise and drill-down trends
* Presenting an overall summary of listening behavior

The application is designed to be **interactive**, **intuitive**, and **insight-driven**.

---

## 🚀 Features

* 📊 **Brief Listening Summary**
  Get a brief overview of your Spotify activity across the entire available time period.

* 📅 **Year-wise Analysis**
  Filter data by year to uncover trends and changes in listening habits.

* 🎵 **Top Artists, Albums & Tracks**
  Discover what you listened to the most based on total minutes played.

* 🧭 **Interactive MPA**
  Use sidebar controls to  explore your MPA.

* 📈 **Visualizations**
  Line charts, pie charts, and bar charts for intuitive understanding.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Web app framework
* **Pandas** – Data manipulation
* **Plotly** – Data visualization

---

## 📂 Dataset

* Source: **Spotify Extended Streaming History**
* Format: JSON files provided by Spotify
* Data includes:

  * Track name
  * Artist name
  * Album name
  * Timestamp
  * Listening duration (ms)



---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/DiwasNeupane10/Spotify-Extended-History-Data-Analysis-Streamlit.git

   ```

2. **Create a virtual environment (optional)**

   ```bash
   ⚠️I have uploaded the dependencies but create a venv .
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app**

   ```bash
   streamlit run ABOUT.py
   ```

---

## 📁 Project Structure

```
spotify-extended-history-analysis/
│
├── ABOUT.py                 # Main Streamlit app
├── data/  # Spotify streaming personalized parquet data
├── pages/ #MPA 
├── utils/                 #  Helper functions
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

---

## 📊 Example Insights

* Total minutes streamed over multiple years
* Most-played artists and albums in specific periods

---

## 🔮 Future Improvements

* Genre-level analysis(**lack of numerical data**)
* Monthly & seasonal trends
* Recommendation insights based on listening patterns(**lack of numerical data**)
* Vision / AI model integration for automated insight generation(**Was Compute Intensive and scratched the idea**)
* Can allow people to gen insghts based on their own data.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 This project is for educational and personal analysis purposes.

---

## 🙌 Acknowledgements

* Spotify for providing Extended Streaming History data
* Streamlit community for excellent documentation and tools

---

✨ *Turn your Spotify data into stories.*
