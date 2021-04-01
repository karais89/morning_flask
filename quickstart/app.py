from flask import Flask, escape, url_for, request, render_template, make_response, abort, jsonify
from flask import session, redirect

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/session')
def session_index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/session/login', methods=['GET', 'POST'])
def session_login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('session_index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/session/logout')
def session_logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('session_index'))


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/')
def index():
    return 'index'

# @app.route('/login')
# def login():
#     return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
# 
# def do_the_login():
#     pass
# 
# def show_the_login_form():
#     pass

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username, password):
    pass

def log_the_user_in(username):
    pass

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# cookie
@app.route('/get/cookies')
def get_cookies():
    username = request.cookies.get('username')
    return "aaa " + username
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

@app.route('/set/cookies')
def set_cookies():
    resp = make_response(render_template('hello.html', name='kaya'))
    resp.set_cookie('username', 'the username')
    return resp

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/error')
def err_test():
    abort(401)
    # this_is_never_executed()

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/u_i/<filename>")
def user_image():
    return "test1234"

class User:
    def __init__(self):
        pass

def get_current_user():
    u = User()
    u.username = "kk",
    u.theme = "dark",
    u.image = "aaa"
    return u

@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])

def get_all_users():
    return [
        {"username": "kkk"},
        {"username": "ccc"},
        {"username": "aaa"}
    ]

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
