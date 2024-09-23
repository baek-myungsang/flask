from flask import Flask
import random

app = Flask(__name__)

topics = [
    {
        'id': 1,
        'title': 'html',
        'body': 'html is ...'
    },
    {
        'id': 2,
        'title': 'css',
        'body': 'css is ...'
    },
    {
        'id': 3,
        'title': 'js',
        'body': 'js is ...'
    }

]


@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + \
            f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''<doctype html>
<html>
    <body>
    <h1><a href="/">Web</a></h1>
    <ol>
        {liTags}
    </ol>
    <h2>Welcome</h2>
    <p>hello, web</p>
    </body>
</html>
'''

#  리턴값은 기본적으로 문자열


@app.route('/create/')
def create():
    return 'Create'


@app.route('/read/<id>/')
def read(id):
    print(id)
    liTags = ''
    for topic in topics:
        liTags = liTags + \
            f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    for topic in topics:

        return f'''<doctype html>
  <html>
      <body>
      <h1><a href="/">Web</a></h1>
      <ol>
          {liTags}
      </ol>
      <h2>Welcome</h2>
      <p>hello, web</p>
      </body>
  </html>
  '''


app.run(port=5001, debug=True)
