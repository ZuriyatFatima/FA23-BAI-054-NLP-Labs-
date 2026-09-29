"""Lab 02 - Task 9: Nested JSON Flattening, DataFrame Operations, and Comment Analysis"""
import math

import pandas as pd
import requests

BASE = "https://jsonplaceholder.typicode.com"


def fetch(endpoint):
    response = requests.get(f"{BASE}/{endpoint}", timeout=15)
    response.raise_for_status()
    return response.json()


# (a) flatten nested users
def flatten_user(user: dict) -> dict:
    return {
        "id": user["id"],
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "city": user["address"]["city"],
        "zipcode": user["address"]["zipcode"],
        "lat": user["address"]["geo"]["lat"],
        "lng": user["address"]["geo"]["lng"],
        "company_name": user["company"]["name"],
        "company_catchphrase": user["company"]["catchPhrase"],
    }


users = fetch("users")
flat_users = [flatten_user(u) for u in users]
print("(a) Flattened users:")
for u in flat_users:
    print("   ", u)

# (b) DataFrame operations
df = pd.DataFrame(flat_users)
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", None)
print("\n(b) DataFrame:\n", df.to_string())
df["lat"] = df["lat"].astype(float)
df["lng"] = df["lng"].astype(float)
df["distance_from_origin"] = df.apply(lambda r: math.sqrt(r["lat"] ** 2 + r["lng"] ** 2), axis=1)
farthest = df.loc[df["distance_from_origin"].idxmax()]
print(f"\n    Farthest from origin: {farthest['name']} ({farthest['distance_from_origin']:.2f})")

# (c) hemispheres (lat == 0 would belong to neither group)
north = df[df["lat"] > 0]
south = df[df["lat"] < 0]
print("\n(c) Northern Hemisphere:", list(north["name"]))
print("    Southern Hemisphere:", list(south["name"]))
avg_n = north["distance_from_origin"].mean() if not north.empty else float("nan")
avg_s = south["distance_from_origin"].mean() if not south.empty else float("nan")
print(f"    Avg distance - North: {avg_n:.2f} | South: {avg_s:.2f}")
print("    Higher average distance:", "Northern" if avg_n > avg_s else "Southern", "Hemisphere")

# (d) comment counts per post
posts = fetch("posts")
comments = fetch("comments")
counts = {p["id"]: 0 for p in posts}
for c in comments:
    if c["postId"] in counts:
        counts[c["postId"]] += 1
ranked = sorted(((p["id"], p["title"][:40], counts[p["id"]]) for p in posts),
                key=lambda t: t[2], reverse=True)
print("\n(d) Top 5 most-commented posts:")
for row in ranked[:5]:
    print("   ", row)
print("    Bottom 5 least-commented posts:")
for row in ranked[-5:]:
    print("   ", row)
