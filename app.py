from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')


database = {
  'GeeksForGeeks': '123',
  'Abdul Kalam': 'xyz',
  'Jony': 'abc',
  'Tony': 'pqr'
}


@app.route('/form_login', methods=['POST', 'GET'])
def home():
  uname = request.form['username']
  password = request.form['password']
  if uname not in database:
    return render_template('home.html', info='Invalid User ????!')
  else:
    if database[uname] != password:
      return render_template('home.html', info='Invalid Password ????!')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
