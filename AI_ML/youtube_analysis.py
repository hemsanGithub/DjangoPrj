import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

import warnings
from collections import Counter
import datetime
import wordcloud
import json

df = pd.read_csv("USvideos.csv")
PLOT_COLORS = ["#268bd2", "#0052CC", "#FF5722", "#b58900", "#003f5c"]
pd.options.display.float_format = '{:.2f}'.format
sns.set(style="ticks")
plt.rc('figure', figsize=(8, 5), dpi=100)
plt.rc('axes', labelpad=20, facecolor="#ffffff", linewidth=0.4, grid=True, labelsize=14)
plt.rc('patch', linewidth=0)
plt.rc('xtick.major', width=0.2)
plt.rc('ytick.major', width=0.2)
plt.rc('grid', color='#9E9E9E', linewidth=0.4)
plt.rc('font', family='Arial', weight='400', size=10)
plt.rc('text', color='#282828')
plt.rc('savefig', pad_inches=0.3, dpi=300)

df["description"] = df["description"].fillna(value="")
# print(df.describe())

def contains_capitalized_word(s):
    for w in s.split():
        if w.isupper():
            return True
    return False


df["contains_capitalized"] = df["title"].apply(contains_capitalized_word)

value_counts = df["contains_capitalized"].value_counts().to_dict()
fig, ax = plt.subplots()
_ = ax.pie([value_counts[False], value_counts[True]], labels=['No', 'Yes'], 
           colors=['#003f5c', '#ffa600'], textprops={'color': '#040204'}, startangle=65)
_ = ax.axis('equal')
_ = ax.set_title('Title Contains Capitalized Word?')

print(plt.show())



# df["title_length"] = df["title"].apply(lambda x: len(x))

# fig, ax = plt.subplots()
# _ = sns.distplot(df["title_length"], kde=False, rug=False, 
#                  color=PLOT_COLORS[4], hist_kws={'alpha': 1}, ax=ax)
# _ = ax.set(xlabel="Title Length", ylabel="No. of videos", xticks=range(0, 110, 10))

# # print(plt.show())



# fig, ax = plt.subplots()
# _ = ax.scatter(x=df['views'], y=df['title_length'], color=PLOT_COLORS[2], edgecolors="#000000", linewidths=0.5)
# _ = ax.set(xlabel="Views", ylabel="Title Length")

# # print(plt.show())
# # Select only numeric columns for correlation
# df_numeric = df.select_dtypes(include=['number','bool'])

# h_labels = [str(x).replace('_', ' ').title() for x in df_numeric.columns]

# fig, ax = plt.subplots(figsize=(10,6))
# _ = sns.heatmap(df_numeric.corr(), annot=True, xticklabels=h_labels, yticklabels=h_labels, cmap=sns.cubehelix_palette(as_cmap=True), ax=ax)

# # print(plt.show())


# title_words = list(df["title"].apply(lambda x: x.split()))
# title_words = [x for y in title_words for x in y]
# wc = wordcloud.WordCloud(width=1200, height=500, 
#                          collocations=False, background_color="white", 
#                          colormap="tab20b").generate(" ".join(title_words))
# plt.figure(figsize=(15,10))
# plt.imshow(wc, interpolation='bilinear')
# _ = plt.axis("off")

# # print(plt.show())


