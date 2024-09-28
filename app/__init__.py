import os

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.config import config_
from app import config_swag, db
from app.logger import setup_logging
from flasgger import Swagger


'''
Endpoints:
/all
/name/<name>
/date/<date>
/day/<day>
/week/<week>
/month/<month>
'''


# Create app
app = Flask(__name__)
app.config.from_object(config_)
app.config.from_mapping(DATABASE=os.path.join(app.instance_path, config_.DBFILE))

# Make db instance dir
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Init db
db.init_app(app)

# Init swagger (docs)
swagger = Swagger(app, template=config_swag.swagger_conf)

# setup logging
setup_logging(app)

# sett rate limiter (max 60 requests per minute)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["60 per minute"]
)

# Import routes
from app import routes
