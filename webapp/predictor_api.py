import pandas as pd
import pickle as pkl
import numpy as np
from scipy.spatial.distance import pdist

tsne = pd.read_csv('tsne_df_v1.csv')

with open('web_features.pkl', 'rb') as f:
    artist_features = pkl.load(f)

with open('scaled_df_v1.pkl', 'rb') as f:
    data = pkl.load(f)

def show_stats(artist):
    return artist_features.loc[artist]

def recommend(artist, n_recs=5):
    """
    calculate n_recs closest artists in data by euclidean distance
    """
    distances = []
    target = data.loc[artist].to_numpy()
    artist_list = list(data.index)
    artist_list.remove(artist)
    
    for name in artist_list:
        comparison = data.loc[name].to_numpy()
        stack = np.vstack((target, comparison))
        dist = pdist(stack)
        # dist = pairwise_distances(target, comparison)
        distances.append(dist[0])

    top_n_ind = np.argsort(distances)[0:n_recs]
    
    return [artist_list[i] for i in top_n_ind]

# def show_pic(artist):

# def show_songs(artist):