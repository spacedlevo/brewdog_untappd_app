from flask import render_template
from brewdog_app import app
import sqlite3


@app.route('/')
def index():
    db = sqlite3.connect('/home/levo/Documents/projects/brewdog/beer_db.sqlite')
    c = db.cursor()
    c.execute(''' SELECT bar FROM bars''')
    bar_locations = c.fetchall()
    c.execute('''  SELECT beers.name, style.style, beers.abv, brewery.name, bars.bar, beers.rating, beers.description, beers.image_url
        FROM beers JOIN bars JOIN beer_location JOIN brewery JOIN style
        ON beer_location.beer_id = beers.id AND beer_location.bar_id = bars.id AND beers.brewery_id = brewery.id AND beers.style_id = style.id
        WHERE bars.bar = ?
        ORDER BY beers.rating DESC
    ''',
              ('Liverpool', ))

    beers = c.fetchall()
    db.close()

    return render_template('index.html', title='Liverpool', beers=beers, bars=bar_locations)


@app.route('/<bar>')
def bar_taplist(bar):
    db = sqlite3.connect('/home/levo/Documents/projects/brewdog/beer_db.sqlite')
    c = db.cursor()
    c.execute(''' SELECT bar FROM bars''')
    bar_locations = c.fetchall()
    c.execute('''  SELECT beers.name, style.style, beers.abv, brewery.name, bars.bar, beers.rating, beers.description, beers.image_url
        FROM beers JOIN bars JOIN beer_location JOIN brewery JOIN style
        ON beer_location.beer_id = beers.id AND beer_location.bar_id = bars.id AND beers.brewery_id = brewery.id AND beers.style_id = style.id
        WHERE bars.bar = ?
        ORDER BY beers.rating DESC
    ''',
              (bar, ))

    beers = c.fetchall()
    db.close()

    return render_template('index.html', title=bar, beers=beers, bars=bar_locations)
