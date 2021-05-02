import matplotlib.pyplot as plt
import pandas as pd
import csv
import seaborn as sns
sns.set_style("dark")

df1 = pd.read_csv("3FeatureResults/Resut_with_n_4_testSize_0.2_3_features.csv")
df2 = pd.read_csv("3FeatureResults/Resut_with_n_4_testSize_0.3_3_features.csv")
df3 = pd.read_csv("3FeatureResults/Resut_with_n_4_testSize_0.4_3_features.csv")
df4 = pd.read_csv("3FeatureResults/Resut_with_n_4_testSize_0.5_3_features.csv")
df5 = pd.read_csv("3FeatureResults/Resut_with_n_4_testSize_0.6_3_features.csv")
df6 = pd.read_csv("3FeatureResults/Resut_with_n_4_testSize_0.7_3_features.csv")


accuracyValues1 = df1['Accuracy']
accuracyValues2 = df2['Accuracy']
accuracyValues3 = df3['Accuracy']
accuracyValues4 = df4['Accuracy']
accuracyValues5 = df5['Accuracy']
accuracyValues6 = df6['Accuracy']


feature_a = df1['Feature A']
feature_b = df1['Feature B']
feature_c = df1['Feature C']



combinationOfAandBFeature = []

for x in range(len(feature_a)):
    combinationOfAandBFeature.append(feature_a[x]+" - "+feature_b[x]+" - "+feature_c[x])


# Create a Pandas series from a list of values ("[]") and plot it:
#pd.Series(df2[2]).plot(kind="bar")

plt.rcParams["figure.figsize"] = [11, 6]


sample =list(combinationOfAandBFeature)

plotdata = pd.DataFrame({
    "a":list(accuracyValues1),
    "b":list(accuracyValues2),
    "c":list(accuracyValues3),
    "d":list(accuracyValues4),
    "e":list(accuracyValues5),
    "f":list(accuracyValues6),

    },index=sample)

plotdata.plot(kind="bar")

plt.title("Combined Result of Graphs when test size (0.2-0.7) (3-Selected)")
plt.xlabel("Feature Combination")
plt.ylabel("Accuracy") 



