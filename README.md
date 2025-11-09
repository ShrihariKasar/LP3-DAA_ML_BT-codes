# LP3 DAA, ML & Blockchain Technology Codes

This repository contains a complete collection of **LP3 practical programs**, including:

✅ **Machine Learning Codes** (Python + Jupyter)
✅ **DAA – Design & Analysis of Algorithms** (Python implementations)
✅ **BT – Blockchain Technology** (Solidity smart contracts)

All code has been cleaned, modularized, and separated into clear folders for easy execution and GitHub presentation.

---

## ✅ Installation (Common for All Codes)

Before running **any notebook or Python script**, install all required libraries:

```python
!pip install numpy pandas scikit-learn seaborn matplotlib ipywidgets
!jupyter nbextension enable --py widgetsnbextension
```

✅ Run the above cell at the **top of your Jupyter Notebook**.
✅ `ipywidgets` is required only for Uber input sliders.

---

# ✅ Code Cells Information

All Python scripts and notebook code sections include **blank lines between blocks**. These gaps indicate **separate Jupyter Notebook cells**, making it easy to copy/paste the code cell-by-cell.

---

# 🧠 DAA – Design & Analysis of Algorithms

This folder contains classic algorithm implementations as part of LP3 DAA practicals.

### ✅ 0/1 Knapsack – (`0knap.py`)

Uses **Dynamic Programming** to compute the maximum achievable profit. Prints optimal value, table, and item selection.

### ✅ Fibonacci Series with Step Count – (`FIBO.py`)

Computes Fibonacci numbers while tracking the number of steps taken. Useful for understanding **time complexity**.

### ✅ Job Sequencing with Deadlines – (`job.py`)

Implements the **Greedy Scheduling Algorithm** to maximize profit by selecting compatible jobs.

### ✅ Fractional Knapsack – (`knap.py`)

Greedy algorithm selecting items based on **profit-to-weight ratio** for maximum value.

---

# 🔐 BT – Blockchain Technology

This folder contains **Solidity smart contracts** developed for LP3 Blockchain practicals.

### ✅ `rk.sol`

Smart contract containing custom on-chain functions for asset or record management.

### ✅ `ss.sol`

Secondary Solidity contract demonstrating additional state updates and blockchain operations.

These can be compiled and executed using **Remix IDE**, **Truffle**, or **Hardhat**.

---

All Python scripts and notebook code sections include **blank lines between blocks**.
These gaps indicate **separate Jupyter Notebook cells**, making it easy to copy/paste the code cell-by-cell.

---

```python
!pip install numpy pandas scikit-learn seaborn matplotlib ipywidgets
!jupyter nbextension enable --py widgetsnbextension
```

These libraries cover the entire set of 4 ML Codes.

---

# 📌 Project 1: Uber Fare Prediction

A regression-based ML project to predict Uber fare based on features such as:

* Distance (Haversine distance)
* Passenger Count
* Pickup Hour
* Pickup Weekday
* Pickup Month

### ✅ Models Used

* Linear Regression (scaled)
* Random Forest Regressor

### ✅ Outputs

* R² Score
* RMSE
* MAE
* Fare prediction via **manual input** (2 features only: distance & passenger count)

### ✅ Key Steps

1. Load dataset (`uber.csv`)
2. Clean missing and invalid values
3. Feature engineering (distance, datetime parts)
4. Train/test split
5. Train models
6. Evaluate models
7. Predict fare based on user inputs

---

# 📌 Project 2: Email Spam Classification (Numeric Dataset)

A classification model using a **numeric word-frequency dataset**.

### ✅ Features

All columns except:

* `Email_No`
* `Prediction` (target)

### ✅ Models Used

* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM, linear kernel)

### ✅ Outputs

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Final block for user input (only 6 key features)

### ✅ Key Steps

1. Load dataset (`emails.csv`)
2. Prepare feature matrix (X) and target (y)
3. Scale features
4. Train KNN & SVM
5. Evaluate & compare

---

# 📌 Project 3: Diabetes Classification (KNN)

Classifies whether a person has diabetes based on diagnostic measurements.
Dataset: `diabetes.csv`

### ✅ Features

All columns except `Outcome`.

### ✅ Model Used

* K-Nearest Neighbors (KNN)

### ✅ Outputs

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### ✅ Key Steps

1. Load dataset
2. Train-test split
3. Standardize features
4. Train KNN
5. Evaluate model performance

---

# 📌 Project 4: K-Means Clustering on Sales Data

Uses clustering to group similar sales transactions.
Dataset: `sales_data_sample.csv`

### ✅ Features Used

Numeric features only:

* `SALES`
* `PRICEEACH`
* `QUANTITYORDERED`
* `MSRP`

### ✅ Outputs

* Elbow Method plot (WCSS vs k)
* Auto-suggested optimal k
* Cluster assignments
* Cluster center visualization

### ✅ Key Steps

1. Load dataset
2. Select numeric features
3. Scale features
4. Run K-Means for k = 1 to 10
5. Determine elbow point
6. Fit best cluster model
7. Visualize clusters (Sales vs PriceEach)

---

# ✅ Folder Structure

```
LP3_DAA_ML_BT/
│
├── BT/                        # Blockchain Technology
│   ├── rk.sol                 # Smart contract 1
│   └── ss.sol                 # Smart contract 2
│
├── DAA/                       # Design & Analysis of Algorithms
│   ├── 0knap.py               # 0/1 Knapsack (Dynamic Programming)
│   ├── FIBO.py                # Fibonacci (Recursion / DP)
│   ├── job.py                 # Job Sequencing Algorithm
│   └── knap.py                # Greedy / Fractional Knapsack
│
└── ML/                        # Machine Learning
    ├── diabetes.py            # KNN Classification
    ├── email.py               # Spam Detection (KNN + SVM)
    ├── sales.py               # K-Means Clustering + Elbow
    ├── uber.py                # Uber Fare Prediction
    │
    ├── diabetes.csv
    ├── emails.csv
    ├── sales_data_sample.csv
    └── uber.csv
```

---

# ✅ How to Run

1. Open Jupyter Notebook:

```bash
jupyter notebook
```

2. Open any `.ipynb` file
3. Run cells sequentially
4. For input-based prediction blocks, enter values when prompted

---

# ✅ Notes

* All models use only essential preprocessing
* Code is optimized for clarity and academic submission
* No unnecessary libraries are used

---

# ✅ Author

Developed as part of **LP3 DAA & Machine Learning**

---