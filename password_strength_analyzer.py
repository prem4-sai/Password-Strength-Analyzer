print("=" * 50)
print("      PASSWORD STRENGTH ANALYZER")
print("=" * 50)

password = input("Enter your password: ")

score = 0

# Special Characters
special_characters = "!@#$%^&*()_+-={}[]|:;<>,.?/"

# -------------------- Length Check --------------------
if len(password) >= 8:
    print("✔ Password length is good")
    score += 1
else:
    print("✘ Password should be at least 8 characters")

# -------------------- Uppercase Check --------------------
if any(char.isupper() for char in password):
    print("✔ Contains Uppercase Letter")
    score += 1
else:
    print("✘ No Uppercase Letter")

# -------------------- Lowercase Check --------------------
if any(char.islower() for char in password):
    print("✔ Contains Lowercase Letter")
    score += 1
else:
    print("✘ No Lowercase Letter")

# -------------------- Number Check --------------------
if any(char.isdigit() for char in password):
    print("✔ Contains Number")
    score += 1
else:
    print("✘ No Number")

# -------------------- Special Character Check --------------------
if any(char in special_characters for char in password):
    print("✔ Contains Special Character")
    score += 1
else:
    print("✘ No Special Character")

# -------------------- Common Weak Password Check --------------------
weak_passwords = [
    "123456",
    "password",
    "password123",
    "admin",
    "qwerty",
    "abc123"
]

if password.lower() in weak_passwords:
    print("\n⚠ Warning: This is a common weak password!")
    score = 0

# -------------------- Sequential Pattern Check --------------------
weak_patterns = [
    "123",
    "1234",
    "12345",
    "abc",
    "abcd",
    "qwerty"
]

for pattern in weak_patterns:
    if pattern in password.lower():
        print(f"\n⚠ Warning: Password contains common pattern: {pattern}")
        score = max(score - 1, 0)
        break

# -------------------- Repeated Character Check --------------------
for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        print("\n⚠ Warning: Password contains repeated characters.")
        score = max(score - 1, 0)
        break

# -------------------- Decide Password Strength --------------------
if score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MEDIUM"
else:
    strength = "STRONG"

# -------------------- Analysis Summary --------------------
print("\n" + "=" * 50)
print("PASSWORD ANALYSIS SUMMARY")
print("=" * 50)

print("Password Length     :", len(password))
print("Uppercase Letter    :", "Yes" if any(char.isupper() for char in password) else "No")
print("Lowercase Letter    :", "Yes" if any(char.islower() for char in password) else "No")
print("Contains Number     :", "Yes" if any(char.isdigit() for char in password) else "No")
print("Special Character   :", "Yes" if any(char in special_characters for char in password) else "No")
print("Final Score         :", score, "/5")
print("Password Strength   :", strength)

# -------------------- Suggestions --------------------
print("\n" + "=" * 50)
print("SUGGESTIONS")
print("=" * 50)

suggestion = False

if len(password) < 8:
    print("- Use at least 8 characters.")
    suggestion = True

if not any(char.isupper() for char in password):
    print("- Add at least one uppercase letter (A-Z).")
    suggestion = True

if not any(char.islower() for char in password):
    print("- Add at least one lowercase letter (a-z).")
    suggestion = True

if not any(char.isdigit() for char in password):
    print("- Add at least one number (0-9).")
    suggestion = True

if not any(char in special_characters for char in password):
    print("- Add at least one special character (!@#$...).")
    suggestion = True

if password.lower() in weak_passwords:
    print("- Avoid using common passwords.")
    suggestion = True

if not suggestion:
    print("- Excellent! Your password is very strong.")

print("\nThank you for using Password Strength Analyzer!")
print("=" * 50)