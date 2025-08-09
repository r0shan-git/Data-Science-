from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name="Jack"
    language = "Python"
    luckynos=[2,13,4,5,6,7,8,9,10]
    footer="</p> Copyright 2025, Jack's Flask App</p>"
    return render_template('index.html', name=name,lang=language,lucky=luckynos,footer=footer)

app.run(debug=True)