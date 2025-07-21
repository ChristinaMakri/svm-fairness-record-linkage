# Fairness in SVM-based Record Linkage  
> Evaluating Bias Using Confusion Matrix-based Metrics

This repository contains the implementation and experimental evaluation of my Bachelor Thesis, conducted at the Department of Applied Informatics, University of Macedonia, Greece. The thesis investigates the presence of algorithmic bias in Support Vector Machine (SVM) classifiers used for record linkage tasks, with a focus on fairness definitions based on confusion matrix metrics.
  
## 📄 Abstract

Record linkage is the process of identifying records from different data sources that refer to the same real-world entity. In modern applications, machine learning classifiers, such as Support Vector Machines, are frequently used to automate this task. However, such algorithms may inherit or amplify societal biases present in the training data.

This study explores multiple fairness definitions (Equalized Odds, Predictive Parity, Predictive Value Parity, Matthews Correlation Coefficient comparison) and evaluates how different ethnicity and nationality groups are affected under each definition. The implementation uses real-world voter registration data and applies synthetic noise to names in order to simulate approximate matching scenarios.
  
## 🧪 Features and Methods

- **SVM-based binary classification** for entity matching
- **Jaro-Winkler similarity** for string comparison of names
- **Confusion Matrix analysis** with detailed fairness metrics:
  - Precision (PPV)
  - TPR / FPR (Equalized Odds)
  - NPV (Predictive Value Parity)
  - MCC (Matthews Correlation Coefficient)
- **Ethnicity & Nationality Bias Analysis**
- **Visualizations** of metric variations across groups and datasets
- Implementation with:
  - Python (scikit-learn, pandas, matplotlib)
  - RecordLinkage Toolkit
  
## 🧾 Published Paper

This work has been officially published by **IEEE Xplore**:
📚 Makri Christina, Karakasidis, Alexandros, Evaggelia Pitoura
**"Towards a more Accurate and Fair SVM-based Record Linkage"**  
*2022 IEEE International Conference on Big Data (Big Data)*.  
[🔗 Read the publication](https://ieeexplore.ieee.org/document/10020514)

  
## 📊 Datasets Used

The datasets used in this project are based on real-world name data enriched with group attributes for fairness evaluation. Specifically:

### 🔹 1. Ethnicity-Labeled Names
- **Source**: Derived from the *North Carolina Voter Registration Database*.
- **Description**: Contains first names and surnames associated with ethnicity labels (e.g., *White*, *Black*, *Asian*, *Hispanic*, etc.).
- **Usage**: Used to assess classifier fairness across ethnic groups by tracking classification outcomes per group.

### 🔹 2. Nationality-Labeled Names
- **Source**: Based on publicly available name lists and the [NamePrism](https://github.com/IBM/name-prism) categorization.
- **Description**: Includes names with inferred nationality groups (e.g., *Greek*, *Spanish*, *English*, etc.).
- **Usage**: Enables fairness comparisons across nationality groups.

### 🔹 3. Synthetic Matching Pairs
- **Construction**: Altered name variants are created from the original records using a random string modification function (insert/delete/replace characters).
- **Purpose**: Simulate realistic noisy data often encountered in real-world record linkage (e.g., typos, transliteration issues).
- **Example**:
  - Original: `Maria Papadopoulos`
  - Altered: `MarIa Papdapoulos`

### 🔹 4. Similarity Features
- For every pair of records, **Jaro-Winkler similarity** is computed on the first name and surname separately.
- These are used as input features for training a binary classifier (`MATCH` vs `NON-MATCH`).

> ℹ️ Note: For privacy reasons, raw name data is not published. However, the pipeline is fully reproducible using public sources or synthetic equivalents.



  

© 2022 Christina Makri.
Supervisor: Dr. Alexandros Karakasidis – University of Macedonia
