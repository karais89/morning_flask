import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # instance_relative_config = True는 구성 파일이 인스턴스 폴더에 상대적임을 앱에 알려줍니다.
    # 인스턴스 폴더는 flaskr 패키지 외부에 있으며 구성 비밀 및 데이터베이스 파일과 같이 버전 제어에 커밋하면 안되는 로컬 데이터를 저장할 수 있습니다. (gitignore에서 instance 폴더를 추가 한 상태)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
