from flask import Flask

# from database.db import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:stackoverflow@localhost:5432/FYP"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "adminusers"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String, unique=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"name: {self.name}, email: {self.email}"


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    num_plate = db.Column(db.String(7), nullable=False, unique=True)
    type = db.Column(db.String, nullable=False)
    suspicious = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"Vehicle(number playe={self.num_plate}, type={self.type}, suspicious={self.suspicious})"


class Registered(db.Model):
    """
    Registered User
    """

    __tablename__ = "registered"

    regid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    cnic = db.Column(db.String, nullable=False)
    contactno = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    dor = db.Column(db.DateTime, nullable=False)
    doe = db.Column(db.DateTime, nullable=False)
    vehicle_id = db.Column(
        db.Integer, db.ForeignKey("vehicles.id"), unique=True, nullable=False
    )

    def __repr__(self):
        return "Registered(name='{}', cnic={},contactNo={},gender={},DOR={},DOE={})".format(
            self.name,
            self.cnic,
            self.contactno,
            self.gender,
            self.dor,
            self.doe,
        )


# class Visitor(db.Model):
#     __tablename__ = "visitors"

#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     name = db.Column(db.String, nullable=False)
#     cnic = db.Column(db.String, nullable=False)
#     license_plate = db.Column(db.String, nullable=False) # license

#     def __repr__(self):
#         return "Visitor(name='{}', cnic={})".format(self.name, self.cnic)


class CarLogs(db.Model):
    __tablename__ = "carlogs"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    image_path = db.Column(db.String, nullable=False)
    is_registered = db.Column(db.Boolean, default=False)
    is_suspicious = db.Column(db.Boolean, default=False)
    is_visitor = db.Column(db.Boolean, default=False)
    time = db.Column(db.DateTime, nullable=False)
    license_plate = db.Column(db.String, nullable=False)
    vehicle_id = db.Column(
        db.Integer, db.ForeignKey("vehicles.id"), unique=False, nullable=True
    )

    def __repr__(self):
        return "timeStamp(image path='{}', entry time={})".format(
            self.image_path, self.time
        )


# if __name__ == "__main__":
#     db.create_all()
#     db.session.commit()
# app.run()
