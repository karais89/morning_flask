import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "app.db"))
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/test?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False