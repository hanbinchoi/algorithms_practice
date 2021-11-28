import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


data =pd.read_csv("cyber_data.csv")

feature_list=["num_PID","Property"]

data=data.loc[:,feature_list]


#결측값 제거

data["Property"]=data["Property"].fillna(0)
# data["RelationShip"]=data["RelationShip"].fillna("relation_empty")
# data["Path"]=data["Path"].fillna("Path_empty")
# data["Address"]=data["Address"].fillna("0.0.0.0")

# Property, num_PID 정규화(추가 부분)
def pid_normalization(x):
    if x >= 200:
        return 200
    elif x >=100:
        return 100
    elif x >=80:
        return 80
    elif x >=50:
        return 50
    elif x >=30:
        return 20
    elif x >=20:
        return 10
    elif x >=10:
        return 10
    else:
        return 0

def prop_normalization(x):
    if x >= 200:
        return 200
    elif x >=100:
        return 100
    elif x >=80:
        return 80
    elif x >=50:
        return 50
    elif x >=30:
        return 30
    elif x >=20:
        return 20
    elif x >=10:
        return 10
    elif x >=5:
        return 5
    else:
        return 0
print(data.head())
print()
data["num_PID"] = data["num_PID"].apply(pid_normalization)
data["Property"] = data["Property"].apply(prop_normalization)
print("** After Normalization **")
print(data.head())
#item set
itemset_size = len(data)
itemset_feature =["num_PID","Parent PID","PID","Path","RelationShip","Address","Protocol","Property","Port","UsedFile","family","hash_value"]
item_frequent= dict()
itemset=[0 for i in range(itemset_size)]
for i in range(0,itemset_size):
    each_list =[0 for i in range(len(itemset_feature))]
    for j in range(0, len(itemset_feature)):
        # item frequency
        if data[itemset_feature[j]][i] in item_frequent:
            value = item_frequent[data[itemset_feature[j]][i]]
            item_frequent[data[itemset_feature[j]][i]]=value+1
        else :
            item_frequent[data[itemset_feature[j]][i]]=1
        each_list[j]=data[itemset_feature[j]][i]
    itemset[i]=each_list



#delete under threshold
threshold =2
for i in range(0,len(itemset)):
    for j in range(0,len(itemset[i])):
        if(item_frequent[itemset[i][j]]<threshold):
            itemset[i][j]=-1

for i in range(0,len(itemset)):
    while(-1 in itemset[i]):
        itemset[i].remove(-1)

keylist = item_frequent.keys()



#(ordered) item_frequency
sorted(item_frequent.items(),reverse=True, key=lambda item:item[1])



for i in range(0, len(itemset)):
    #sorting
    index=0
    for j in range(0, len(itemset[i])):
        for k in range(j, len(itemset[i])):
            if(item_frequent[itemset[i][j]]<item_frequent[itemset[i][k]]):
                temp = itemset[i][j]
                itemset[i][j]=itemset[i][k]
                itemset[i][k]=temp




#convert to str
for i in range(0,len(itemset)):
    for j in range(0, len(itemset[i])):
        itemset[i][j]=str(itemset[i][j])


# FP-growth
data = np.array(itemset)
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)

from mlxtend.frequent_patterns import fpgrowth

fpgrowth_result=fpgrowth(df, min_support=0.3, use_colnames=True)

print("Result FP-growth")
print(fpgrowth_result)


#Apriori
from mlxtend.frequent_patterns import apriori
apriori_result=apriori(df, min_support=0.3, use_colnames=True)
print("\nResult Apriori ")
print(apriori_result)