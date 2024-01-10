import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score, f1_score, matthews_corrcoef, recall_score
from imblearn.over_sampling import SMOTE


def processdata(file):
    df = pd.read_csv(file)
    
    df[df.isnull().any(axis=1)].head()
    #del df['FEMALE']
    df=df.dropna()
    attributes = df[['Rainfall', 'MinTemp', 'MaxTemp', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm']]
    targets = df['RainTomorrow']
    targets = targets.map({'Yes': 1, 'No': 0})

    #targets = df['RainTomorrow']
    #attributes = df.drop('TOTCHG', axis=1)
    #attributes = df.drop('FEMALE', axis=1)
    smote = SMOTE()
    attributes, targets = smote.fit_resample(attributes, targets)

    train_attributes, test_attributes, train_targets, test_targets \
        = train_test_split(attributes, targets, test_size=0.2, random_state=42)

    return train_attributes, test_attributes, train_targets, test_targets

train_x, test_x, train_y, test_y = processdata('/Users/abhudaysingh/Downloads/weatherAUS.csv')

rf_classifier = DecisionTreeClassifier(max_depth=10, min_samples_split=2, random_state=42)
rf_classifier.fit(train_x, train_y)

auc_scores = []
f1_scores = []
mcc_scores = []
recall_scores = []

cv = KFold(n_splits=5, shuffle=True, random_state=42)

for train_indices, val_indices in cv.split(train_x):
    X_train_fold, X_val_fold = train_x.iloc[train_indices], train_x.iloc[val_indices]
    y_train_fold, y_val_fold = train_y.iloc[train_indices], train_y.iloc[val_indices]
    
    # Use the same hyperparameters for the cross-validation fold
    rf_classifier_fold = DecisionTreeClassifier(max_depth=10, min_samples_split=2, random_state=42)
    rf_classifier_fold.fit(X_train_fold, y_train_fold)
    
    auc_scores.append(roc_auc_score(y_val_fold, rf_classifier_fold.predict(X_val_fold)))
    f1_scores.append(f1_score(y_val_fold, rf_classifier_fold.predict(X_val_fold)))
    mcc_scores.append(matthews_corrcoef(y_val_fold, rf_classifier_fold.predict(X_val_fold)))
    recall_scores.append(recall_score(y_val_fold, rf_classifier_fold.predict(X_val_fold)))

print("AUC:", sum(auc_scores) / len(auc_scores))
print("F1 Score:", sum(f1_scores) / len(f1_scores))
print("Matthews Correlation Coefficient:", sum(mcc_scores) / len(mcc_scores))
print("Recall:", sum(recall_scores) / len(recall_scores))

y_pred = rf_classifier.predict(test_x)
auc = roc_auc_score(test_y, y_pred)
f1 = f1_score(test_y, y_pred)
mcc = matthews_corrcoef(test_y, y_pred)
recall = recall_score(test_y, y_pred)

print("\nTest Set Metrics:")
print("AUC:", auc)
print("F1 Score:", f1)
print("Matthews Correlation Coefficient:", mcc)
print("Recall:", recall)
