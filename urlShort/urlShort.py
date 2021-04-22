from flask import (Blueprint, render_template, request, redirect, url_for,
                   flash, abort, session, jsonify)
import json
import os.path
import os
from werkzeug.utils import secure_filename

bp = Blueprint('urlShort', __name__)


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('home.html', codes=session.keys())


@bp.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
                session[request.form['code']] = True
        if request.form['code'] in urls:
            flash('That short name already been taken, Please select another name.')
            return redirect(url_for('urlShort.home'))

        if 'url' in request.form:
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            filepath = os.getcwd() + '/urlShort/static/user_files'
            print(filepath, os.path.exists(filepath))
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            f.save(filepath + '/' + full_name)
            urls[request.form['code']] = {'file': full_name}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        session[request.form['code']] = True
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('urlShort.home'))


@bp.route('/<string:code>')
def redirect_to_url(code):
    urls = {}
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
    if code in urls:
        if 'url' in urls[code]:
            return redirect(urls[code]['url'])
        else:
            return redirect(url_for('static', filename='user_files/'
                            + urls[code]['file']))
    return abort(404)


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))

# if __name__=='__main__':
#     bp.run(debug=True)
