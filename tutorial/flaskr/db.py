import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_app(app):
    # app.teardown_appcontext()는 응답을 반환 한 후 정리할 때 해당 함수를 호출하도록 Flask에 지시합니다.
    app.teardown_appcontext(close_db)
    # app.cli.add_command ()는 flask 명령으로 호출 할 수 있는 새 명령을 추가합니다.
    app.cli.add_command(init_db_command)


def init_db():
    # get_db는 파일에서 읽은 명령을 실행하는 데 사용되는 데이터베이스 연결을 반환합니다.
    db = get_db()

    # open_resource ()는 flaskr 패키지와 관련된 파일을 엽니다.
    # 이는 나중에 애플리케이션을 배포 할 때 해당 위치가 어디에 있는지 알 필요가 없기 때문에 유용합니다.
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


# click.command()는 init_db 함수를 호출하고 사용자에게 성공 메시지를 표시하는 init-db라는 명령 줄 명령을 정의합니다.
# 명령 작성에 대한 자세한 내용은 명령 줄 인터페이스를 참조하십시오.
@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def get_db():
    if "db" not in g:
        # sqlite3.connect()는 DATABASE 구성 키가 가리키는 파일에 대한 연결을 설정합니다.
        # 이 파일은 아직 존재하지 않아도 되며 나중에 데이터베이스를 초기화 해야합니다.
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row는 연결이 dict처럼 작동하는 행을 반환하도록 지시합니다.
        # 이렇게하면 이름으로 열에 액세스 할 수 있습니다.
        g.db.row_factory = sqlite3.Row

    return g.db


# close_db는 g.db가 설정되었는지 확인하여 연결이 생성되었는지 확인합니다. 연결이 있으면 닫힙니다.
# 더 내려 가면 각 요청 후에 호출되도록 애플리케이션 팩토리의 close_db 함수에 대해 애플리케이션에 알려줍니다.
def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()