marks: dict[str, int] = {
    "Math": 80,
    "Science": 82,
    "History": 78,
    "English": 35,
    "Python": 98,
    "Physics": 63,
}
print(f"Marks: {marks}")

for subject in marks.keys():
    print(subject)

for score in marks.values():
    print(score)

for subject, score in marks.items():
    print(f"{subject}: {score}/100")

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject}: PASS")
    else:
        print(f"{subject}: FAILED!!!")

marks["English"] = 70
print(f"Louis scored {marks['English']} in English.")

marks["Geography"] = 78

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject}: PASS")
    else:
        print(f"{subject}: FAILED!!!")

python_score = marks["Python"]
print(f"Louis scored {python_score} in Python")

python_score = marks.get("Python")
print(f"Louis scored {python_score} in Python")

java_score: int | None = marks.get("Java")

if java_score is None:
    print("Louis did not study Java")
else:
    print(f"Louis scored {java_score} in java")

del marks["English"]

print(f"Marks: {marks}")
