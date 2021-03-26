# flask Quickstart

```
python -m venv venv
```

- vscode에서 python 인터프리터 설정
- vscode에서 run and debug 메뉴의 create setting.json 클릭
- pip install flask

## Github 프로젝트 칸반 사용 테스트 중
- PullRequest 부분 테스트 진행 중 (vscode에서 쉽게 사용 가능한지에 대한 부분)

시작하고 싶으신가요? 이 페이지는 Flask에 대한 좋은 소개를 제공합니다. 
Flask가 이미 설치되어 있다고 가정합니다. 그렇지 않은 경우 설치 섹션으로 이동하십시오.

github-flow 사용
- 그냥 작업마다 브랜치 생성 후 바로 master로 부어주는 형태
- 풀리퀘 생성시 resolved: #티켓번호 형태로 설명에 추가해줘야 자동 티켓 완료 처리 됨


## [A minimal Application](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

최소 Flask 애플리케이션은 위와 같습니다.

그럼 그 코드가 뭘 한 거지?
1. 먼저 *Flask* 클래스를 가져 왔습니다. 이 클래스의 인스턴스는 WSGI 응용 프로그램이됩니다. 
2. 다음으로이 클래스의 인스턴스를 만듭니다. 첫 번째 인수는 응용 프로그램의 모듈 또는 패키지 이름입니다. 단일 모듈을 사용하는 경우 (이 예에서와 같이) __name__을 사용해야합니다. 응용 프로그램으로 시작되었는지 아니면 모듈로 가져 왔는지에 따라 이름이 달라지기 때문입니다 ( '__main__'과 실제 가져 오기 이름). 이것은 Flask가 템플릿, 정적 파일 등을 찾을 위치를 알기 위해 필요합니다. 자세한 내용은 [Flask 문서](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask)를 참조하세요. 
3. 그런 다음 route () 데코레이터를 사용하여 함수를 트리거해야하는 URL을 Flask에 알립니다. 
4. 함수에는 특정 함수에 대한 URL을 생성하는데도 사용되는 이름이 주어지며 사용자의 브라우저에 표시하려는 메시지를 반환합니다. 

hello.py 또는 유사한 이름으로 저장하십시오. Flask 자체와 충돌 할 수 있으므로 응용 프로그램 flask.py를 호출하지 마십시오.

이렇게하면 매우 간단한 내장 서버가 시작됩니다. 테스트에는 충분하지만 프로덕션에서 사용하려는 것은 아닙니다. 배포 옵션은 [배포 옵션 페이지](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment)를 참조하십시오.

이제 http://127.0.0.1:5000/으로 이동하면 hello world 인사말이 표시됩니다. 

### 외부에서 볼 수 있는 서버

서버를 실행하면 네트워크의 다른 컴퓨터가 아닌 사용자 자신의 컴퓨터에서만 서버에 액세스 할 수 있습니다. 디버깅 모드에서는 애플리케이션 사용자가 컴퓨터에서 임의의 Python 코드를 실행할 수 있기 때문에 이것이 기본값입니다.

디버거를 비활성화했거나 네트워크의 사용자를 신뢰하는 경우 명령 줄에 --host = 0.0.0.0을 추가하기 만하면 서버를 공개적으로 사용할 수 있습니다.

```
$ flask run --host = 0.0.0.0
```

이렇게하면 운영 체제가 모든 공용 IP를 수신하도록 지시합니다.

참고: 실제 서버 배포시 위 옵션을 줘서 배포 진행 해야 됨. 

파이썬에서 웹 서버를 배포 하는 방법은 생각보다는 간단하지 않다. (Nginx 등의 도움이 필요) 그렇다고 엄청 복잡하는 않다.

웹 브라우저 (크롬, 파폭) -> 웹 서버 (Nginx, Apache) -> WSGI서버 (Gunicom) -> WSGI 애플리케이션 (플라스크)

> WSGI 서버는 웹 서버와 WSGI 애플리케이션 중간에 위치한다. 그래서 WSGI 서버는 WSGI 미들웨어(middleware) 또는 WSGI 컨테이너(container)라고도 한다.

## 디버그 모드

(오류 및 스택 추적 만 기록하고 싶으십니까? [애플리케이션 오류 페이지 참조](https://flask.palletsprojects.com/en/1.1.x/errorhandling/#application-errors))

flask 스크립트는 로컬 development server를 시작하는 것이 좋지만 코드를 변경할 때마다 수동으로 다시 시작해야합니다. 그것은 별로 좋지 않으며 Flask가 더 잘할 수 있습니다. 디버그 지원을 활성화하면 서버가 코드 변경시 자체적으로 다시 로드 되며 문제가 발생하면 유용한 디버거를 제공합니다.

모든 개발 기능 (디버그 모드 포함)을 활성화하려면 서버를 실행하기 전에 FLASK_ENV 환경 변수를 export 할때 `development` 변수를 세팅 할 수 있습니다.

```sh
$ export FLASK_ENV=development
$ flask run
```
- 윈도우에서는 export 명령어가 아닌 set 명령어

이것은 다음을 수행합니다.
1. 디버거를 활성화합니다.
2. 자동 리로드를 활성화합니다.
3. Flask 앱에서 디버그 모드를 활성화합니다.

FLASK_DEBUG = 1을 내보내서 환경과 별도로 디버그 모드를 제어 할 수도 있습니다.

[개발 서버 문서](https://flask.palletsprojects.com/en/1.1.x/server/#server)에 설명 된 더 많은 매개 변수가 있습니다.

주의
인터랙티브 디버거가 포크 환경에서 작동하지 않더라도 (프로덕션 서버에서 사용하는 것이 거의 불가능 함), 여전히 임의의 코드 실행을 허용합니다. 이는 주요 보안 위험을 야기하므로 프로덕션 시스템에서 사용해서는 안됩니다.

## 참조
- https://flask.palletsprojects.com/en/1.1.x/quickstart/