from flask import Flask, redirect, render_template

app = Flask(__name__)


counts = 0


@app.route('/')
def route_main():
    return render_template("index.html", counts=counts)


@app.route('/request-counter')
def route_counter():
    global counts
    counts += 1
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = "something"
    app.run(debug=True, port=5000)
