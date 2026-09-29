"""Lab 02 - Task 8: To-Do Completion Rate Analysis Across Users"""
import sys
import requests

TODOS_URL = "https://jsonplaceholder.typicode.com/todos"
USERS_URL = "https://jsonplaceholder.typicode.com/users"

# (a) fetch + validate
try:
    response = requests.get(TODOS_URL, timeout=15)
except requests.RequestException as err:
    sys.exit(f"Error: could not reach {TODOS_URL}: {err}")
if response.status_code != 200:
    sys.exit(f"Error: expected status 200 but got {response.status_code}")
todos = response.json()
if not isinstance(todos, list):
    sys.exit("Error: the parsed response is not a list")
if len(todos) < 1:
    sys.exit("Error: the list contains no records")
print("(a) Total todo records retrieved:", len(todos))

# (b) group by userId
stats = {}
for todo in todos:
    s = stats.setdefault(todo["userId"], {"total": 0, "completed": 0, "incomplete": 0})
    s["total"] += 1
    s["completed" if todo["completed"] else "incomplete"] += 1
print("\n(b) Per-user statistics:")
for uid in sorted(stats):
    s = stats[uid]
    print(f"    User {uid}: {s}  completed + incomplete == total -> "
          f"{s['completed'] + s['incomplete'] == s['total']}")

# (c) completion rates
rates = {uid: round(s["completed"] / s["total"] * 100, 1) for uid, s in stats.items()}
best = max(rates, key=rates.get)
worst = min(rates, key=rates.get)
print(f"\n(c-i)   Highest completion rate: user {best} ({rates[best]}%)")
print(f"(c-ii)  Lowest completion rate : user {worst} ({rates[worst]}%)")
print(f"(c-iii) Average completion rate: {round(sum(rates.values()) / len(rates), 1)}%")

# (d) table with user names
users_resp = requests.get(USERS_URL, timeout=15)
if users_resp.status_code != 200:
    sys.exit(f"Error: users request failed with status {users_resp.status_code}")
lookup = {u["id"]: u["name"] for u in users_resp.json()}

print("\n(d) Completion ranking:")
header = f"{'Rank':<6}{'Name':<26}{'Total Tasks':<14}{'Completed':<12}{'Completion Rate %':<18}"
print(header)
print("-" * len(header))
for rank, uid in enumerate(sorted(rates, key=rates.get, reverse=True), start=1):
    s = stats[uid]
    print(f"{rank:<6}{lookup.get(uid, 'Unknown'):<26}{s['total']:<14}{s['completed']:<12}{rates[uid]:<18}")
