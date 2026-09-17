from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Invoice & Billing Management System</h1>
    <p>Application is under development.</p>
    <p>Billing and invoice modules coming soon.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
