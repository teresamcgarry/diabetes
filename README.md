# **Diabetes Prediction Project - Capstone Project**

## **Analysis to understand the best predictors of Diabetes**

## **Project Overview**

This project delivers a complete analytics workflow exploring health indicators and demographic factors associated with diabetes. It includes feature engineering, data aggregation, statistical testing, and visualization using Python and Power BI.

The goal is to identify meaningful predictors of diabetes that can support early detection and inform public‑health decision making.

Final outputs include:

- Reproducible Python scripts
- Interactive Power BI dashboards
- A concise presentation deck

All datasets, analysis code, and visual assets are organized for clarity and portfolio readiness.

## **Key Business Question**

Which features are the best predictors of Diabetes:

- Clinical/Psychological
- Demographic
- Functional Health
- Socioeconomic
- Lifestyle

## **Research Background**

Diabetes is one of the most common chronic diseases in the United States, affecting millions and placing a substantial burden on the healthcare system. Although there is no cure, lifestyle changes and medical treatment can significantly reduce risks. Early detection improves outcomes, making predictive models valuable tools for clinicians and public‑health planning.

In 2021:

- **38.4 million Americans** had diabetes
- **97.6 million adults** had prediabetes
- **1.2 million** new diagnoses occurred

**Diabetes Data Source**

The **Behavioural Risk Factor Surveillance System (BRFSS)** is an annual CDC survey collecting responses from over 400,000 U.S. adults on health behaviours, chronic conditions, and preventive care.

This project uses the **2015 BRFSS dataset**, sourced from Kaggle: _diabetes_012_health_indicators_BRFSS2015.csv_

The target variable **Diabetes_012** includes:

- **0** - No diabetes / only during pregnancy
- **1** - Prediabetes
- **2** - Diabetes

The dataset contains **21 numeric features** covering clinical, lifestyle, demographic, and socioeconomic factors.

Link: <https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?utm_source=copilot.com>

There is class imbalance in this dataset.

**Dataset Features**

This dataset has 21 feature variables. All variables are numeric.

| **Feature** | **Question** | **Codes** |
| --- | --- | --- |
| Diabetes_012 | Have you ever been told by a doctor that you have diabetes? | 0=no diabetes<br><br>1=pre-diabetes<br><br>2=diabetes |
| HighBP | Have you ever been told by a doctor, nurse, or other health professional that you have high blood pressure? | 0=no high BP<br><br>1=High BP |
| HighChol | Have you ever been told by a doctor, nurse, or other health professional that your blood cholesterol is high? | 0=no high cholesterol<br><br>1=high cholesterol |
| CholCheck | Have you had your cholesterol checked within the past five years? | 0=no<br><br>1=yes |
| BMI | Calculated from weight and height | Range: 12:98<br><br><18.5: Underweight<br><br>18.5-24.8: Normal weight<br><br>25-29.9: Overweight<br><br>\>=30:Obese |
| Smoker | Have you smoked at least 10 cigarettes in your entire life? (Note 5 packs=1-cigarettes) | 0=no<br><br>1=yes |
| Stroke | (Ever told) you had a stroke? | 0=no<br><br>1=yes |
| HeartDiseaseorAttack | Have you ever been told by a doctor, nurse, or other health professional that you had coronary heart disease or a heart attack? | 0=no<br><br>1=yes |
| PhysActivity | During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise? | 0=no<br><br>1=yes |
| Fruits | Do you eat fruit at least once per day? | 0=no<br><br>1=yes |
| Veggies | Do you eat vegetables at least once per day? | 0 =no<br><br>1=yes |
| HvyAlcholConsump | During the past 30 days, how many drinks of alcohol did you have on average per week?<br><br>Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) | 0=no<br><br>1=yes |
| AnyHealthcare | Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare or Medicaid? | 0=no<br><br>1=yes |
| NoDocbcCost | Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? | 0=no<br><br>1=yes |
| GenHlth | Would you say that in general your health is… | 1= excellent<br><br>2=Very good<br><br>3=Good<br><br>4=Fair<br><br>5= poor |
| MentHlth | Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? | 0-30 days |
| PhysHlth | Thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? | 0-30 days |
| DiffWalk | Do you have serious difficulty walking or climbing stairs? | 0=no<br><br>1=yes |
| Sex | Are you male or female? | 0=female<br><br>1=male |
| Age | What is your age? | 1=18-24 years<br><br>2=25-29 years<br><br>3=30-34 years<br><br>4=35-39 years<br><br>5=40-44 years<br><br>6=45-49 years<br><br>7=50-54 years<br><br>8=55-59 years<br><br>9=60-64 years<br><br>10=65-69 years<br><br>11=70-74 years<br><br>12=75-79 years<br><br>13 = 80+ |
| Education | What is the highest grade or year of school you completed? | 1= never attended school or only kindergarten<br><br>2=Grades 1-8 (elementary)<br><br>3=Grades 9-11(some high school)<br><br>4=Grade 12 or GED(high school graduate)<br><br>5=College 1-3 years (some college or technical school)<br><br>6=College 4+ years (college graduate) |
| Income | Is your annual household income from all sources… | 1=< \$10k<br><br>2=\$10k-\$14.99k<br><br>3=\$15k-£19.99k<br><br>4=\$20k-\$24.99k<br><br>5=\$25k=\$34.99k<br><br>6=\$35k-\$49.99k<br><br>7=\$50k-£74.99k<br><br>8=≥ \$75k |

