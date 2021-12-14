import redis


red = redis.Redis(
    host = 'redis-16799.c278.us-east-1-4.ec2.cloud.redislabs.com',
    port = 16799,
    password = 'LWuhL746W5fUaQdRQgPVyMpWHidyh4ua'
)

red.set('var1', 'value1')  # записываем в кэш строку "value1"
print(red.get('var1'))  # считываем из кэша данные

