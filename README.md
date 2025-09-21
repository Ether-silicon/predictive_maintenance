## 📂 Repository Contents

* preprocessing/ – MATLAB scripts for reading .mat and .tdms files, segmentation, normalization, and feature extraction.

* modeling/ – Python scripts (scikit-learn) for imputation, SMOTE balancing, and training classification models (Random Forest, SVM, Decision Tree).

## 📊 Dataset

This project uses the KAIST Bearing Dataset from the Korea Advanced Institute of Science and Technology (KAIST), widely used in fault diagnosis and predictive maintenance research.

* Literature reference:
[Lee, et al. (2023). Feature Partial Density for bearing fault classification using KAIST dataset.](https://www.sciencedirect.com/science/article/pii/S2352340923001671?via%3Dihub)
* Dataset access: [KAIST Bearing Dataset](https://data.mendeley.com/datasets/ztmf3m7h5x/6)

| ⚠️ Note: The raw dataset is not included in this repository due to size and license constraints.

## ⚙️ Workflow

### 1.Data Preprocessing

* Convert .mat (vibration) and .tdms (current, temperature) files.
* Segment 1-minute recordings into 2-second windows.
* Apply imputation (mean, median, KNN, zero-fill).
* Extract time-domain, frequency-domain, and statistical features.

### 2.Modeling

* Apply SMOTE for class balancing.
* Train and evaluate Random Forest, SVM, and Decision Tree models.
* Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix.

## 🚀 Results

* Random Forest achieved 99.9% accuracy and 99.87% F1-score, outperforming the literature benchmark of 91.3%.
* Demonstrated strong feature importance from both vibration and temperature data, validating multi-sensor integration.

## 🔮 Future Work

* Extend to Remaining Useful Life (RUL) prediction.
* Explore hybrid models (CNN-LSTM, deep ensembles).
* Deployment in real-time predictive maintenance systems.

## 🛠️ Tech Stack

* MATLAB – Signal processing, feature extraction.
* Python (scikit-learn, pandas, numpy) – Modeling, imputation, class balancing.
