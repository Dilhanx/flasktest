from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Kappa'

@app.route('/test')
def test():

  return 'test'
@app.route('/test/<test>')
def testtest(test):

  return test

if __name__ == '__main__':  
  app.run()
