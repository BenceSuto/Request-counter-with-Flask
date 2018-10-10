from flask import Flask, redirect

app = Flask(__name__)

counts = 0


@app.route('/request-counter')
def route_counter():
    counts += 1
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = "something"
    app.run(debug=True, port=5000)