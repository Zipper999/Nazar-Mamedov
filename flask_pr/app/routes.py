from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item
from . import db

# Создаем Blueprint
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            new_item = Item(name=name)
            db.session.add(new_item)
            db.session.commit()
        return redirect(url_for('main.items'))
    items = Item.query.all()
    return render_template('items.html', items=items)

@bp.route('/delete/<int:id>')
def delete_item(id):
    item = Item.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('main.items'))
@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        new_name = request.form.get('name')
        if new_name:
            item.name = new_name
            db.session.commit()
            return redirect(url_for('main.items'))
    return render_template('update_item.html', item=item)