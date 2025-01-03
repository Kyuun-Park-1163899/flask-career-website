from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title':'Data Analyst',
    'location':'Seoul, Korea',
    'salary':'$2000'
  },
  {
    'id': 2,
    'title':'Data Scientist',
    'location':'Busan, Korea',
  },
  {
    'id': 3,
    'title':'Web Developer',
    'location':'Christchurch, New Zealand',
    'salary':'$4000'
  },
  {
    'id': 4,
    'title':'IT Manager',
    'location':'Auckland, New Zealand',
    'salary':'$5000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)