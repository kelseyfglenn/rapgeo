import flask
from flask import request
from clusta_api import show_stats, recommend

import pickle as pkl

with open('all_artist_urls.pkl', 'rb') as f:
    links = pkl.load(f)

app = flask.Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def landing():
    return flask.render_template('landing.html')

@app.route("/profile", methods=["GET", "POST"])
def get_artist_profile():
    """
    load rapper picture, stats, songs 
    """

    # look for the name searched from the landing page
    artist = request.form['artist']
    query = request.args.to_dict()
    
    if query == {}:
        query = artist
    else:
        query = query['artist']

    stats = show_stats(query)

    return flask.render_template('profile.html',
                                stats = stats,
                                artist = artist,
                                links = links)

@app.route("/recommend", methods=["GET", "POST"])
def get_recs():
    """
    generate recommendations
    """
    artist = request.form['artist']
    query = request.args.to_dict()
    
    if query == {}:
        query = artist
    else:
        query = query['artist']

    recs = recommend(artist, 6)
    stats = [show_stats(rec) for rec in recs]

    return flask.render_template('recommender.html',
                                 recs = recs,
                                 stats = stats,
                                 links = links,
                                 artist = artist)

if __name__=='__main__':
    app.run(debug=True)

