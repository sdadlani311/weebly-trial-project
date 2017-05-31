#!/usr/bin/env python
from flask import request, render_template
from flask_restless import APIManager
from index import app, db
from models import User, Site, Page, Element
api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(User, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Site, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Page, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Element, methods=['GET', 'POST', 'DELETE', 'PUT'])

@app.route('/', methods=['GET', 'POST'])
def login():
    # login logic here
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
