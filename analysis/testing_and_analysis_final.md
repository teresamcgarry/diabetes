**Testing and Data Analysis File**

**Methodology and Evaluation of the Data Analysis**

This capstone analysis applies appropriate data preparation, exploratory techniques, and predictive modelling to a large population health dataset, using sound methodological choices including Winsorisation, non-parametric correlation, multinomial and binary logistic regression, and random forest modelling. However, model performance is fundamentally constrained by severe class imbalance, particularly for prediabetes, which led most models to favour the majority “no diabetes” class and struggle to reliably distinguish between classes, even when resampling and class-based weighting were applied. Reframing the task as binary risk identification did produce more stable and interpretable results, supporting the conclusion that the model is better suited to population-level screening rather than diagnostic classification.

**Initial EDA: Summary**

-   There are profiles for 253,680 individuals in this dataset.

-   The datafile has the following profile for the target variable Diabetes\_012 with counts as follows:

-   no diabetes: 213,703 (84%)

-   prediabetes: 4,631 (1.8%)

-   diabetes: 35,346 (13.9%)

-   There are an additional 21 variables, all of which are floats.

-   The description of each feature is included in the README file (i.e. the feature name, the question asked and the possible response codes).

-   The dataset has been cleaned.

-   There are no null values.

-   However, Body Mass Index (BMI) has both upper and lower outliers that need addressing.

**Data Analysis**

The following table describes the original BMI values, while the histogram below offers a visual representation of their distribution.

