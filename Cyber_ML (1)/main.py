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
#
#
# data =pd.read_csv("cyber_data.csv")
#
# feature_list=["file_name","num_PID","PID","Parent PID","Property","RelationShip","Path","Protocol","Address"]
#
# data=data.loc[:,feature_list]
#
#
# #결측값 제거 임시
#
# data=data.fillna(method='ffill')
# data=data.fillna(method='bfill')
#
#
# #숫자 타입으로 변경 (encoding)
#
# encoder = LabelEncoder()
#
# encoder.fit(data["file_name"])
# data["file_name"] = pd.DataFrame(encoder.transform(data["file_name"]))
#
# encoder.fit(data["PID"])
# data["PID"] =pd.DataFrame(encoder.transform(data["PID"]))
#
# encoder.fit(data["RelationShip"])
# data["RelationShip"] =pd.DataFrame(encoder.transform(data["RelationShip"]))
#
# encoder.fit(data["Path"])
# data["Path"] =pd.DataFrame(encoder.transform(data["Path"]))
#
# encoder.fit(data["Protocol"])
# data["Protocol"] =pd.DataFrame(encoder.transform(data["Protocol"]))
#
# encoder.fit(data["Address"])
# data["Address"] =pd.DataFrame(encoder.transform(data["Address"]))
#
#
# # 추가 -> Min-max Normalization
# f = data[["num_PID","Property"]]
#
# min_max_scaler = MinMaxScaler()
# fitted = min_max_scaler.fit(f)
#
# f = min_max_scaler.transform(f)
# f = pd.DataFrame(f,columns=["num_PID","Property"])
#
#
# data = data.drop(["num_PID","Property"],axis=1)
# data[["num_PID","Property"]] = f[["num_PID","Property"]]
#
#
# #target 임시 (Parent PID)
# X= data.drop(columns=['Parent PID'])
# y=data['Parent PID']
#
# #train, test set = 8 : 2
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# #decision Tree
# decision = DecisionTreeClassifier(criterion='entropy', max_depth=15, random_state=30)
# decision.fit(X_train, y_train)
# y_pred = decision.predict(X_test)
#
# print("accuracy: %.3f" %accuracy_score(y_test, y_pred))
#
# # confusion matrix
# print('[Decision Tree]')
# confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'], margins= True)
# sns.heatmap(confusion_matrix, annot=True, fmt = 'd')
# plt.show()
#
# # classification report
# print(classification_report(y_test, y_pred))
#
import mlxtend
import numpy as np
import pandas as pd

# 데이터 불러오기
data =pd.read_csv("cyber_data.csv")
feature_list=["num_PID","PID","Parent PID","Property","RelationShip","Protocol","Address","Port","UsedFile","family"]
data=data.loc[:,feature_list]

# 결측값 제거
data = data.fillna({"RelationShip":"no-relation"})
data = data.fillna({"Property":0})
data = data.fillna({"Address":"no-addr"})

# num_PID, property 정규화
def pid_normalization(x):
    if x >= 200:
        return "pid_num:200"
    elif x >=100:
        return "pid_num:100"
    elif x >=80:
        return "pid_num:80"
    elif x >=50:
        return "pid_num:50"
    elif x >=30:
        return "pid_num:30"
    elif x >=20:
        return "pid_num:20"
    elif x >=10:
        return "pid_num:10"
    else:
        return "pid_num:0"

def prop_normalization(x):
    if x >= 200:
        return "property:200"
    elif x >=100:
        return "property:100"
    elif x >=80:
        return "property:80"
    elif x >=50:
        return "property:50"
    elif x >=30:
        return "property:30"
    elif x >=20:
        return "property:20"
    elif x >=10:
        return "property:10"
    elif x >=5:
        return "property:5"
    else:
        return "property:0"

data["num_PID"] = data["num_PID"].apply(pid_normalization)
data["Property"] = data["Property"].apply(prop_normalization)
print(data.info())

def paret_PID_str(x):
    return "Parent PID:"+str(x)
def port_str(x):
    return "Port:"+str(x)
def usedFile_str(x):
    return "UsedFile:"+str(x)

# 모든 컬럼 문자열로 변경
data["Parent PID"] = data["Parent PID"].apply(paret_PID_str)
data["Port"] = data["Port"].apply(port_str)
data["UsedFile"] = data["UsedFile"].apply(usedFile_str)

data = data.to_numpy()
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)

from mlxtend.frequent_patterns import fpgrowth

print(fpgrowth(df, min_support=0.2, use_colnames=True))