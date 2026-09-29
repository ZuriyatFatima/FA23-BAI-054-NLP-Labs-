"""Lab 02 - Task 7: Multi-Endpoint API Data Joining and Analysis"""
import json
import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch(url):
    response = requests.get(url, timeout=15)
    if response.status_code != 200:
        raise ConnectionError(f"Request to {url} failed with status code {response.status_code}")
    return response.json()


# (a) fetch + validate
users = fetch(USERS_URL)
posts = fetch(POSTS_URL)
print(f"(a) Fetched {len(users)} users and {len(posts)} posts (both status 200).")

# (b) join users.id <-> posts.userId
joined = {}
for user in users:
    user_posts = [p["title"] for p in posts if p["userId"] == user["id"]]
    joined[user["name"]] = {"email": user["email"],
                            "post_count": len(user_posts),
                            "titles": user_posts}
print("\n(b) First 3 users:")
print(json.dumps(dict(list(joined.items())[:3]), indent=2))

# (c) user with the most posts (ties: the first user reaching the maximum is shown)
top_name = max(joined, key=lambda n: joined[n]["post_count"])
top_user = next(u for u in users if u["name"] == top_name)
print("\n(c) User with the most posts:")
print("    (i)   Name   :", top_name)
print("    (ii)  Email  :", top_user["email"])
print("    (iii) Company:", top_user["company"]["name"])
print("    (iv)  Post titles:")
for i, title in enumerate(joined[top_name]["titles"], start=1):
    print(f"          {i}. {title}")

# (d) filter users
print("\n(d) Users with 'synergies' in company.bs OR city longer than 8 characters:")
for user in users:
    has_synergies = "synergies" in user["company"]["bs"].lower()
    long_city = len(user["address"]["city"]) > 8
    if has_synergies or long_city:
        print(f"    {user['name']:25} {user['address']['city']:18} posts: {joined[user['name']]['post_count']}")
