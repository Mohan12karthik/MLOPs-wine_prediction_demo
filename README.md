# 🍷 Wine Quality Prediction (MLOps Demo)

A simple Machine Learning project to predict wine quality using a **Random Forest Regressor**, with:

- 🚀 **DVC** for dataset versioning
- ☁️ **AWS S3** as the DVC remote
- 🧪 **PyTest** for unit testing
- 🔍 **MLflow** for experiment tracking
- 📦 Organized source code in `src/`

This repository demonstrates a clean, reproducible workflow suitable for MLOps portfolios.

## 📸 S3 Dataset Storage (Screenshots)

Below are the screenshots of the AWS S3 bucket where the dataset is stored as a remote for DVC.

### 📁 S3 Bucket List
![S3 Bucket List](/path/to/your/local/image1.png)

This screenshot shows the bucket created in your AWS account named:


Which acts as the remote store for DVC.

---

### 📂 S3 md5 Folder Contents
![S3 md5 Folder](/path/to/your/local/image2.png)

This screenshot shows the DVC‑generated md5 folder under `files/`, which contains hashed dataset chunks managed by DVC.

---

## 🔍 Why Use DVC + AWS S3?

During **Udemy MLOps Section‑4**, we learn:

✔ How to version datasets using `dvc add`  
✔ How to push dataset files to S3 with `dvc push`  
✔ How the md5 hashing works behind the scenes  
✔ How to keep the dataset out of Git but still versioned

With this approach:
- Git tracks *only pointers* (`.dvc` files)
- S3 stores the actual dataset
- Data remains versionable, shareable, and reproducible

---

## 💻 Project Structure

```
wine_prediction_demo/
├── data/
│   ├── wine_sample.csv.dvc    # DVC pointer
│   └── wine_sample.csv        # Actual data (pulled via DVC)
├── src/
│   ├── __init__.py
│   ├── train.py               # Standalone training script
│   ├── utils.py               # Data helpers
│   └── requirements.txt       # Python dependencies
├── tests/
│   ├── __init__.py
│   └── test_main.py           # Pytest tests
├── .gitignore
└── README.md
   ```
