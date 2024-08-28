# Cardekho
Data Cleaning and Structuring
Data Extraction:
The data extraction functions car_overview_dict_creator, car_feature_dict_creator, and car_spec_dict_creator are designed to parse JSON strings and extract relevant information into dictionaries.
These extracted details are then converted into pandas DataFrames for further processing.
Data Concatenation:
Loaded and processed car data from different cities (Bangalore, Chennai, Delhi, Hyderabad, Jaipur, Kolkata).
After processing, the data is concatenated into a single DataFrame and saved as car_details.csv.
Data Cleaning:
Dropped unnecessary columns, handle missing values, and standardize price values using the convert_to_lakhs function.
Columns with units are identified and cleaned, converting them into numerical values where applicable.
Object columns are converted to numerical where possible.
Outlier Removal:
The IQR method is used to remove outliers, ensuring the data's robustness for model training.
Imputation:
Missing values in numerical columns are imputed based on skewness, either using the mean or median.
Categorical columns are imputed using the mode.
Feature Selection and Modeling:
Label Encoding:
Categorical columns are label-encoded to prepare the data for machine learning models.
Model Training:
Used several models, including Linear Regression, Decision Tree Regressor, and Random Forest Regressor.
For each model, you split the data into training and testing sets, train the model, and evaluate its performance using metrics like Mean Squared Error (MSE) and R².
Feature Selection:
Recursive Feature Elimination (RFE) is applied to identify the top 10 features most relevant to predicting car prices.
Model Selection
The high R2 after hyper tuning got the Gradient Bossting Regressor. Used the model to predict the car price value through streamlit
