import os
import redis
import time

def handle(event, context):
    r = redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=6379,
        db=0,
        password=os.getenv("REDIS_PASSWORD")
    )
    key = str(int(time.time()))
    r.set(key, event.body)
    return "Feedback saved"
