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

## 서버가 시작 되지 않는 경우해야 할 일

python -m flask가 실패하거나 flask가 없는 경우 여러 가지 이유가 있을 수 있습니다. 우선 오류 메시지를 확인해야합니다.

### 이전 버전의 플라스크

0.11보다 오래된 Flask 버전은 응용 프로그램을 시작하는 다른 방법을 사용했습니다. 간단히 말해, flask 명령은 존재하지 않았고 python -m flask도 없었습니다. 이 경우 두 가지 옵션이 있습니다. 새로운 Flask 버전으로 업그레이드하거나 개발 서버 문서를 살펴보고 서버를 실행하는 대체 방법을 확인하세요.

### 잘못된 가져 오기 이름

`FLASK_APP` 환경 변수는 플라스크 실행시 가져올 모듈의 이름입니다. 모듈 이름이 잘못 지정된 경우 시작시 가져 오기 오류가 발생합니다 (또는 응용 프로그램으로 이동할 때 디버그가 활성화 된 경우). 가져 오려고 시도한 내용과 실패한 이유를 알려줍니다.

가장 일반적인 이유는 오타이거나 실제로 `app` 객체를 만들지 않았기 때문입니다.

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

## 라우팅

최신 웹 애플리케이션은 사용자를 돕기 위해 의미있는 URL을 사용합니다. 사용자는 페이지를 좋아하고 페이지가 기억하고 페이지를 직접 방문하는 데 사용할 수있는 의미있는 URL을 사용하는 경우 다시 방문 할 가능성이 높습니다.

route() 데코레이터를 사용하여 함수를 URL에 바인딩합니다.

```py
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

더 많은 것을 할 수 있습니다! URL의 일부를 동적으로 만들고 함수에 여러 규칙을 연결할 수 있습니다.

### 변수 규칙

<variable_name>으로 섹션을 표시하여 URL에 변수 섹션을 추가 할 수 있습니다. 그런 다음 함수는 <variable_name>을 키워드 인수로받습니다. 
선택적으로 변환기를 사용하여 <converter : variable_name>과 같은 인수 유형을 지정할 수 있습니다.

```py
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
```

변환 타입
- string : (기본값) 슬래시가없는 모든 텍스트를 허용합니다.
- int : 양의 정수를 허용합니다.
- float : 양의 부동 소수점 값을 허용합니다.
- path : 문자열과 비슷하지만 슬래시도 허용합니다.
- uuid : UUID 문자열 허용

### 고유 URL / 리다이렉션 동작

다음 두 가지 규칙은 후행 슬래시 사용이 다릅니다.

```py
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

프로젝트 엔드 포인트의 표준 URL에는 후행 슬래시가 있습니다. 파일 시스템의 폴더와 비슷합니다. 후행 슬래시 없이 URL에 액세스하는 경우 Flask는 후행 슬래시가있는 표준 URL로 리디렉션합니다.

about 엔드 포인트의 표준 URL에는 후행 슬래시가 없습니다. 파일의 경로 이름과 비슷합니다. 후행 슬래시가 있는 URL에 액세스 하면 404 "찾을 수 없음" 오류가 발생합니다. 이렇게하면 이러한 리소스에 대해 URL을 고유하게 유지하여 검색 엔진이 동일한 페이지를 두 번 색인하는 것을 방지 할 수 있습니다.

후행 슬래시를 URL 끝에 붙이는 것은 해당 URL 리소스가 디렉토리(directory)임을 의미합니다. 이를 붙이지 않은 것은 해당 URL 리소스가 파일(file)임을 의미하죠.

### URL Building

특정 함수에 대한 URL을 작성하려면 `url_for()` 함수를 사용하십시오. 함수 이름을 첫 번째 인수로 받아들이고 각각 URL 규칙의 변수 부분에 해당하는 여러 키워드 인수를받습니다. 알 수없는 변수 부분이 쿼리 매개 변수로 URL에 추가됩니다.

URL을 템플릿에 하드 코딩하는 대신 URL 반전 함수 url_for ()를 사용하여 URL을 빌드하려는 이유는 무엇입니까?

1. 반전은 종종 URL을 하드 코딩하는 것보다 더 설명 적입니다.
2. 하드 코딩 된 URL을 수동으로 변경하는 것을 기억할 필요없이 한 번에 URL을 변경할 수 있습니다.
3. URL 구축은 특수 문자 및 유니 코드 데이터의 이스케이프를 투명하게 처리합니다.
4. 생성 된 경로는 항상 절대적이므로 브라우저에서 상대 경로의 예기치 않은 동작을 방지합니다. 애플리케이션이 URL 루트 외부에있는 경우 (예 : / 대신 / myapplication에) url_for ()가이를 적절하게 처리합니다.

예를 들어, 여기에서는 test_request_context() 메서드를 사용하여 url_for()를 시도합니다. test_request_context()는 Flask에게 Python 셸을 사용하는 동안에도 요청을 처리하는 것처럼 동작하도록 지시합니다. [컨텍스트 로컬](https://flask.palletsprojects.com/en/1.1.x/quickstart/#context-locals)을 참조하십시오.

```py
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```
/
/login
/login?next=/
/user/John%20Doe
```

### HTTP 메서드

웹 응용 프로그램은 URL에 액세스 할 때 다른 HTTP Methods를 사용합니다. Flask로 작업 할 때 HTTP Methods에 익숙해 져야합니다. 기본적으로 경로는 GET 요청에만 응답합니다. route() 데코레이터의 methods 인수를 사용하여 다른 HTTP Methods를 처리 할 수 있습니다.

```py
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

GET이 있는 경우 Flask는 HEAD 메서드에 대한 지원을 자동으로 추가하고 HTTP RFC에 따라 HEAD 요청을 처리합니다. 마찬가지로 OPTIONS가 자동으로 구현됩니다.

## 정적 파일

동적 웹 애플리케이션에는 정적 파일도 필요합니다. 일반적으로 CSS 및 JavaScript 파일의 출처입니다. 이상적으로는 웹 서버가 사용자를 위해 웹 서버를 구성하지만, 개발 중에 Flask도 이 작업을 수행할 수 있습니다. 패키지 또는 모듈 옆에 static이라는 폴더를 생성하면 애플리케이션의 / static에서 사용할 수 있습니다.

정적 파일에 대한 URL을 생성하려면 특수한 '정적'엔드 포인트 이름을 사용하십시오.

```py
url_for('static', filename = 'style.css')
```

파일은 `static/style.css`로 파일 시스템에 저장되어야합니다.

[역주]
- 해당 부분은 개발 용도에서는 자동으로 static 폴더에 접근을 하는 것 같고, ngix등으로 배포시 해당 경로로 지정해주는 부분으로 보인다.
- https://stackoverflow.com/questions/31682179/how-to-serve-flask-static-files-using-nginx


## 참조
- https://flask.palletsprojects.com/en/1.1.x/quickstart/