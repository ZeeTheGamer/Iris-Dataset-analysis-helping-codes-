import matplotlib.pyplot as plt
import pandas as pd
import csv

df1 = pd.read_csv("2FeatureResults/Resut_with_n_4_testSize_0.2_2_features.csv")
df2 = pd.read_csv("2FeatureResults/Resut_with_n_4_testSize_0.3_2_features.csv")
df3 = pd.read_csv("2FeatureResults/Resut_with_n_4_testSize_0.4_2_features.csv")
df4 = pd.read_csv("2FeatureResults/Resut_with_n_4_testSize_0.5_2_features.csv")
df5 = pd.read_csv("2FeatureResults/Resut_with_n_4_testSize_0.6_2_features.csv")
df6 = pd.read_csv("2FeatureResults/Resut_with_n_4_testSize_0.7_2_features.csv")


accuracyValues1 = df1['Accuracy']
accuracyValues2 = df2['Accuracy']
accuracyValues3 = df3['Accuracy']
accuracyValues4 = df4['Accuracy']
accuracyValues5 = df5['Accuracy']
accuracyValues6 = df6['Accuracy']


feature_a = df1['Feature A']
feature_b = df1['Feature B']



combinationOfAandBFeature = []

for x in range(len(feature_a)):
    combinationOfAandBFeature.append(feature_a[x]+" - "+feature_b[x])


# Create a Pandas series from a list of values ("[]") and plot it:
#pd.Series(df2[2]).plot(kind="bar")

plt.rcParams["figure.figsize"] = [11, 6]


sample =list(combinationOfAandBFeature)

plotdata = pd.DataFrame({
    "Resut_with_n_4_testSize_0.2_2_features.csv":list(accuracyValues1),
    "Resut_with_n_4_testSize_0.3_2_features.csv":list(accuracyValues2),
    "Resut_with_n_4_testSize_0.4_2_features.csv":list(accuracyValues3),
    "Resut_with_n_4_testSize_0.5_2_features.csv":list(accuracyValues4),
    "Resut_with_n_4_testSize_0.6_2_features.csv":list(accuracyValues5),
    "Resut_with_n_4_testSize_0.7_2_features.csv":list(accuracyValues6),

    },index=sample)

plotdata.plot(kind="bar")

plt.title("Combined Result of Graphs when test size is 0.2-0.7 and N=4 ")
plt.xlabel("Feature Combination")
plt.ylabel("Accuracy") 



