import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # instance_relative_config = True는 구성 파일이 인스턴스 폴더에 상대적임을 앱에 알려줍니다.
    # 인스턴스 폴더는 flaskr 패키지 외부에 있으며 구성 비밀 및 데이터베이스 파일과 같이 버전 제어에 커밋하면 안되는 로컬 데이터를 저장할 수 있습니다. (gitignore에서 instance 폴더를 추가 한 상태)
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping ()은 앱에서 사용할 기본 구성을 설정합니다.
    # SECRET_KEY는 Flask 및 확장 프로그램에서 데이터를 안전하게 유지하는 데 사용됩니다.
    # 개발 중에 편리한 값을 제공하기 위해 'dev'로 설정되어 있지만 배포시 임의의 값으로 재정의해야합니다.
    # DATABASE는 SQLite 데이터베이스 파일이 저장 될 경로입니다.
    # 이는 Flask가 인스턴스 폴더에 대해 선택한 경로 인 app.instance_path 아래에 있습니다.
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # app.config.from_pyfile ()은 인스턴스 폴더의 config.py 파일에서 가져온 값으로 기본 구성을 재정의합니다.
        # 예를 들어 배포 할 때 실제 SECRET_KEY를 설정하는 데 사용할 수 있습니다.
        # test_config는 공장으로 전달 될 수도 있으며 인스턴스 구성 대신 사용됩니다.
        # 이렇게하면 가이드의 뒷부분에서 작성할 테스트를 구성한 개발 값과 독립적으로 구성 할 수 있습니다.
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

    from . import db
    db.init_app(app)

    # app.register_blueprint()를 사용하여 블루프린트를 가져오고 등록합니다. 
    from . import auth
    app.register_blueprint(auth.bp)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
