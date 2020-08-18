from app import db


class Teachers(db.Model):
    """ Модель преподавателей """
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    about = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    lesson_time = db.Column(db.String)
    # Ссылка на поле в модели цели (One-to-Many)
    goals = db.relationship("Goals", back_populates="goal")
    # Ссылка на поле в модели рассписание (One-to-Many)
    week_day = db.relationship("TimetableTeachers", back_populates="week")


class Goals(db.Model):
    """ Модель целей занятий """
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False)
    # Ссылка на модель преподавателя (One-to-Many)
    teachers_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    goal = db.relationship("Teachers", back_populates="goals", uselist=False)

    # Ссылка на поле в модели подбора преподавателя (One-to-Many)
    search_teacher = db.relationship("SearchTeacher", back_populates="goal", uselist=False)


class TimetableTeachers(db.Model):
    """ Модель расписания преподавателей на неделю """
    __tablename__ = 'timetables'
    id = db.Column(db.Integer, primary_key=True)
    day_times = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    # ссылка на поле id в модели преподавателя (One-to-Many)
    teachers_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    week = db.relationship("Teachers", back_populates="week_day", uselist=False)
    # ссылка на поле id в модели booking (One-to-Many)
    booking = db.relationship("Booking", back_populates='day_times', uselist=False)


class SearchTeacher(db.Model):
    """ Модель поиска преподавателя по критериям: цели и планируемое кол-во часов занятий в неделю """
    __tablename__ = 'search_teachers'
    id = db.Column(db.Integer, primary_key=True)
    how_time = db.Column(db.String(20), nullable=False)
    client_name = db.Column(db.String(25), nullable=False)
    client_phone = db.Column(db.String(10), nullable=False)
    # Ссылка на поле в модели цели (One-to-Many)
    goal_id = db.Column(db.Integer, db.ForeignKey("goals.id"))
    goal = db.relationship("Goals", back_populates="search_teacher", uselist=False)


class Booking(db.Model):
    """ Модель для записи на пробное занятие к преподавателю """
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(25), nullable=False)
    client_phone = db.Column(db.String(10), nullable=False)
    # ссылка на поле id в модели Teachers (One-to-Many)
    timetable_id = db.Column(db.Integer, db.ForeignKey("timetables.id"))
    # ссылка на поле free и day в модели TimetableTeachers (One-to-One)
    day_times = db.relationship("TimetableTeachers", back_populates="booking", uselist=False)
