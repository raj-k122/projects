# -*- coding: utf-8 -*-
"""Netflix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ml4UlmY1zXYKoeg3WqBoF3BVvTYHW0t8

**Import libraries**
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""**Load data and clean it** """

netflix = pd.read_csv(r"/content/netflix_titles.csv")
netflix = netflix.drop(['show_id'], axis = 1)
netflix.drop(netflix.index[netflix['type'] == 'TV Show'], inplace=True)
netflix['duration'] = netflix['duration'].map(lambda x: x.rstrip(' min'))
netflix = netflix.reset_index()
netflix = netflix.drop(['index'], axis = 1)
print(netflix.head(10))

""" **Convert object values to integer where required** """

time = netflix['duration'].astype(str).astype(int)
release = netflix['release_year'].astype(str).astype(int)
print(time.head())
print(release.head())
plt.scatter(release, time)

"""**Locate movies longer than 2 hrs and store in a variable**"""

long_movies = netflix.loc[(time > 120)]
print(long_movies)

x = long_movies['release_year'].astype(str).astype(int)
y = long_movies['duration'].astype(str).astype(int)
plt.scatter(x, y))

"""**Plot the data**"""

long_movies.plot(kind='hist')
plt.ylabel('Movies longer than 2 hours')
plt.xlabel('Release Year')
plt.title('Number of long movies over the years')
plt.show()