import matplotlib.pyplot as plt
import pandas as pd
import csv


file = "Resut_with_n_5_testSize_0.3_2_features.csv"

df1 = pd.read_csv(file)


accuracyValues1 = df1['Accuracy']

feature_a = df1['Feature A']
feature_b = df1['Feature B']



combinationOfAandBFeature = []

for x in range(len(feature_a)):
    combinationOfAandBFeature.append(feature_a[x]+" - "+feature_b[x])


# Create a Pandas series from a list of values ("[]") and plot it:
#pd.Series(df2[2]).plot(kind="bar")

sample =list(combinationOfAandBFeature)


plotdata = pd.DataFrame({
    file:list(accuracyValues1)
    },index=sample)


plotdata.plot(kind="bar")

plt.title("Result of  "+file)
plt.xlabel("Feature Combination")
plt.ylabel("Accuracy") 


