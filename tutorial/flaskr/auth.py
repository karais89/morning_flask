import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# 'auth'라는 블루 프린트가 생성됩니다.
# 애플리케이션 객체와 마찬가지로 블루 프린트는 정의 된 위치를 알아야 하므로 __name__이 두 번째 인수로 전달됩니다.
# url_prefix는 Blueprint와 관련된 모든 URL 앞에 추가됩니다.
bp = Blueprint("auth", __name__, url_prefix="/auth")


# @bp.before_app_request 애너테이션 사용. 이 애너테이션이 적용된 함수는 라우트 함수보다 먼저 실행된다.
# 즉, 앞으로 load_logged_in_user 함수는 모든 라우트 함수보다 먼저 실행될 것이다.
# bp.before_app_request()는 요청 된 URL에 관계 없이 view 함수 이전에 실행되는 함수를 등록합니다.
# load_logged_in_user는 사용자 ID가 세션에 저장되어 있는지 확인하고 데이터베이스에서 해당 사용자의 데이터를 가져 와서 요청 기간 동안 지속되는 g.user에 저장합니다.
# 사용자 ID가 없거나 ID가 없는 경우 g.user는 None이됩니다.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


# @bp.route는 URL/register를 register 함수와 연결합니다.
# Flask가 /auth/register에 대한 요청을 받으면 register 뷰를 호출하고 반환 값을 응답으로 사용합니다.
@bp.route("/register", methods=("GET", "POST"))
def register():
    # 사용자가 양식을 제출 한 경우 request.method는 'POST'가됩니다. 이 경우 입력 유효성 검사를 시작하십시오.
    if request.method == "POST":
        # request.form은 제출 된 양식 키 및 값을 매핑하는 특수한 유형의 dict입니다. 사용자는 사용자 이름과 비밀번호를 입력합니다.
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        # 사용자 이름과 암호가 비어 있지 않은지 확인하십시오.
        # 데이터베이스를 쿼리하고 결과가 반환되는지 확인하여 사용자 이름이 아직 등록되지 않았는지 확인합니다.
        # db.execute는 ? 사용자 입력을위한 자리 표시 자 및 자리 표시자를 대체 할 값의 튜플. 데이터베이스 라이브러리는 값을 이스케이프 처리하므로 SQL 인젝션 공격에 취약하지 않습니다.
        # fetchone ()은 쿼리에서 한 행을 반환합니다. 쿼리가 결과를 반환하지 않으면 없음을 반환합니다. 나중에 모든 결과 목록을 반환하는 fetchall ()이 사용됩니다.
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif (
            db.execute("SELECT id FROM user WHERE username = ?", (username,)).fetchone
            is not None
        ):
            error = "User {} is already registered".format(username)

        # 유효성 검사가 성공하면 새 사용자 데이터를 데이터베이스에 삽입합니다.
        # 보안을 위해 암호를 데이터베이스에 직접 저장해서는 안됩니다. 대신 generate_password_hash()를 사용하여 암호를 안전하게 해시하고 해당 해시를 저장합니다.
        # 이 쿼리는 데이터를 수정하므로 변경 사항을 저장하려면 나중에 db.commit()을 호출해야합니다.
        if error is None:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
            # 사용자를 저장하면 로그인 페이지로 리디렉션됩니다.
            # url_for()는 이름을 기반으로 로그인 뷰의 URL을 생성합니다.
            # 링크하는 모든 코드를 변경하지 않고 나중에 URL을 변경할 수 있으므로 URL을 직접 작성하는 것보다 선호됩니다.
            # redirect()는 생성 된 URL에 대한 리디렉션 응답을 생성합니다.
            return redirect(url_for("auth.login"))

        # 유효성 검사에 실패하면 오류가 사용자에게 표시됩니다. flash()는 템플릿을 렌더링 할 때 검색 할 수 있는 메시지를 저장합니다.
        flash(error)

    # 사용자가 처음에 auth/register으로 이동하거나 유효성 검사 오류가 발생한 경우 등록 양식이있는 HTML 페이지가 표시 되어야 합니다.
    # render_template()은 HTML이 포함 된 템플릿을 렌더링합니다.
    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        # check_password_hash()는 저장된 해시와 동일한 방식으로 제출 된 비밀번호를 해시하고 안전하게 비교합니다. 일치하면 암호가 유효합니다.
        if user is None:
            error = "Incorrect username"
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password"

        # 세션은 요청 전반에 걸쳐 데이터를 저장하는 사전입니다. 유효성 검사가 성공하면 사용자의 ID가 새 세션에 저장됩니다.
        # 데이터는 브라우저로 전송되는 쿠키에 저장되고 브라우저는 후속 요청과 함께 이를 다시 전송합니다.
        # Flask는 데이터가 변조되지 않도록 안전하게 서명합니다.
        # 이제 사용자 ID가 세션에 저장되었으므로 후속 요청에서 사용할 수 있습니다.
        # 각 요청을 시작할 때 사용자가 로그인 한 경우 정보가 로드되고 다른보기에서 사용할 수 있어야 합니다.
        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("indx"))


# 이 데코레이터는 적용된 원래 뷰를 래핑하는 새 뷰 함수를 반환 합니다. 
# 새 함수는 사용자가 로드 되었는지 확인하고 그렇지 않으면 로그인 페이지로 리디렉션합니다. 
# 사용자가 로드되면 원래 뷰가 호출되고 정상적으로 계속됩니다. 블로그 뷰를 작성할 때 이 데코레이터를 사용합니다.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view