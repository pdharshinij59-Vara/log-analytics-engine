import json
from collections import Counter

# Sample logs
logs = [
    {"service": "auth", "user": "u101", "status": "error", "latency": 230},
    {"service": "payment", "user": "u202", "status": "success", "latency": 120},
    {"service": "auth", "user": "u101", "status": "success", "latency": 80},
    {"service": "orders", "user": "u303", "status": "error", "latency": 300}
]

# Count errors
errors = [log for log in logs if log["status"] == "error"]
print("Total Errors:", len(errors))

# Top users
users = [log["user"] for log in logs]
top_users = Counter(users)

print("Top Users:", top_users)
