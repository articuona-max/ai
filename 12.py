import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score


df = pd.read_csv('student.csv')
df['pass']  = df['marks']>=25
print(df)

x= df[['hrs_studied', 'marks']]
y= df['pass']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6)
model = DecisionTreeClassifier()
model.fit(x, y)

y_pred = model.predict(x_test)

print(f'prediction of {x_test} is \n{y_pred}')
print(f'naccuracy_score = {accuracy_score(y_pred, y_test)}')
print(f'classification_report = {classification_report(y_pred, y_test)}')
