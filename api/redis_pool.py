import redis

pool=redis.ConnectionPool(password=123)
REDIS_CONN=redis.Redis(connection_pool=pool)
