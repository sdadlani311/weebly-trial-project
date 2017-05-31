import datetime
from index import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    sites = db.relationship('Site', backref='user')
    signup_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email
        self.signup_date = datetime.datetime.now()

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Site(db.Model):

    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String, unique=True, nullable=False)
    url = db.Column(db.String, nullable=False)
    pages = db.relationship('Page', backref='site')
    published = db.Column(db.Boolean, default=False)

    def __init__(self, user_id, title, url, published):
        self.user_id = user_id
        self.title = title
        self.url = url
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Page(db.Model):

    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'))
    url = db.Column(db.String, nullable=False)
    elements = db.relationship('Element', backref='page')
    order = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, site_id, url, order):
        self.site_id = site_id
        self.url = url
        self.order = order

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Element(db.Model):

    __tablename__ = "elements"

    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    attributes = db.Column(db.String)
    content = db.Column(db.Text)
    order = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, page_id, attributes, content, order):
        self.page_id = page_id
        self.attribute = attributes
        self.content = content
        self.order = order

    def __repr__(self):
        return '<id {}>'.format(self.id)
