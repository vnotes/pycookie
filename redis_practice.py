import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
rdb = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    pass
