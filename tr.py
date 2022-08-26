from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return """<html><head><title>Hi</title></head>
    <body>
    <form><select name='drp'><option value='f'>First</option>
    <option value='s'>Second</option>
    </select>
    <button type=submit>Submit</button>
    </form>
    </body>
    </html>"""