from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Menu, Quote


@app.route('/')
def index():
    menus = Menu.query.all()
    return render_template('form.html', menus=menus)


@app.route('/quote', methods=['POST'])
def quote():
    group_size = int(request.form['group_size'])
    menu_id = int(request.form['menu'])
    menu = Menu.query.get(menu_id)
    total_price = group_size * menu.price_per_person

    # Enregistrer le devis
    quote = Quote(group_size=group_size, menu_id=menu_id, total_price=total_price)
    db.session.add(quote)
    db.session.commit()

    return render_template('result.html', group_size=group_size, menu=menu, total_price=total_price)
