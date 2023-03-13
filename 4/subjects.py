
subjects: tuple[str, str, str] = ("Math", "Science", "History")

print(f"No. of subjects: {len(subjects)}")

for subject in subjects:
    print(f"Louis is signing up for: {subject}")

print(subjects[1])

addl_subjects = ("English", "Python", "Physics")
total_subjects = subjects + addl_subjects
print(f"All subjects: {total_subjects}")

if "Python" in total_subjects:
    print("Yayy, Louis is going to learn Python!!")
else:
    print("Oh ho, no Python for Louis")
