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


> Note: Raw datasets are not included due to licensing or privacy concerns. The code is fully reproducible with similar public data.


© 2022 Christina Makri.
Supervisor: Dr. Alexandros Karakasidis – University of Macedonia
