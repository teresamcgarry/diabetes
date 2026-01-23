# **Capstone Project: Diabetes Risk Prediction Project**

## **Analysis to understand the best predictors of diabetes risk**
![People Image v4](https://github.com/user-attachments/assets/ce3ab396-568a-414d-8e31-a9c9a2649b3a)

# **Project Overview**

This project delivers a complete analytics workflow exploring health indicators and demographic factors associated with diabetes. It includes feature engineering, data aggregation, statistical testing, and visualisation using Python, PowerPoint and Power BI.

The goal is to identify meaningful predictors of diabetes that can support early detection and inform public‑health decision making.

Final outputs include:

- Reproducible Python scripts
- Interactive Power BI dashboards
- A concise PowerPoint presentation deck

All datasets, analysis code, and visual assets are organized for clarity and portfolio readiness.

# **Table of Contents** 

- Key Business Question
- Research Background
- Diabetes Dataset Description
- Project Plan
- Methods & Analysis Approach
- Key Findings
- Dashboards
- Repository Structure
- Requirements
- Effective data management practices
- How to Reproduce this Project
- Practical Challenges and Considerations
- Ethical and Privacy Considerations
- Use of Generative AI
- Evaluation of the learning process
- Further Analysis Opportunities
- Credits

# *Key Business Question*

## *Which health, behavioural and socioeconomic factors are the most influential predictors of diabetes risk in the US population?*

To address this question, predictors were organised into five conceptual domains. 

The five groups are:

- Clinical / Physiological: indicators of underlying health status, diagnosed conditions.

- Demographic:  – core population characteristics: age and sex.

- Functional Health – measures of physical functioning, mobility, and limitations in daily activities.

- Socioeconomic – variables reflecting education, income, employment, and access to resources.

- Lifestyle – behavioural factors including physical activity, diet, smoking, and alcohol use.

# **Research Background**

Diabetes is one of the most common chronic diseases in the United States, affecting millions and placing a substantial burden on the healthcare system. Although there is no cure, lifestyle changes and medical treatment can significantly reduce risks. Early detection improves outcomes, making predictive models valuable tools for clinicians and public‑health planning.

In 2021:

- **38.4 million Americans** had diabetes
- **97.6 million adults** had prediabetes
- **1.2 million** new diagnoses occurred

Data analytics plays a crucial role in healthcare, and this project demonstrates how analytical methods and AI can help address real‑world challenges such as early identification of diabetes risk and understanding the factors that drive poor health outcomes. By applying statistical modelling, machine‑learning techniques, and interpretability tools like SHAP, the analysis shows how data can uncover hidden patterns, support targeted interventions, and guide resource allocation. 

# **Diabetes Dataset Description**

## **Dataset Explored**

The **Behavioural Risk Factor Surveillance System (BRFSS)** is an annual CDC (Centers for Disease Control and Prevention, the national public health agency of the United States) survey collecting responses from over 400,000 U.S. adults on health behaviours, chronic conditions, and preventive care.

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

## *Dataset Features*

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

# **Project Plan**

A Trello board was used for project planning and tracking.

[Diabetes Analysis | Trello](https://trello.com/b/wzOxufpZ/diabetes-analysis)

# **Methods & Analysis Approach** 

## **Methods**
I selected research methodologies that aligned with the dataset and the goal of identifying predictors of diabetes risk. Because the data came from a health survey rather than an experiment, an observational analytical approach was most appropriate. I combined exploratory data analysis, logistic regression, and Random Forest modelling to interpret relationships, quantify predictor effects, and capture nonlinear patterns. These methods were chosen to balance interpretability with predictive accuracy. Their rationale for use and limitations are documented in a separate document (**analysis/testing_and_analysis.md**).

## **The application of data analytics tools, technologies and methodologies**

I experimented with different statititical techniques (mean, median, mode, standard deviation and chi-square, visualisation libraries (Matplotlib and Plotly, and seaborn), modelling approaches (multinomical regression, logistic regression, random forest, random forest with weights and parameter tuning and eventually SHAP, and workflow structures to determine what best supported accurate predictions and clear interpretability. 

I also trialled AI Assistant in Visual Code for automated modelling appraoches and documented these experiments in GitHub. 

Building the scikit‑learn pipeline required restructuring my preprocessing steps, and I iterated through several designs to avoid data leakage and improve reproducibility. 

I encountered many challenges such as a dataset with the majority were no diabetes, making analysis challenging. Also the SHAP computational time crashed my compter on several occasions, and there were some issues with categorical encoding of BMI for visualisaiotn and the remembering to drop them for modelling and use BMI_winsorised took several iterations, and I resolved them through tenactiy and experimentation.

These trials, refinements, and documented commits demonstrate a deliberate, research‑driven approach to selecting and adapting tools that strengthened both the workflow and the final model.

## **Data cleaning**

The dataset was already pre‑cleaned, so only minimal preprocessing was required prior to exploratory data analysis.

## **Winsorisation**

The accompanying testing and analysis file (analysis/testing_and_analysis.md) documents one additional step, namely, Winsorisation of the BMI variable. 

The raw BMI values contained extreme outliers at both ends of the distribution (as low as 12 and as high as 98). To reduce the influence of these biologically implausible values while retaining all observations, the BMI range was Winsorised to fall between 18 and 50.

## Statistical Analysis: Evaluate the problem-solving approach and solution aproposed

Several complementary analytical approaches were applied:

- Correlation analysis to assess linear associations between key features.

- Multinomial logistic regression and binary logistic regression to quantify the strength and direction of relationships between predictors and diabetes outcomes.

- Random Forest modelling, including systematic hyperparameter tuning, to capture nonlinear relationships and interaction effects while evaluating variable importance.

To evaluate the relationships between variables and identify the strongest predictors of diabetes risk, I applied a combination of correlation analysis, logistic regression, and Random Forest modelling, each selected for the specific analytical strengths they offer. 

**Correlation analysis** provided an initial, intuitive view of linear associations and helped me familiarise myself with the dataset, though it is limited in that it cannot detect nonlinear patterns or interaction effects. 

**Logistic regression—both multinomial and binary** allowed me to quantify the direction and magnitude of each predictor’s influence, but its assumptions of linearity in the log‑odds and its difficulty handling complex interactions meant it could not fully capture the structure of the data. 

To overcome these limitations, I incorporated a **Random Forest model with hyperparameter tuning**, which is well suited for modelling nonlinear relationships and interactions while also providing clear variable‑importance measures. 

I considered alternative approaches such as gradient boosting, but Random Forest offered the best balance of interpretability, performance, and computational efficiency for this dataset. All methods, decisions, and reflections—including descriptions of each technique and their trade‑offs—are fully documented in the training and analysis notebook at **analysis/testing_and_analysis.md**

# **Key Findings**

## Conclusions 

**1. Clinical / Physiological factors lead**

BMI, blood pressure, cholesterol, and general health were the strongest risk indicators.

**2. Demographics matter**

Age (especially mid-40s onwards) and lower income levels were the next most important predictors

**3. Functional limitations signalled risk**

Poor physical health days, mobility issues and mental health burden, flagged elevated risk

**4. Lifestyle factors contributed but were less dominant**

Smoking, alcohol use, and physical inactivity contributed, but were less influential than clinical, demographic and socioeconomic factors 

## **Recommendations**

1. Prioritise clinical risk screening with routine checks for BMI, blood pressure and cholesterol in primary care settings

2. Target high-risk demographic groups by expanding preventative outreach for adults in their 40s and beyond, and for lower-income populations where risk increases

3. Strengthen support for functional and mental health needs
   
4. Reinforce lifestyle interventions with structural support by promoting smoking cessation, physical activity and reduced alcohol use 

# **Dashboards**

## **Data Visualisation**

Insights from this data analysis are communicated through multiple formats to support analysis and insight:

- A Power BI dashboard providing an exploration of key metrics and patterns.

- A PowerPoint presentation summarising the main findings, modelling results, and practical implications.

- Visualisations embedded within Jupyter notebooks.

## **Communicating findings to technical and non‑technical audiences**

The dashboard is designed to communicate insights effectively to both technical and non-technical audiences by combining clear visual summaries and plain-language explanations for decision-makers with the ability to explore underlying metrics and model outputs for more technically informed users.

## **Page 1: This page is an explanation of the backgroud to the project**

<img width="2000" height="1121" alt="image" src="https://github.com/user-attachments/assets/abfac08d-8e92-45df-9c36-b53ef56a46b8" />

## **Page 2: This page is a summary of the key findings of the research**

<img width="1480" height="826" alt="image" src="https://github.com/user-attachments/assets/277e8aac-2567-4743-9472-a0705b2792d1" />

## **Page 3: This page is a summary of the diabetes predictors grouped into 5 groups to aid understanding**

<img width="2000" height="1121" alt="image" src="https://github.com/user-attachments/assets/ac9f1c07-c904-45cf-b8f0-4d3e3d717295" />


## **Page 4: This page is a summary of the top 5 predictors of diabetes risk**

<img width="2000" height="1121" alt="image" src="https://github.com/user-attachments/assets/5bb1871a-bfb8-48c6-89b8-ac81981b794e" />

## **Page 5: This page is a summary of the top 10 predictors of diabetes risk i.e. offering a little more detail into the key diabetes risk predictors**

<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/c07ab5c2-0ebf-4009-a681-4c7c1a4ad09f" />

## **Page 6: This page is a summary of all 21 predictors of diabetes risk i.e. offering the full detail of diabetes risk predictors**

<img width="2000" height="1115" alt="image" src="https://github.com/user-attachments/assets/38e2a727-b9ea-4461-9dc8-9bfffcf9c03e" />

## **Page 7: This page is a summary of the SHAP analysis offering more explanation of the diabetes risk predictors**

<img width="1465" height="808" alt="image" src="https://github.com/user-attachments/assets/fb19fff9-1b59-417f-880d-40e417f13f8f" />

# **Repository Strucutre**
<img width="648" height="494" alt="image" src="https://github.com/user-attachments/assets/df4cf5e7-00d7-46fb-ab46-e78dea5e6887" />

This was created using: <https://r3cla.github.io/HubTree/>

# **Requirements**

- Python 3.7+
- pandas
- numpy
- seaborn
- matplotlib
- scikit‑learn
- statsmodels
- Jupyter Notebook / JupyterLab
- VS Code
- Virtual environment (venv or Conda)
- pip or conda for package installation
- Power BI Desktop
- Trello (project management)
- GitHub (version control)
- Dataset: BRFSS 2015 CSV
- Minimum 8–16 GB RAM recommended
- Windows/macOS/Linux compatible environment
- Dataset: BRFSS 2015 CSV

# **Effective data management practices**

In this project I demonstrated effective data collection, cleaning, storage, and processing by maintaining a clear, reproducible workflow supported by structured data management practices and a fully annotated Jupyter notebook. 

The raw dataset was imported, inspected, and cleaned systematically; although no values were missing, BMI contained extreme outliers that required Winsorisation to stabilise the distribution. The cleaned dataset was then stored in a well‑organised, structured format to ensure consistency and repeatability across the analysis.

GitHub served as the central workspace for storing code and project files, providing transparency, traceability, and safe experimentation through version control. Each stage of refinement—from early exploratory cleaning to the final preprocessing pipelines—was captured in incremental commits, allowing changes to be reviewed, compared, and reverted when necessary. Detailed documentation in the notebook explains every transformation step, including outlier handling, feature engineering, and validation checks. The Power BI dashboard also includes a dedicated section outlining data sources and the full processing pipeline, reinforcing how the data was collected, prepared, and transformed throughout the project.

# *How to reproduce this project*

To reproduce this project, clone the repository to your local machine and install all required dependencies using the provided environment or requirements file. 

After setup, open the testing_and_analysis notebook to review what analysis was previously and run the Python code in order to generate the results. 

If your project uses configuration files or specific data paths, update those settings as noted in the documentation.

# **Practical challenges and considerations**

## **Technical environment issues**

Kernel instability: Repeated kernel crashes disrupted workflow, especially during memory‑intensive modelling and visualisation. This required frequent restarts, checkpointing, and breaking code into smaller, more manageable segments.

Library incompatibilities: Conflicts between package versions (e.g., pandas, scikit‑learn, matplotlib) caused import errors and inconsistent behaviour. Resolving this involved reinstalling environments, pinning versions, and occasionally rewriting code to match available library functions.

Computational constraints: Large datasets and ensemble models strained available RAM and CPU resources, limiting the complexity of models that could be run and requiring more efficient preprocessing and sampling strategies.

## **Data‑related challenges**

Severe class imbalance: The dominance of the “no diabetes” class reduced model performance and required additional techniques such as resampling, weighting, and reframing the prediction task.

Data cleaning complexity: Handling missing values, outliers, and mixed data types added significant preprocessing overhead and required careful methodological justification.

Modelling and evaluation considerations
Model convergence issues: Some algorithms struggled to converge due to imbalance, multicollinearity, or noisy predictors, requiring tuning, simplification, or alternative models.

Balancing interpretability and performance: More powerful models (e.g., random forests) performed better but were harder to interpret, while simpler models were more transparent but less accurate.

Threshold and calibration considerations: For screening‑oriented tasks, selecting appropriate probability cut‑offs and assessing calibration became essential to ensure practical usefulness.

## **Workflow and reproducibility**

Maintaining a stable environment: Ensuring reproducibility across sessions was challenging due to environment resets and package conflicts.

Version control and documentation: Tracking changes, documenting decisions, and ensuring code clarity were essential to manage complexity and avoid regressions.

# **Ethical and Privacy Considerations**

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

# **Use of generative AI**

Generative AI played a central role in supporting this project by accelerating coding, guiding data analysis, enhancing visualisation, and strengthening the overall story. 

It helped me interpret and process complex health data more efficiently, revealing patterns and insights that would have been far slower to uncover manually. 

AI‑driven visualisation support also enabled me to turn raw outputs into clear, intuitive graphics that deepened understanding and improved communication of results. 

Beyond the technical work, AI contributed to the storytelling aspect of the project by helping me synthesise findings and structure them into a coherent, concise, engaging narrative. 

Throughout the workflow, AI‑assisted tools provided valuable support for refining code, troubleshooting issues, and exploring alternative modelling approaches. 

Together, these capabilities demonstrate how analytics and AI can transform raw health data into actionable insights that strengthen decision‑making and enable more proactive, data‑driven healthcare.

# **Evaluation of the learning process**

Working on this project has been a genuinely iterative learning experience that strengthened both my technical skills and my ability to adapt to new tools and challenges. Along the way, I uncovered gaps in my Python programming and statistical knowledge—whether it was handling skewed health variables, structuring scikit‑learn pipelines, or learning entirely new techniques like SHAP and SMOTE. Getting comfortable with Power BI and DAX was equally rewarding and occasionally exasperating, but seeing the final dashboard come together in a way that tells a clear, compelling story made the effort worthwhile.

Each challenge pushed me to research solutions, test alternatives, and refine my approach. Analysis is never just about writing code; it’s about exploring the data, understanding what it represents, and shaping a narrative that does it justice. All of this work is fully documented in the training and analysis notebook located at **analysis/testing_and_analysis.md**.

My key learnings include:

- What feels impossible at midnight often becomes achievable in the morning—very little works perfectly the first time, and that’s normal.

- Data analysis is a journey. You can’t predict every technique or library you’ll need, and sometimes your environment breaks because you’ve installed too many conflicting packages. Frustrating, yes—but always solvable.

- Stay curious, and remember that data analysis is meant to be enjoyable.

Through this process, I’ve learned a great deal about Python, Power BI, GitHub, PowerPoint, and statistical testing. And perhaps most importantly, I’ve learned that analysis is never truly “finished”—there’s always another test you could run or another refinement you could make. The real skill lies in recognising when the results are consistent, meaningful, and ready to stand on their own.

At that point it is time to stop!

# **Further Analysis Opportunities**

Further analysis opportinities are outlined in the accompanying file located here: analysis/testing_and_analysis.md

[Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?utm_source=copilot.com)



# **Credits**

The Code Institute course materials for the course "Data Analysis with Artificial Intelligence" were used as a template for the code in this project.

The following GutHub File Structure Visualizer was used. <https://r3cla.github.io/HubTree/>

All files were created and uploaded to GitHub






























