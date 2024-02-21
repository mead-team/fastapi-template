from redis import Redis

from app.core.setting import settings


REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PORT
REDIS_DATABASE = settings.REDIS_DATABASE
redis_config = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE)