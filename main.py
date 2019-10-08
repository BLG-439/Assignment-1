from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
  kot="Plot"
  return render_template('index.html', kot=kot)

if __name__ == '__main__':
  app.run(debug=True)
