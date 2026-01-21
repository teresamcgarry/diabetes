# **Capstone Project: Diabetes Risk Prediction Project**

## **Analysis to understand the best predictors of diabetes risk**
![People Image v4](https://github.com/user-attachments/assets/ce3ab396-568a-414d-8e31-a9c9a2649b3a)

## **Project Overview**

This project delivers a complete analytics workflow exploring health indicators and demographic factors associated with diabetes. It includes feature engineering, data aggregation, statistical testing, and visualization using Python and Power BI.

The goal is to identify meaningful predictors of diabetes that can support early detection and inform public‑health decision making.

Final outputs include:

- Reproducible Python scripts
- Interactive Power BI dashboards
- A concise presentation deck

All datasets, analysis code, and visual assets are organized for clarity and portfolio readiness.

## **Table of Contents** 

## **Key Business Question**

**Which health, behavioural and socioeconomic factors are the most influential predictors of diabetes risk in the US population?**

To address this question, predictors were organised into five conceptual domains. This structure supports both interpretation and story-telling when discussing model results. 

The five groups are:

- Clinical / Physiological: indicators of underlying health status, diagnosed conditions.

- Demographic:  – core population characteristics: age and sex.

- Functional Health – measures of physical functioning, mobility, and limitations in daily activities.

- Socioeconomic – variables reflecting education, income, employment, and access to resources.

- Lifestyle – behavioural factors including physical activity, diet, smoking, and alcohol use.

## **Research Background**

Diabetes is one of the most common chronic diseases in the United States, affecting millions and placing a substantial burden on the healthcare system. Although there is no cure, lifestyle changes and medical treatment can significantly reduce risks. Early detection improves outcomes, making predictive models valuable tools for clinicians and public‑health planning.

In 2021:

- **38.4 million Americans** had diabetes
- **97.6 million adults** had prediabetes
- **1.2 million** new diagnoses occurred

## **Diabetes Dataset Description**

The **Behavioural Risk Factor Surveillance System (BRFSS)** is an annual CDC survey collecting responses from over 400,000 U.S. adults on health behaviours, chronic conditions, and preventive care.

This project uses the **2015 BRFSS dataset**, sourced from Kaggle: _diabetes_012_health_indicators_BRFSS2015.csv_

The target variable **Diabetes_012** includes:

- **0** - No diabetes / only during pregnancy
- **1** - Prediabetes
- **2** - Diabetes

Although the dataset is large (n = 253,680), the target variable **Diabetes_012** is highly imbalanced. The distribution of classes is as follows:

- 0 — No diabetes / only during pregnancy: 213,703 individuals (84%)

- 1 — Prediabetes: 4,631 individuals (1.8%)

- 2 — Diabetes: 35,346 individuals (13.9%)

This imbalance indicates that the majority class (0) dominates the dataset, while the prediabetes class (1) is particularly under‑represented. As a result, standard classification models may be biased toward predicting the majority class unless appropriate techniques—such as class weighting, resampling, or algorithmic adjustments—are applied.

**Dataset Features**

As well as the target variable, this dataset has 21 additional variables. All variables are numeric.

| Group | Feature | Question | Codes |
| --- | --- | --- | --- |
| Target | Diabetes_012 | Have you ever been told by a doctor that you have diabetes? | 0=no diabetes1=pre-diabetes2=diabetes |
| Clinical/Physiological | GenHlth | Would you say that in general your health is… | 1= excellent2=Very good3=Good4=Fair5= poor |
| Clinical/Physiological | BMI | Calculated from weight and height | Range: 12:98<18.5: Underweight18.5-24.8: Normal weight25-29.9: Overweight>=30: Obese |
| Clinical/Physiological | HighChol | Have you ever been told by a doctor, nurse, or other health professional that your blood cholesterol is high? | 0=no high cholesterol1=high cholesterol |
| Clinical/Physiological | CholCheck | Have you had your cholesterol checked within the past five years? | 0=no1=yes |
| Clinical/Physiological | HeartDiseaseorAttack | Have you ever been told by a doctor, nurse, or other health professional that you had coronary heart disease or a heart attack? | 0=no1=yes |
| Clinical/Physiological | HighBP | Have you ever been told by a doctor, nurse, or other health professional that you have high blood pressure? | 0=no high BP1=High BP |
| Clinical/Physiological | Stroke | (Ever told) you had a stroke? | 0=no1=yes |
| Demographic | Age | What is your age? | 1=18–24 years2=25–29 years3=30-34 years4=35-39 years5=40-44 years6=45-49 years7=50-54 years8=55-59 years9=60-64 years10=65-69 years11=70-74 years12=75-79 years13 = 80+ |
| Demographic | Sex | Are you male or female? | 0=female1=male |
| Functional Health | DiffWalk | Do you have serious difficulty walking or climbing stairs? | 0=no1=yes |
| Functional Health | PhysHlth | Thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? | 0-30 days |
| Functional Health | MentHlth | Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? | 0-30 days |
| Socioeconomic | NoDocbcCost | Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? | 0=no1=yes |
| Socioeconomic | AnyHealthcare | Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare or Medicaid? | 0=no1=yes |
| Socioeconomic | Education | What is the highest grade or year of school you completed? | 1= never attended school or only kindergarten2=Grades 1-8 (elementary)3=Grades 9-11(some high school)4=Grade 12 or GED(high school graduate)5=College 1–3 years (some college or technical school)6=College 4+ years (college graduate) |
| Socioeconomic | Income | Is your annual household income from all sources… | 1=< $10k2=$10k-$14.99k3=$15k-£19.99k4=$20k-$24.99k5=$25k=$34.99k6=$35k-$49.99k7=$50k-£74.99k8=≥ $75k |
| Lifestyle | Smoker | Have you smoked at least 10 cigarettes in your entire life? (Note 5 packs=1—cigarettes) | 0=no1=yes |
| Lifestyle | HvyAlcholConsump | During the past 30 days, how many drinks of alcohol did you have on average per week?Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) | 0=no1=yes |
| Lifestyle | Fruits | Do you eat fruit at least once per day? | 0=no1=yes |
| Lifestyle | Veggies | Do you eat vegetables at least once per day? | 0 =no1=yes |
| Lifestyle | PhysActivity | During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise? | 0=no1=yes |

