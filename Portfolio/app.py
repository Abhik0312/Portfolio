from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Email setup (use Mailtrap or Gmail SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("project.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject=f"New message from {name}",
                      sender=email,
                      recipients=["sarkarabhik86@gmail.com"],
                      body=message)
        mail.send(msg)
        flash("Message sent successfully!")
        return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
