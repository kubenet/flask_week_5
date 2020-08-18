from app import db


class Persons(db.Model):
    """ Модель пользователь """
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    orders = db.relationship("Goals", back_populates="goal")


class Meals(db.Model):
    """ Модель блюдо """
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    description = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String, nullable=False)
    category = db.relationship("Categories", back_populates="title")


class Categories(db.Model):
    """ Модель категории """
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    goal = db.relationship("Meals", back_populates="goals", uselist=False)


class Orders(db.Model):
    """ Модель заказы """
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    sum = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    list_meals = db.Column(db.String, nullable=False)
