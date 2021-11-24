import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


data =pd.read_csv("cyber_data.csv")

feature_list=["file_name","num_PID","PID","Parent PID","Property","RelationShip","Path","Protocol","Address"]

data=data.loc[:,feature_list]


#결측값 제거 임시

data=data.fillna(method='ffill')
data=data.fillna(method='bfill')


#숫자 타입으로 변경 (encoding)

encoder = LabelEncoder()

encoder.fit(data["file_name"])
data["file_name"] = pd.DataFrame(encoder.transform(data["file_name"]))

encoder.fit(data["PID"])
data["PID"] =pd.DataFrame(encoder.transform(data["PID"]))

encoder.fit(data["RelationShip"])
data["RelationShip"] =pd.DataFrame(encoder.transform(data["RelationShip"]))

encoder.fit(data["Path"])
data["Path"] =pd.DataFrame(encoder.transform(data["Path"]))

encoder.fit(data["Protocol"])
data["Protocol"] =pd.DataFrame(encoder.transform(data["Protocol"]))

encoder.fit(data["Address"])
data["Address"] =pd.DataFrame(encoder.transform(data["Address"]))


# 추가 -> Min-max Normalization
f = data[["num_PID","Property"]]

min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(f)

f = min_max_scaler.transform(f)
f = pd.DataFrame(f,columns=["num_PID","Property"])


data = data.drop(["num_PID","Property"],axis=1)
data[["num_PID","Property"]] = f[["num_PID","Property"]]


#target 임시 (Parent PID)
X= data.drop(columns=['Parent PID'])
y=data['Parent PID']

#train, test set = 8 : 2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#decision Tree
decision = DecisionTreeClassifier(criterion='entropy', max_depth=15, random_state=30)
decision.fit(X_train, y_train)
y_pred = decision.predict(X_test)

print("accuracy: %.3f" %accuracy_score(y_test, y_pred))

# confusion matrix
print('[Decision Tree]')
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'], margins= True)
sns.heatmap(confusion_matrix, annot=True, fmt = 'd')
plt.show()

# classification report
print(classification_report(y_test, y_pred))