**Project Plan**

A Trello board was used for project planning and tracking.

[Diabetes Analysis | Trello](https://trello.com/b/wzOxufpZ/diabetes-analysis)

# **Methods/Analysis Approach** 
## **Data cleaning**

The dataset was already pre‑cleaned, so only minimal preprocessing was required prior to exploratory data analysis.

## **Winsorisation**

The accompanying testing_and_analysis file (analysis/testing_and_analysis.md) documents one additional step, anmely, Winsorisation of the BMI variable. 

The raw BMI values contained extreme outliers at both ends of the distribution (as low as 12 and as high as 98). To reduce the influence of these biologically implausible values while retaining all observations, the BMI range was Winsorised to fall between 18 and 50.

## **Statistical Analysis**

To explore variable relationships and determine the most influential predictors of diabetes risk, several complementary analytical approaches were applied:

- Correlation analysis to assess linear associations between key features.

- Multinomial logistic regression and binary logistic regression to quantify the strength and direction of relationships between predictors and diabetes outcomes.

- Random Forest modelling, including systematic hyperparameter tuning, to capture nonlinear relationships and interaction effects while evaluating variable importance.

This anlysis is fully documented in the training and analysis notebook which can be located here: analysis/testing_and_analysis.md

# *Key Findings*
## *Conclusions**

- Diabetes risk is mainly driven by overall clinical and physiological elements such as general health, body weight and blood pressure

- Physical limitations, such as difficulty walking, and long-term health conditions, further increase risk

- Socioeconomic disadvantage also contributes to higher risk, whilst lifestyle factors play a much more modest role

## **Recommendations**
- Diabetes prevention measures should prioritise maintaining:
 -cardiovascular health
 - a healthy weight

In terms of wider societal measures, support services should be developed that identify and support people showing early signs of declining general or physical health

## **Data Visualisation**

Insights from this data analysis are communicated through multiple formats to support analysis and insight:

- A Power BI dashboard providing an exploration of key metrics and patterns.

- A presentation summarising the main findings, modelling results, and practical implications.

- Visualisations embedded within Jupyter notebooks.

**Dashboards**

List each dashboard page and describe:

- What insights it presents
- Which visual elements are used
- How it communicates findings to technical and non‑technical audiences

## **Repository Strucutre**

XXXXXXx

## **How to Reproduce**

- Clone the repository
- Install dependencies
- 
## **Requirements**

- Python 3.7+ (pandas, numpy, seaborn, matplotlib, scikit‑learn, statsmodels)
- VS Code
- Power BI
- Trello (project management)
- GitHub (version control)
- Dataset: BRFSS 2015 CSV

**Ethical Considerations**

## **Data Privacy**

The dataset contains no personally identifiable information (PII) and is fully anonymized in accordance with GDPR principles. All data is publicly available and intended for research use.

## **Bias or fairness issues with the data**

Survey data may reflect:

- Sampling bias
- Under‑representation of certain groups
- Self‑reported inaccuracies

Predictive models can serve to amplify these biases, so results should be interpreted with caution, especially across demographic subgroups.

## **Legal or societal issues**

The BRFSS dataset is publicly released for research use, so there are no direct legal restrictions. However, health data can reflect broader societal inequalities and differences in healthcare access. Any insights or models built from this dataset should be interpreted with awareness of these underlying disparities.

## **Use of generative AI**

## **Further Analysis Opportunities**

[Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?utm_source=copilot.com)

## **Credits**

The Code Institute course materials for the course "Data Analysis with Artificial Intelligence" were used as a template for the code in this project.

The following GutHub File Structure Visualizer was used. <https://r3cla.github.io/HubTree/>

All files were created and uploaded to GitHub















