from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/test')
def test():

  return 'test'
@app.route('/test/<test>')
def testtest(test):

  return test

if __name__ == '__main__':
  app.run()
