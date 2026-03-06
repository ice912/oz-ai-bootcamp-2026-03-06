#print("Hello worker")
import redis

redis_client = redis.from_url("redis://redis:6379", decode_response=True)

def run():
    pass

if __name__ == "__main__":
    run()