from flask import Flask, render_template, request, redirect, url_for
import json
import os.path
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        if os.path.exists
        urls[request.form['code']] = {'url': request.form['url']}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))
# if __name__=='__main__':
#     app.run(debug=True)
