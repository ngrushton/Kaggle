import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tweet = pd.read_csv('Data/train.csv')
test = pd.read_csv('Data/test.csv')
tweet.head(3)

x = tweet.target.value_counts()
sns.barplot(x.index, x)
plt.gca().set_ylabel('samples')
