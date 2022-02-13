import string
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def main():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    session1 = session["counter"]
    return  render_template("index.html", session1 = session1)

@app.route('/destroy_session')
def delete():
    session.pop('counter')

    return  redirect("/")

@app.route('/plus2', methods=['POST'])
def plus2():
    session['counter'] = session['counter'] + 1
    return  redirect("/")

@app.route('/userplus', methods=['POST'])
def user():
    user = request.form['text']
    if user == '':
        session['counter'] = session['counter'] - 1
    else:
        session['counter'] = session['counter'] + int(user) - 1
    return  redirect("/")


if __name__=="__main__":
    app.run(debug=True)