**Project Plan**

A Trello board was used for project planning and tracking.

[Diabetes Analysis | Trello](https://trello.com/b/wzOxufpZ/diabetes-analysis)

**Data cleaning**

The dataset was already pre‑cleaned, so minimal preprocessing was required before exploratory data analysis.

**Statistical Analysis and Why Chosen/Data analysis methods used and their limitation/alternative approaches**

To understand relationships and identify predictors, the following methods were used:

- Correlation analysis
- Logistic regression
- Additional statistical tests as appropriate

Limitations and alternative approaches are discussed in the analysis notebooks.

**Data Visualisation**

Insights are communicated through:

- A Power BI dashboard
- A presentation summarizing key findings
- Visualizations embedded in Jupyter notebooks

**Key Findings**

**Strategic Insights and Recommendations**

**Dashboards**

List each dashboard page and describe:

- What insights it presents
- Which visual elements are used
- How it communicates findings to technical and non‑technical audiences

**Requirements**

- Python 3.7+ (pandas, numpy, seaborn, matplotlib, scikit‑learn, statsmodels)
- VS Code
- Power BI
- Trello (project management)
- GitHub (version control)
- Dataset: BRFSS 2015 CSV

**How to Reproduce**

- Clone the repository
- Install dependencies

Code:

pip install -r requirements.txt

- Place raw CSV file into /data_raw
- Run Jupyter notebook
- Open the Power BI dashboard

**Ethical Considerations**

**Data Privacy**

The dataset contains no personally identifiable information (PII) and is fully anonymized in accordance with GDPR principles. All data is publicly available and intended for research use.

**Bias or fairness issues with the data**

Survey data may reflect:

- Sampling bias
- Under‑representation of certain groups
- Self‑reported inaccuracies

Predictive models can serve to amplify these biases, so results should be interpreted with caution, especially across demographic subgroups.

**Legal or societal issues**

The BRFSS dataset is publicly released for research use, so there are no direct legal restrictions. However, health data can reflect broader societal inequalities and differences in healthcare access. Any insights or models built from this dataset should be interpreted with awareness of these underlying disparities.

**Use of generative AI**

**Further Analysis Opportunities**

| **Analysis** | **Opportunity** |
| --- | --- |
|     |     |
|     |     |

[Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?utm_source=copilot.com)

**Credits**

The Code Institute course materials for the course "Data Analysis with Artificial Intelligence" were used as a template for the code in this project.

The following GutHub File Structure Visualizer was used. <https://r3cla.github.io/HubTree/>

All files were created and uploaded to GitHub
