from sqlalchemy.dialects import postgresql
from models import metadata
from engine import engine


metadata.create_all(engine)