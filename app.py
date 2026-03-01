from flask import Flask, jsonify, request, render_template

app = Flask(__name__, 
            static_folder="static",
            template_folder="templates")

# -------------------------
# Login Page
# -------------------------
@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")


# -------------------------
# Signup Page
# -------------------------
@app.route("/signup", methods=["GET"])
def signup_page():
    return render_template("signup.html")


# -------------------------
# Create User (Form Submit)
# -------------------------
@app.route("/api/user", methods=["POST"])
def create_user():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    return jsonify({
        "status": "User received",
        "username": username,
        "email": email,
        "password": password
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)