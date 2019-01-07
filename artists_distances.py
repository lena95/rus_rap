import json
from glob import glob
import os
import urllib.parse
from rus_rap.uniqueNames import normilizeArtist
from rus_rap.preprocessing import text_stemming
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.manifold import MDS

MDS()

DIR_PATH_TEXTS = ".\\textsByArtist"
DIR_PATH_WORDS = ".\\sortWordFreq"

textArtist = dict()


def getWordSet(filename):
    result = set()
    file = open(DIR_PATH_WORDS + "\\" + filename)
    for line in file:
        result.add(line.split(" ")[0])
    return result


for path in glob(os.path.join(os.path.expanduser(DIR_PATH_TEXTS), '*.json')):
    nameFile = os.path.basename(path)[:os.path.basename(path).rfind('.')]  # without extension
    print(nameFile)
    file = open(path, mode="r", encoding="maccyrillic")
    data = json.load(file)
    artist = urllib.parse.unquote(data["artist"]).encode('maccyrillic').decode('utf-8')
    wordSet = getWordSet(nameFile)

    texts = list()
    print(len(data['texts']))
    for text in data['texts']:
        texts.append(text_stemming(urllib.parse.unquote(text).encode('maccyrillic').decode('utf-8', errors="ignore"),
                                   wordDict=wordSet))
    textArtist[artist] = " ".join(texts)

    # print(textArtist[artist])

listArt = np.array(list(textArtist.items()))
print(listArt)

tfidf_vectorizer = TfidfVectorizer(max_df=0.9, max_features=200000,
                                   min_df=0.1,
                                   use_idf=True, ngram_range=(1, 1))

tfidf_matrix = tfidf_vectorizer.fit_transform(listArt[:, 1])
print(tfidf_matrix.shape)

terms = tfidf_vectorizer.get_feature_names()
print(terms)
dist = 1 - cosine_similarity(tfidf_matrix)
print(dist)

mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
xs, ys = pos[:, 0], pos[:, 1]
print(xs)
print(ys)

df = pd.DataFrame(dict(x=xs, y=ys, name=listArt[:, 0]))

df.to_csv("results.csv", sep='\t', encoding='utf-8')

fig, ax = plt.subplots(figsize=(17, 9)) # set size
ax.margins(0.05)
print("-----------------------------------")
print(df)
print("-----------------------------------")

for index, row in df.iterrows():
    ax.plot(row['x'], row['y'], marker='o', linestyle='', ms=12,
            color='#66ff99',
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelbottom='off')
    ax.tick_params(
        axis='y',  # changes apply to the y-axis
        which='both',  # both major and minor ticks are affected
        left='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelleft='off')

for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['name'], size=8)

plt.show()



# print(os.path.basename(path))
# print(os.path.basename(path)[:os.path.basename(path).rfind('.')])


# keyArtist = findArtistsKey(artist)
# if keyArtist is not None:
#     text = text_stemming(urllib.parse.unquote(' '.join(data['text'])).encode('maccyrillic').decode('utf-8', errors="ignore"))
#     docCollection[keyArtist].append(text)