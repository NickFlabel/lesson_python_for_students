import redis

r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

r.set("my_key", "my_val")

val = r.get("my_key")
print(val)