Online research suggests that BMI is more typically between 18 and 50 (e.g. https://www.cdc.gov/healthyweight/assessing/bmi/adult\_bmi/index.html (cdc.gov in Bing)

Therefore, in this dataset, there are some extreme outliers at both the lower and upper ends.

| **Variable** | **Count**  | **mean** | **std**  | **min** | **25%** | **50%** | **75%** | **max** |
|--------------|------------|----------|----------|---------|---------|---------|---------|---------|
| **BMI**      | **253680** | **28**   | **6.61** | **12**  | **24**  | **27**  | **31**  | **98**  |

<img src="media\media\image1.png" style="width:6.03194in;height:4.02829in" />

BMI was also grouped into 4 classifications to aid analysis:

-   Underweight: &lt;18

-   Normal weight: &gt;18 and &lt;=24.8

-   Overweight: &gt;=25 and &lt;=29.9

-   Obese: &gt;=30

<img src="media\media\image2.png" style="width:6.03209in;height:3.92763in" />

**Winsorisation**

**Description of Winsorisation**

Winsorisation is a practical way to limit the influence of extreme values without discarding data entirely. Instead of removing outliers, they are capped at the chosen percentile thresholds. This preserves sample size and distributional shape while preventing extreme values from dominating visualisations or summary statistics.

**Data Cleaning Undertaken**

In this dataset, Winsorisation for BMI was set to 1% (BMI = 18) and 99% (BMI = 50). The revised BMI distribution is summarised in the following histogram.

| **Variable**        | **Count**  | **mean** | **std**  | **min** | **25%** | **50%** | **75%** | **max** |
|---------------------|------------|----------|----------|---------|---------|---------|---------|---------|
| **BMI\_winsorised** | **253680** | **28**   | **6.03** | **18**  | **25**  | **27**  | **31**  | **50**  |

This variable, **BMI\_winsorised,** will be used in all analyses going forward and BMI will be dropped.

<img src="media\media\image3.png" style="width:6.05293in;height:4.63606in" />

**Spearman Correlation**

**Description of Spearman Correlation**

Spearman correlation is a rank-based measure of association that captures how well the relationship between two variables can be described by a monotonic trend (i.e. as one variable increases, the other always tends to decrease) rather than a straight line. It is especially useful when the data is skewed, ordinal, or contains outliers, which is why it works so well in health and behavioural datasets like this one.

**Analysis Undertaken**

A Spearman correlation, rather than a Pearson correlation, was selected to support the analysis as the variable distributions were typically skewed (i.e. not normally distributed).

Two separate correlation analyses were conducted:

-   An initial correlation of all features vs all features, to understand the relationships between features.

-   A second correlation using Diabetes\_012 as the target/outcome variable versus the remaining features.

**Initial Correlation: All features vs All features using a Heatmap.**

**Findings**

This initial correlation matrix shows how health and demographic variables are interrelated. General health is linked to physical health and mobility issues, while age is correlated with higher blood pressure and poorer overall health. A higher BMI is associated with increased cardiovascular risks, and lower income and education levels tend to be associated with worse health outcomes.

<img src="media\media\image4.png" style="width:6.26806in;height:5.00417in" />

**Second correlation: Diabetes\_012 as the target variable**

**Findings**

Once again, diabetes risk is driven most strongly by overall health, blood pressure, BMI, mobility limitations, and cholesterol, with age and heart disease also playing meaningful roles. Protective factors such as physical activity, higher education, and higher income show a lower likelihood of diabetes risk.

**Feature Importance in Predicting Diabetes**

1.  Diabetes\_012             1.000000

2.  GenHlth                 0.297138

3.  HighBP                   0.271668

4.  BMI\_winsorised           0.235914 (like original BMI)

5.  DiffWalk               0.223567

6.  HighChol                 0.210668

7.  Age                     0.186357

8.  HeartDiseaseorAttack 0.178564

9.  PhysHlth                 0.161718

10. Stroke                   0.105887

11. CholCheck               0.068018

12. Smoker                   0.063040

13. MentHlth                 0.044921

14. NoDocbcCost             0.037379

15. Sex                     0.030143

16. AnyHealthcare           0.014530

17. Fruits                 -0.042268

18. HvyAlcoholConsump   -0.057244

19. Veggies                 -0.059353

20. PhysActivity         -0.121988

21. Education             -0.126862

22. Income                 -0.172611

**Chi-square**

**Description of Chi-square**

Chi-square is a statistical test that measures whether two categorical variables are associated. It compares the observed counts in a contingency table with the expected counts that you would get if there were no relationship between the variables.

**Analysis Undertaken**

Chi-square tests were undertaken for the 14 binary variables, with Diabetes\_012 as the target variable.

**Findings**

The chi-square results show that all 14 variables have statistically significant associations with diabetes status, but the strength of those relationships varies widely. High blood pressure, difficulty walking, high cholesterol, and heart disease/attack exhibit the strongest associations (highest Cramer's V), suggesting they are the most influential correlates of diabetes in this set.

Variables such as sex and (lack of) access to healthcare show very weak associations, indicating they have a minimal practical relationship despite statistical significance driven by the large sample size.

The results are shown in the table below.

| **Variable**        | **Chi2** | **p**       | **cramers\_v** |
|---------------------|----------|-------------|----------------|
| HighBP              | 18794.64 | 0.0         | 0.27219        |
| DiffWalk            | 12776.94 | 0.0         | 0.22442        |
| HighChol            | 11258.92 | 0.0         | 0.21067        |
| HeartDieaseorAttack | 8244.89  | 0.0         | 0.18028        |
| PhysActivity        | 3789.30  | 0.0         | 0.12222        |
| Stroke              | 2916.75  | 0.0         | 0.10723        |
| CholCheck           | 1173.75  | 1.3291e-255 | 0.06802        |
| Smoker              | 1010.51  | 3.7167e-220 | 0.06311        |
| Veggies             | 893.84   | 8.0296e-195 | 0.05936        |
| HvyAlcoholConsump   | 850.32   | 2.2619e185  | 0.05789        |
| Fruits              | 454.347  | 2.1867e-99  | 0.04232        |
| NoDocbcCost         | 396.082  | 9.8158e-87  | 0.03951        |
| Sex                 | 250.851  | 3.3767e-55  | 0.03145        |
| AnyHealthcare       | 69.078   | 9.9979e-16  | 0.01650        |

**Modelling**

**Model 1: Multinomial Logistic Regression**

**Description of Multinomial Logistic Regression**

Multinomial logistic regression was used to model the probability of belonging to one of three outcome categories (i.e. no diabetes, prediabetes, or diabetes) based on the predictor variables. This method extends binary logistic regression by allowing the dependent variable to have more than two unordered categories, while still using the logistic function to estimate category-specific probabilities.

**Analysis Undertaken**

An initial multinomial regression was conducted using the original three-category outcome variable, retaining the codes:

-   **No diabetes**: 213,703 individual responses

-   **Prediabetes**: 35,346 individual responses

-   **Diabetes**: 4,631 individual responses

> This allowed the model to estimate how each predictor influenced the likelihood of membership in each category.
>
> **Definitions**
>
> Definitions of:

-   **precision** = Of all the cases the model said were diabetes, how many were truly diabetes (i.e. few false positives)

-   **recall** = Of all the people who have diabetes, how many did the model correctly identify? (i.e. few false negatives)

-   **f1\_score**: = How well does the model perform when we care about both catching true cases and avoiding false alarms?

-   **support**: count of individuals in each class

> In health analysis, **recall** is more typically the primary evaluation metric.
>
> **Findings**

-   Despite achieving moderate overall accuracy (69%), the multinomial logistic regression performs poorly on the two minority classes, especially prediabetes, indicating a limited ability to differentiate between the three diabetes classes.

-   Individuals who are younger, leaner, healthier, and socioeconomically advantaged are much more likely to be classified as having no diabetes.

**Classification report**

The model accuracy was 69%.

| **Variable: Class** | **precision** | **recall** | **f1-score** | **Support** |
|---------------------|---------------|------------|--------------|-------------|
| No diabetes (0)     | 0.9449        | 0.7049     | 0.8075       | 42741       |
| Prediabetes (1)     | 0.0350        | 0.1825     | 0.0587       | 926         |
| Diabetes (2)        | 0.3365        | 0.6671     | 0.4474       | 7069        |
|                     |               |            |              |             |
| Accuracy            |               |            | 0.6901       | 50736       |
| macro avg           | 0.4388        | 0.5182     | 0.4378       | 50736       |
| weighted avg        | 0.8435        | 0.6901     | 0.7436       | 50736       |

**Model 1: Multinomial Logistic Regression Confusion Matrix**

No diabetes (class 0) shows that whilst most predictions are correctly identified (30,130), a further 12,611 are misclassified, especially diabetes (class 2). Furthermore, prediabetes (class 1) shows very poor performance with only 169 out of 926 cases correctly identified. Most are misclassified as diabetes (class 2). Finally, diabetes (class 2) shows moderate performance with 4,716 correct predictions out of 7,069, but with 1,470 misclassified as no diabetes (class 0).

In summary, the model over-predicts diabetes and misclassifies a substantial number of diabetes cases as healthy. This limits its usefulness in a medical setting.

<img src="media\media\image5.png" style="width:4.19794in;height:2.82778in" />

**Top positive & negative coefficients per class:**

**No diabetes (class 0): top positive features:**

-   HvyAlcoholConsump 0.145355

-   Income 0.133858

-   PhysHlth 0.055354

-   Education 0.042370

-   Fruits 0.024307

-   PhysActivity 0.016320

-   MentHlth 0.015768

-   Veggies 0.011974

**No diabetes (class 0): top negative features:**

-   GenHlth -0.586325

-   BMI\_winsorised -0.503940

-   Age -0.467266

-   HighBP -0.333542

-   HighChol -0.293158

-   CholCheck -0.228686

-   Sex -0.128226

-   HeartDiseaseorAttack -0.066704

**Prediabetes (class 1): top positive features:**

-   Age 0.390335

-   BMI\_winsorised 0.310915

-   GenHlth 0.264090

-   HighChol 0.242938

-   CholCheck 0.124227

-   HighBP 0.122307

-   NoDocbcCost 0.099967

-   MentHlth 0.066339

**Prediabetes (class 1): top negative features:**

-   Income -0.128164

-   Education -0.060001

-   DiffWalk -0.054067

-   PhysHlth -0.049724

-   HeartDiseaseorAttack -0.043618

-   Stroke -0.040096

-   AnyHealthcare -0.019065

-   HvyAlcoholConsump -0.018618

**Diabetes (class 2): top positive features:**

-   GenHlth 0.617056

-   BMI\_winsorised 0.505217

-   Age 0.463535

-   HighBP 0.357944

-   HighChol 0.285405

-   CholCheck 0.246751

-   Sex 0.142219

-   HeartDiseaseorAttack 0.074738

**Diabetes (class 2): top negative features:**

-   HvyAlcoholConsump -0.166793

-   Income -0.124718

-   PhysHlth -0.057332

-   Education -0.036977

-   MentHlth -0.030262

-   Fruits -0.025697

-   PhysActivity -0.016740

-   Veggies -0.011804

**Model 2: Logistic Regression with a simple binary variable**

1.  **Analysis Undertaken**

A logistic regression was conducted with the target variable reduced to 2 outcome codes:

-   Diabetes (code 0): 35,346 individual responses

-   Prediabetes (code 1): 4,631 individual responses

The aim was to understand the factors that lead from prediabetes to diabetes.

**Findings**

This logistic regression comparing prediabetes with diabetes showed limited ability to distinguish between the two groups, achieving only moderate performance (ROC AUC = 0.62) despite the large sample size. Indeed, the performance for identifying prediabetes was particularly weak, reflecting both the severe class imbalance and the close similarity between the two metabolic states.

Overall, the available variables do not provide enough differentiation to reliably separate prediabetes from diabetes.

**Findings**

The logistic regression model demonstrated moderate overall performance, achieving an accuracy of 59% and a ROC AUC of 0.624, indicating limited ability to distinguish between prediabetes and diabetes.

**Classification report**

The model accuracy was 59%. ROC AUC was 0.6241.

| **Variable: Class** | **precision** | **recall** | **f1-score** | **Support** |
|---------------------|---------------|------------|--------------|-------------|
| Diabetes (0)        | 0.9153        | 0.5949     | 0.7211       | 7070        |
| Prediabetes (1)     | 0.1579        | 0.5799     | 0.2482       | 926         |
|                     |               |            |              |             |
| Accuracy            |               |            | 0.5932       | 7996        |
| macro avg           | 0.5366        | 0.5874     | 0.4847       | 7996        |
| weighted avg        | 0.8276        | 0.5932     | 0.6664       | 7996        |

**Model 2: Logistic Regression Confusion Matrix**

The model correctly identifies 4,206 out of 7,070 cases, but 2,864 are misclassified as prediabetes. 537 out of 926 cases are correctly predicted as prediabetes, while 389 are misclassified as diabetes.

The model could be useful for initial screening but lacks the precision required for a formal diagnosis.

<img src="media\media\image6.png" style="width:3.76944in;height:2.491in" />

**Prediabetes (class 1): top positive features:**

NoDocbcCost 0.096627

HvyAlcoholConsump 0.095689

MentHlth 0.090416

PhysActivity 0.020658

PhysHlth 0.012075

Fruits 0.011002

Income -0.001100

Smoker -0.013267

Veggies -0.022703

AnyHealthcare -0.023970

**Prediabetes (class 1): top negative features:**

HighChol -0.032735

Education -0.037476

Age -0.048128

DiffWalk -0.056069

Sex -0.077414

Stroke -0.080416

HeartDiseaseorAttack -0.114240

BMI\_winsorised -0.130547

HighBP -0.166303

GenHlth -0.283423

**Random Forest**

**Description of Random Forest**

A random forest is an ensemble machine‑learning method that builds many decision trees and combines their predictions to produce a more stable, accurate result. Each tree sees a slightly different sample of the data and a random subset of features, which reduces overfitting and captures complex, non‑linear relationships. Because of this structure, random forests tend to perform well on noisy, imbalanced, or high‑dimensional datasets like health surveys.

**Analysis undertaken with 3 and 2 classes.**

**Model 3: Random Forest with 3 Classes**

An initial Random Forest was undertaken with 3 classes:

-   0 = No diabetes: 213,703 individual responses

-   1 = Prediabetes: 4,631 individual responses

-   2 = Diabetes: 35,346 individual responses

**Findings**

This model achieves an 84% accuracy, which is almost entirely driven by the 'no diabetes' class, i.e., the dominant class. It has extremely poor recall for prediabetes as well as for diabetes, which may be problematic in a real-world setting.

Feature importance is dominated by BMI, age, income, physical and general health, which are known diabetes risk factors.

**Classification report**

The model accuracy was 84%.

| **Variable: Class** | **Precision** | **recall** | **f1-score** | **Support** |
|---------------------|---------------|------------|--------------|-------------|
| No diabetes (0)     | 0.8594        | 0.9696     | 0.9112       | 42741       |
| Prediabetes (1)     | 0.0000        | 0.0000     | 0.0000       | 926         |
| Diabetes (2)        | 0.4764        | 0.1597     | 0.2392       | 7069        |
|                     |               |            |              |             |
| Accuracy            |               |            | 0.8390       | 50736       |
| macro avg           | 0.4452        | 0.3764     | 0.3835       | 50736       |
| weighted avg        | 0.7903        | 0.8390     | 0.8009       | 50736       |

**Model 3: Random Forest with 3 Classes Confusion Matrix**

The model mostly correctly predicts no diabetes (41,441 predictions) but 1,300 cases are misclassified, mainly as diabetes (1,172 cases)

The model completely misses the prediabetes class, mostly misclassifying as no diabetes (857 cases) which suggests that it may not be able to make a meaningful decision for this category.

There is a diabetes underprediction, with the model heavily favouring predicting ‘no diabetes,’ even for true diabetes cases (5,925 cases), which could be extremely problematic.

A key reason for this is likely to be the imbalance in the dataset with the dominance of ‘no diabetes’ predictions, which may be skewing the model’s decision-making.

The model’s failure to reliably distinguish the high-risk groups means that it will have limited usefulness in a real-world setting.

<img src="media\media\image7.png" style="width:3.41632in;height:2.88889in" />

Top 15 feature importances:

-   BMI\_winsorised 0.176090

-   Age 0.136864

-   Income 0.098828

-   PhysHlth 0.078618

-   GenHlth 0.071413

-   Education 0.068487

-   MentHlth 0.065723

-   Smoker 0.035564

-   Fruits 0.035047

-   HighBP 0.034379

-   Sex 0.033271

-   Veggies 0.027300

-   PhysActivity 0.027211

-   HighChol 0.026885

-   DiffWalk 0.018963

<img src="media\media\image8.png" style="width:6.26806in;height:4.66111in" />

**Improving the Model**

To improve the model, two further actions were undertaken:

-   SMOTE oversampling to increase representation of minority classes.

-   Class-based weighting

**SMOTE**

**Definition of SMOTE**

SMOTE is a resampling technique used to fix class imbalance by creating synthetic minority‑class examples rather than simply duplicating existing ones. It works by selecting a minority sample, finding its nearest neighbours, and generating new points along the line between them, which helps the model learn a fuller decision boundary instead of being overwhelmed by the majority class.

**Results**

SMOTE did not improve the model. Its findings are not included.

**Class-Based Weights**

**Definition of Class-Based Weights**

Class-based weights are a mechanism used in machine learning models to compensate for imbalanced datasets like this one by giving more influence on the underrepresented classes during training.

When one class dominates (e.g. the ‘no diabetes’ class represents 84% of the dataset), a model can achieve high accuracy simply by predicting the majority class. Class-based weights counteract this by:

-   Increasing the penalty for misclassifying minority-class samples

-   Reducing the penalty for misclassifying majority-class samples

-   Shifting the model’s decision boundaries so it pays more attention to the minority class.

**Model 4: Random Forest with 2 Classes and class-based weighting**

A second Random Forest model was undertaken with 2 classes:

-   0 = No diabetes: 213,703 individual responses

-   1 = Prediabetes/Diabetes: 39,977 individual responses

**Findings**

The model achieved 74% accuracy. Once again, the model was strong at identifying individuals without diabetes while still capturing the most at‑risk cases despite the class imbalance. Feature importance results highlight that overall health status, blood pressure and BMI are the dominant predictors for diabetes.

**Classification report**

The model accuracy was 74%.

| **Variable: Class**      | **precision** | **Recall** | **f1-score** | **Support** |
|--------------------------|---------------|------------|--------------|-------------|
| No diabetes (0)          | 0.9396        | 0.7395     | 0.8276       | 42741       |
| Prediabetes/Diabetes (1) | 0.3488        | 0.7460     | 0.4753       | 7995        |
|                          |               |            |              |             |
| Accuracy                 |               |            | 0.7405       | 50736       |
| macro avg                | 0.6442        | 0.7427     | 0.6515       | 50736       |
| weighted avg             | 0.8465        | 0.7405     | 0.7721       | 50736       |

**Model 4: Random Forest (2 Classes and Class-Based Weighting) Confusion Matrix**

Recall is the most important metric in this diagnostic setting, and it is strong and similar for both classes (i.e. no diabetes and prediabetes/diabetes), with the model identifying circa 75% of cases.

However, the precision is not so good as 11,135 healthy individuals are incorrectly flagged as having a diabetes risk. Equally, 2,031 individuals who have pre/diabetes are incorrectly flagged as no diabetes.

This means in a real-world setting, the model may be useful for initial screening, but it is not reliable for confirming a formal prediabetes or diabetes diagnosis.

<img src="media\media\image9.png" style="width:3.94514in;height:3.31197in" />

Top 15 feature importances:

-   GenHlth 0.214270

-   HighBP 0.178877

-   BMI\_winsorised 0.149961

-   Age 0.111840

-   HighChol 0.085582

-   Income 0.044127

-   DiffWalk 0.042807

-   PhysHlth 0.040593

-   HeartDiseaseorAttack 0.022892

-   Education 0.020479

-   MentHlth 0.018176

-   Sex 0.012761

-   PhysActivity 0.011353

-   Smoker 0.010054

-   Fruits 0.009378

<img src="media\media\image10.png" style="width:5.02831in;height:3.7665in" />

These top 15 features were then grouped into 1 of 5 groups as follows:

**Clinical / Physiological:**

-   GenHlth

-   HighBP

-   BMI\_winsorised

-   HighChol

-   HeartDiseaseorAttack

**Demographic:**

-   Age

-   Sex

**Functional Health:**

-   DiffWalk

-   PhysHlth

-   MentHlth

**Socioeconomic:**

-   Income

-   Education

**Lifestyle:**

-   Smoker

-   Fruits

-   PhysActivity.

**Groups:**

-   Clinical/Physiological: 67%

-   Functional health: 12.8%

-   Demographic: 10.4%

-   Socioeconomic: 6.6%

-   Lifestyle: 3.2%

> <img src="media\media\image11.png" style="width:5.85675in;height:3.55in" />

**Hyperparameter Tuning for Random Forest**

Hyperparameter tuning for Random Forest controls how the forest learns to provide better predictions, better generalisations, and more stable models. Random Forest already reduces over-fitting by averaging many trees. Hyperparameter tuning fin-tunes the bias-variance trade-off.

**Model 5: Random Forest Model with Hyperparameter Tuning**

A final Random Forest model with hyperparameter tuning was generated with 2 classes:

-   0 = no diabetes: 213,703 individual responses

-   1 = prediabetes/diabetes: 39,977 individual responses

**Please Note**

This element of the model led to the computer crashing and hanging on numerous occasions. However, it does perform best, and this is the model used in the presentation and dashboard.

**Findings**

The model achieves a recall of 55% for the prediabetes/diabetes class, correctly identifying 4,320 individuals with elevated risk. However, the precision for this class is 41%, indicating that many individuals flagged as “at risk” do not actually have diabetes (6,302). At the same time, the model misses 3,675 true cases, predicting “no diabetes” for individuals who do in fact have the condition.

The model has value as a broad early-stage screening tool, but its performance is not strong enough for diagnostic confirmation.

**Classification report**

The model accuracy was 80%.

| **Variable: Class**      | **precision** | **Recall** | **f1-score** | **Support** |
|--------------------------|---------------|------------|--------------|-------------|
| No diabetes (0)          | 0.9084        | 0.8525     | 0.8796       | 42741       |
| Prediabetes/Diabetes (1) | 0.4067        | 0.5483     | 0.4641       | 7995        |
|                          |               |            |              |             |
| Accuracy                 |               |            | 0.8034       | 50736       |
| macro avg                | 0.6575        | 0.6964     | 0.6718       | 50736       |
| weighted avg             | 0.8293        | 0.8034     | 0.8141       | 50736       |

<img src="media\media\image12.png" style="width:4.79696in;height:4.03822in" />

All feature importance:

-   BMI\_winsorised: 0.156779

-   GenHlth: 0.145500

-   Age: 0.117952

-   HighBP: 0.107613

-   Income: 0.068414

-   PhysHlth: 0.064184

-   HighChol: 0.057104

-   MentHlth: 0.048144

-   Education: 0.043550

-   DiffWalk: 0.030598

-   Smoker: 0.021375

-   Fruits: 0.021355

-   Sex: 0.020849

-   HeartDiseaseorAttack: 0.019409

-   PhysActivity: 0.019118

-   Veggies: 0.017157

-   NoDocbcCost: 0.010246

-   HvyAlcoholConsump: 0.009233

-   Stroke: 0.007801

-   CholCheck: 0.007309

-   AnyHealthcare: 0.006308

The model built the following groups:

-   Clinical/Physiological: 50.2%

-   Demographic: 13.9%

-   Functional health: 14.3%

-   Socioeconomic: 12.85%

-   Lifestyle: 8.8%

<img src="media\media\image13.png" style="width:6.26806in;height:3.85in" />

**SHAP**

SHAP (SHapley Additive exPlanations)

A method that shows how much each feature pushes a prediction up or down, using ideas from cooperative game theory.

Why it matters

-   It tells you which features matter most.

-   It shows whether a high or low value increases risk.

-   It gives transparent, model‑agnostic explanations for complex models like Random Forests or XGBoost.

**Findings**

The SHAP summary shows that **clinical health measures** (general health, BMI, blood pressure, cholesterol) were the strongest drivers of diabetes‑risk predictions, **demographics** (age and income) were the next most influential, **functional limitations** added meaningful but smaller impact, and **lifestyle behaviours** contributed the least compared with the other factor groups.

<img src="media\media\image14.png" style="width:6.26806in;height:7.63194in" />

**Further Research Opportunities**

Feature-level investigations:

-   Partial dependence analysis to understand how individual predictors influence predicted diabetes risk.

-   SHAP value decomposition to provide model‑agnostic explanations and highlight non‑linear or interaction effects.

-   Interaction term exploration within logistic models to test whether combinations of variables meaningfully shift risk.

Alternative modelling strategies:

-   Gradient boosting approaches (e.g., XGBoost, LightGBM, CatBoost) which often handle imbalance and non‑linear structure more effectively than random forests.

-   Calibration analysis to assess whether predicted probabilities reflect true risk, especially important in screening contexts.

Class imbalance–focused techniques:

-   Synthetic data generation using SMOTE variants (SMOTE‑NC, Borderline‑SMOTE) tailored to mixed data types.

-   One‑class classification to model prediabetes as an anomaly detection problem rather than a multi‑class task.

-   Threshold optimisation to tune decision boundaries for sensitivity vs specificity trade‑offs.
