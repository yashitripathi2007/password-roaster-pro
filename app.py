from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# ------------------ Utilities ------------------

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))


def analyze_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    return score


# ------------------ Roast Messages ------------------

roasts = {
    "savage": [
        "Bro this password is fighting for its life 💀",
        "Hackers are already inside 😭",
        "This password needs therapy."
    ],
    "funny": [
        "Not great, not terrible… like instant noodles 🍜",
        "I've seen worse, but still yikes 😬",
        "Okay-ish but don’t get comfy."
    ],
    "polite": [
        "This password could be improved 😊",
        "You’re on the right track!",
        "Nice choice, just a bit more complexity."
    ]
}

# ------------------ Routes ------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()

    password = data.get("password", "")
    style = data.get("style", "funny")

    # Handle empty password
    if not password:
        return jsonify({
            "score": 0,
            "roast": "Bestie… you didn’t even type a password 😭",
            "suggestion": generate_password()
        })

    score = analyze_password(password)
    roast = random.choice(roasts.get(style, roasts["funny"]))
    suggestion = generate_password()

    return jsonify({
        "score": score,
        "roast": roast,
        "suggestion": suggestion
    })


# ------------------ Run Server ------------------

if __name__ == "__main__":
    app.run(debug=True)
