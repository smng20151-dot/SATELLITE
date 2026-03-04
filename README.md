# 📊 CSV Comparison Dashboard (Streamlit Project)

## 📌 Project Overview

This project is a Streamlit-based web application that compares two CSV files stored locally inside the project folder.

The application allows users to:

- Load two predefined CSV files
- Preview datasets
- Select numeric columns
- Generate Line or Bar chart comparisons
- Merge datasets using a common column
- View statistical summaries

This project is suitable for:
- Academic submission
- Internship demonstration
- Research data comparison
- Offline analytics projects

---

## 📁 Project Structure

csv_compare_dashboard/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
│
└── data/
    ├── file1.csv
    └── file2.csv


---

## 📂 CSV File Format

Both CSV files should follow a structured format.

Example:

### file1.csv

Date,Sales,Profit  
2025-01-01,100,20  
2025-01-02,150,30  
2025-01-03,200,50  

### file2.csv

Date,Sales,Profit  
2025-01-01,120,25  
2025-01-02,170,40  
2025-01-03,220,60  

Requirements:
- At least one common column (e.g., Date)
- At least one numeric column (e.g., Sales, Profit)

---

## ⚙️ Installation

Make sure Python 3.8+ is installed.

### Step 1: Install Dependencies

pip install -r requirements.txt

---

## ▶️ Run the Application

Inside the project folder, execute:

python -m streamlit run app.py

The application will open automatically in your browser at:

http://localhost:8501

---

## 📊 Features

✔ Load CSV files from local data folder  
✔ Data preview  
✔ Dynamic column selection  
✔ Line chart comparison  
✔ Bar chart comparison  
✔ Merge functionality  
✔ Statistical summary  

---

## 🧠 Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib

---

## 🚀 Future Improvements (Optional Enhancements)

- Correlation heatmap
- Date-based filtering
- Interactive Plotly charts
- Sidebar filters
- Multi-page dashboard
- Cloud deployment

---

## 👨‍💻 Author

RAMYA AR  
SMNG ACADEMY  

---

## 📜 License

This project is for educational purposes.
