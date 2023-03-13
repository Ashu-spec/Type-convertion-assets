friends: list[str] = ["Cece", "Roko", "Chiko", "Niko"]

print(f"Friends: {friends}")

for friend in friends:
    print(f"Zola {friend}!")

print(f"Friends Count: {len(friends)}")

unfriend = friends.pop()
print(f"Unfriend: {unfriend}")
print(f"Friends: {friends}")

friends.append("Ziko")
print(f"Friends: {friends}")

print(friends[2])

friends.remove("Roko")
print(f"Friends: {friends}")

friends.insert(1, "Roko")
print(f"Friends: {friends}")

if "Roko" in friends:
    print("Yay, Roko is in the friend list")
else:
    print("Oh no, Roko is not your friend")

friends.insert(0, "Niko")
print(f"Friends: {friends}")

friends.sort()
print(f"Friends: {friends}")

friends.reverse()
print(f"Friends: {friends}")

unfriend = friends.pop(2)
print(f"Unfriend: {unfriend}")
print(f"Friends: {friends}")
