"""
Napisz funkcję, która zliczy ile osób ma zadany status
statuses = {
"Alice": "online",
"Bob": "offline",
"Eve": "online",
}
assert count_status(statuses, "online") == 2
assert count_status(statuses, "offline") == 1
assert count_status(statuses, "xxx") == 0
"""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def chech_online_status():
    online, offline = 0, 0
    for v in statuses.values():
        if v == "online":
            online += 1
        elif v == "offline":
            offline += 1
    return online, offline


assert chech_online_status()[0] == 2  # online
assert chech_online_status()[1] == 1  # offline
