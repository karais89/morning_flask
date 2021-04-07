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


## 렌더링 템플릿

Python 내에서 HTML을 생성하는 것은 재미가 없으며 실제로는 애플리케이션 보안을 유지하기 위해 HTML 이스케이프를 직접 수행해야하기 때문에 매우 번거 롭습니다. 그 때문에 Flask는 자동으로 [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) 템플릿 엔진을 구성합니다.

템플릿을 렌더링하려면 `render_template()` 메서드를 사용할 수 있습니다. 여러분이해야 할 일은 템플릿의 이름과 템플릿 엔진에 키워드 인자로 전달할 변수를 제공하는 것뿐입니다. 다음은 템플릿을 렌더링하는 방법에 대한 간단한 예입니다.

```py
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Flask는 templates 폴더에서 템플릿을 찾습니다. 따라서 애플리케이션이 module인 경우 이 폴더는 해당 모듈 옆에 있고, 패키지 인 경우 실제로 패키지 내부에 있습니다

```
Case 1: a module:
/application.py
/templates
    /hello.html

Case 2: a package:
/application
    /__init__.py
    /templates
        /hello.html
```

템플릿의 경우 Jinja2 템플릿의 모든 기능을 사용할 수 있습니다. 자세한 내용은 공식 [Jinja2 템플릿 문서](https://jinja.palletsprojects.com/en/2.11.x/templates/)를 참조하세요.

템플릿 예제입니다.
```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

템플릿 내에서 요청, 세션 및 g 객체와 `get_flashed_messages()` 함수에 액세스 할 수도 있습니다.

상속이 사용되는 경우 템플릿이 특히 유용합니다. 작동 방식을 알고 싶다면 [템플릿 상속 패턴 문서](https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/#template-inheritance)를 참조하십시오. 기본적으로 템플릿 상속을 통해 각 페이지의 특정 요소 (예 : 머리글, 탐색 및 바닥 글)를 유지할 수 있습니다.

자동 이스케이프가 활성화되어 있으므로 이름에 HTML이 포함되어 있으면 자동으로 이스케이프됩니다. 변수를 신뢰할 수 있고 그것이 안전한 HTML이라는 것을 알고 있다면 (예를 들어 위키 마크 업을 HTML로 변환하는 모듈에서 왔기 때문에) Markup 클래스를 사용하거나 | 안전 필터를 사용하여 안전하다고 표시 할 수 있습니다. 템플릿. 더 많은 예제를 보려면 Jinja 2 문서로 이동하십시오.

다음은 Markup 클래스의 작동 방식에 대한 기본 소개입니다.

```
>>> from markupsafe import Markup
>>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
>>> Markup.escape('<blink>hacker</blink>')
Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
>>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
```

## Accessing Request Data

웹 애플리케이션의 경우 클라이언트가 서버로 보내는 데이터에 반응하는 것이 중요합니다. 
Flask에서 이 정보는 전역 요청 객체에 의해 제공됩니다. Python에 대한 경험이 있다면 해당 객체가 전역이 될 수 있는 방법과 Flask가 여전히 스레드 안전을 유지하도록 관리하는 방법이 궁금 할 것입니다. 대답은 컨텍스트 로컬입니다.

### 컨테스트 로컬

작동 방식과 컨텍스트 로컬로 테스트를 구현하는 방법을 이해하려면 이 섹션을 읽고 그렇지 않으면 건너 뛰십시오.

Flask의 특정 개체는 전역 개체이지만 일반적인 종류는 아닙니다. 이러한 개체는 실제로 특정 컨텍스트에 로컬 인 개체에 대한 프록시입니다. 한입. 그러나 그것은 실제로 이해하기 매우 쉽습니다.

컨텍스트가 처리 스레드라고 상상해보십시오. 요청이 들어오고 웹 서버가 새 스레드를 생성하기로 결정합니다 (또는 다른 항목, 기본 개체가 스레드 이외의 동시성 시스템을 처리 할 수 있음). Flask가 내부 요청 처리를 시작하면 현재 스레드가 활성 컨텍스트임을 파악하고 현재 애플리케이션과 WSGI 환경을 해당 컨텍스트 (스레드)에 바인딩합니다. 한 응용 프로그램이 중단없이 다른 응용 프로그램을 호출 할 수 있도록 지능적인 방식으로 이를 수행합니다.

이것은 당신에게 무엇을 의미합니까? 기본적으로 단위 테스트와 같은 작업을 수행하지 않는 한 이것이 사실임을 완전히 무시할 수 있습니다. 요청 객체가 없기 때문에 요청 객체에 의존하는 코드가 갑자기 중단되는 것을 알 수 있습니다. 해결책은 요청 객체를 직접 만들고 컨텍스트에 바인딩하는 것입니다. 단위 테스트를 위한 가장 쉬운 솔루션은 test_request_context() 컨텍스트 관리자를 사용하는 것입니다. with 문과 함께 테스트 요청을 바인딩하여 상호 작용할 수 있습니다. 다음은 그 예입니다.

```python
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
The other possibility is passing a whole WSGI environment to the request_context() method:

from flask import request

with app.request_context(environ):
    assert request.method == 'POST'
```

우선 컨텍스트 객체라는 것을 유닛 테스트를 하지 않는 한 자세히 알 필요는 없고, 플라스크는 컨텍스트 로컬 방식으로 동작한다 정도로 알면 될 것 같다.

### The Request Object

요청 객체는 API 섹션에 문서화되어 있으며 여기서 자세히 다루지 않을 것입니다([Request 참조](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request)). 다음은 가장 일반적인 작업 중 일부에 대한 광범위한 개요입니다. 먼저 플라스크 모듈에서 가져와야합니다.

```py
from flask import request
```

현재 요청 방법은 method 속성을 사용하여 사용할 수 있습니다. 양식 데이터 (POST 또는 PUT 요청에서 전송 된 데이터)에 액세스하려면 양식 속성을 사용할 수 있습니다. 다음은 위에서 언급 한 두 가지 속성의 전체 예입니다.

```py
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
```

양식 속성에 키가 없으면 어떻게 됩니까? 이 경우 특별한 KeyError가 발생합니다. 표준 KeyError처럼 포착 할 수 있지만 그렇게 하지 않으면 HTTP 400 Bad Request 오류 페이지가 대신 표시됩니다. 따라서 많은 상황에서 그 문제를 다룰 필요가 없습니다.

URL(?key=value)에 제출 된 매개 변수에 액세스하려면 args 속성을 사용할 수 있습니다.

```py
searchword = request.args.get('key', '')
```

사용자가 URL을 변경하고 400 요청 페이지를 표시하는 것은 사용자 친화적이지 않기 때문에 get 또는 KeyError를 포착하여 URL 매개 변수에 액세스하는 것이 좋습니다.

요청 객체의 메서드 및 속성에 대한 전체 목록은 [요청 문서](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request)를 참조하세요.

### 파일 업로드

Flask로 업로드 된 파일을 쉽게 처리 할 수 있습니다. HTML 양식에 enctype = "multipart / form-data"속성을 설정하는 것을 잊지 마십시오. 그렇지 않으면 브라우저가 파일을 전혀 전송하지 않습니다.

업로드 된 파일은 메모리 또는 파일 시스템의 임시 위치에 저장됩니다. 요청 개체의 파일 속성을 확인하여 해당 파일에 액세스 할 수 있습니다. 업로드 된 각 파일은 해당 사전에 저장됩니다. 표준 Python 파일 객체처럼 작동하지만 서버의 파일 시스템에 해당 파일을 저장할 수있는 save () 메서드도 있습니다. 다음은 작동 방식을 보여주는 간단한 예입니다.

```py
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
```

파일이 애플리케이션에 업로드되기 전에 클라이언트에서 파일 이름이 어떻게 지정되었는지 알고 싶다면 filename 속성에 액세스 할 수 있습니다. 그러나이 값은 위조 될 수 있으므로 절대로 그 값을 신뢰하지 마십시오. 클라이언트의 파일 이름을 사용하여 서버에 파일을 저장하려면 Werkzeug가 제공하는 secure_filename () 함수를 통해 전달하십시오.

```py
from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
    ...
```
- 더 나은 예를 보려면 [파일 업로드 패턴](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files)을 확인하세요.
- 파일 쪽 업로드 부분은 무시. 할 일이 없음

### 쿠키
쿠키에 액세스하려면 쿠키 속성을 사용할 수 있습니다. 쿠키를 설정하려면 응답 객체의 set_cookie 메소드를 사용할 수 있습니다. 요청 개체의 쿠키 속성은 클라이언트가 전송하는 모든 쿠키가 포함 된 사전입니다. [세션](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)을 사용하려면 쿠키를 직접 사용하지 말고 대신 쿠키 위에 보안을 추가하는 Flask의 세션을 사용하십시오.

```py
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```

```py
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```

쿠키는 응답 개체에 설정됩니다. 일반적으로 보기 함수에서 문자열을 반환하기 때문에 Flask는 이를 응답 객체로 변환합니다. 명시 적으로 그렇게하려면 make_response() 함수를 사용한 다음 수정할 수 있습니다.

때때로 응답 객체가 아직 존재하지 않는 지점에 쿠키를 설정하고자 할 수 있습니다. 이는 [지연된 요청 콜백 패턴](https://flask.palletsprojects.com/en/1.1.x/patterns/deferredcallbacks/#deferred-callbacks)을 활용하여 가능합니다.

이에 대해서는 [응답 정보](https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses)도 참조 하십시오.

## 리다이렉션 및 오류

사용자를 다른 끝점으로 리디렉션하려면 [redirect()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.redirect) 함수를 사용하십시오. 오류 코드로 요청을 조기에 중단하려면 [abort()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.abort) 함수를 사용하십시오.

```py
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

이것은 사용자가 색인에서 액세스 할 수없는 페이지 (401은 액세스가 거부됨을 의미)로 리디렉션되기 때문에 다소 무의미한 예이지만 작동 방식을 보여줍니다.

기본적으로 각 오류 코드에 대해 흑백 오류 페이지가 표시됩니다. 오류 페이지를 사용자 정의하려면 errorhandler() 데코레이터를 사용할 수 있습니다.

```py
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

render_template() 호출 후의 404에 유의하십시오. 이것은 Flask에게 해당 페이지의 상태 코드가 찾을 수 없음을 의미하는 404이어야 함을 알려줍니다. 기본적으로 200은 모든 것이 문제 없다로 해석 됩니다.

자세한 내용은 [오류 처리기](https://flask.palletsprojects.com/en/1.1.x/errorhandling/#error-handlers)를 참조하십시오.

## About Responses

보기 함수의 반환 값은 자동으로 응답 개체로 변환됩니다. 반환 값이 문자열 인 경우 문자열이 응답 본문, 200 OK 상태 코드 및 text/html MIME 유형 인 응답 객체로 변환됩니다. 반환 값이 dict이면 응답을 생성하기 위해 jsonify()가 호출됩니다. Flask가 반환 값을 응답 개체로 변환하는 데 적용하는 논리는 다음과 같습니다.

1. 올바른 유형의 응답 객체가 반환되면 뷰에서 직접 반환됩니다.
2. 문자열 인 경우 해당 데이터와 기본 매개 변수를 사용하여 응답 객체가 생성됩니다.
3. dict 인 경우 응답 객체는 jsonify를 사용하여 생성됩니다.
4. 튜플이 반환되면 튜플의 항목이 추가 정보를 제공 할 수 있습니다. 이러한 튜플은 (응답, 상태), (응답, 헤더) 또는 (응답, 상태, 헤더) 형식이어야합니다. 상태 값은 상태 코드를 재정의하고 헤더는 추가 헤더 값의 목록 또는 사전이 될 수 있습니다.
5. 작동하지 않는 경우 Flask는 반환 값이 유효한 WSGI 응용 프로그램이라고 가정하고이를 응답 객체로 변환합니다.

뷰 내에서 결과 응답 객체를 얻으려면 make_response() 함수를 사용할 수 있습니다.

```py
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

반환 표현식을 make_response()로 래핑하고 응답 객체를 가져와 수정 한 다음 반환하면 됩니다.

```py
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

### APIs with JSON

API를 작성할 때 일반적인 응답 형식은 JSON입니다. Flask로 이러한 API 작성을 시작하는 것은 쉽습니다. 뷰에서 dict를 반환하면 JSON 응답으로 변환됩니다.

```py
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
```

API 디자인에 따라 dict 이외의 유형에 대한 JSON 응답을 만들 수 있습니다. 이 경우 지원되는 모든 JSON 데이터 유형을 직렬화하는 [jsonify()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify) 함수를 사용하십시오. 또는 더 복잡한 애플리케이션을 지원하는 Flask 커뮤니티 확장을 살펴보세요.

```py
@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])
```
- python list 내의 for문은 또 봐도 적응이 안됨.

## 세션

세션, 쿠키는 매일 보는 개념인데 항상 볼때마다 정확히 어떤 개념인지 좀 헷갈리는 것 같다.

요청 객체 외에도 세션이라는 두 번째 객체가있어 한 요청에서 다음 요청까지 사용자 별 정보를 저장할 수 있습니다. 이는 귀하를 위해 쿠키 위에 구현되며 암호화 방식으로 쿠키에 서명합니다. 이것이 의미하는 바는 사용자가 서명에 사용 된 비밀 키를 모르면 쿠키의 내용을 볼 수는 있지만 수정할 수는 없다는 것입니다.

```py
from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```

여기에 언급 된 escape()는 템플릿 엔진을 사용하지 않는 경우 이스케이프 처리합니다 (이 예제에서와 같이).

### 좋은 비밀 키를 생성하는 방법

비밀 키는 가능한 한 임의적이어야합니다. 운영 체제에는 암호화 랜덤 생성기를 기반으로 매우 임의의 데이터를 생성하는 방법이 있습니다. 다음 명령을 사용하여 Flask.secret_key (또는 SECRET_KEY)에 대한 값을 빠르게 생성합니다.

```
$ python -c 'import os; print (os.urandom (16)) '
b'_5 # y2L "F4Q8z \ n \ xec] / '
```

쿠키 기반 세션에 대한 참고 사항 : Flask는 세션 개체에 입력 한 값을 가져 와서 쿠키에 직렬화합니다. 일부 값이 요청간에 유지되지 않고 쿠키가 실제로 활성화되어 있으며 명확한 오류 메시지가 표시되지 않는 경우 웹 브라우저에서 지원하는 크기와 비교하여 페이지 응답에서 쿠키 크기를 확인하십시오.

기본 클라이언트 측 기반 세션 외에도 서버 측에서 세션을 처리하려는 경우 이를 지원하는 여러 Flask 확장이 있습니다.

- 쿠키(Cookie)
    - 쿠키는 클라이언트에 저장되는 키와 값이 들이있는 작은 데이터 파일입니다.
    - 쿠키는 이름, 값, 만료날짜(쿠키 저장기간), 경로정보가 들어있습니다.
    - 쿠키는 일정 시간동안 데이터를 저장할 수 있어서 로그인 상태를 유지합니다.
    - 쿠키는 클라이언트의 상태 정보를 본인 하드 디스크에 저장하였다가 필요할 때 참조, 재사용합니다
- 세션(Session)
    - 세션은 클라이언트와 웹서버 간 네트워크 연결이 지속 유지되고 있는 상태를 말합니다.
    - 즉, 사용자가 브라우저를 열어 서버에 접속한 뒤 접속을 종료할 때 시점 까지를 말합니다.
    - HTTP 프로토콜은 비접속형 프로토콜이므로, 매 접속시마다 새로운 네트워크 연결이 이루어지는데, 세션이 연결유지를 가능하게 해줍니다.
    - 클라이언트가 웹서버에 Request를 보내면, 해당 서버의 엔진이 클라이언트에게 유일한 ID를 부여하는데 이 ID를 세션이라고 부릅니다.
    - 세션 ID는 임시로 저장하여 페이지 이동 시 이용하거나, 클라이언트가 재 접속 했을 때 클라이언트를 유일하게 구분하는 수단이 됩니다.

## Message Flashing

좋은 애플리케이션과 사용자 인터페이스는 모두 피드백에 관한 것입니다. 사용자가 충분한 피드백을받지 못하면 응용 프로그램을 싫어하게 될 것입니다. Flask는 플래싱 시스템을 사용하여 사용자에게 피드백을 제공하는 매우 간단한 방법을 제공합니다. 플래싱 시스템은 기본적으로 요청이 끝날 때 메시지를 기록하고 다음 요청에만 액세스 할 수있게합니다. 이것은 일반적으로 메시지를 노출하기 위해 레이아웃 템플릿과 결합됩니다.

메시지를 플래시하려면 flash() 메서드를 사용하고, 메시지를 가져 오려면 템플릿에서도 사용할 수 있는 get_flashed_messages()를 사용할 수 있습니다. 전체 예제는 [Message Flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/#message-flashing-pattern)을 확인하십시오.


## 로깅

때로는 정확해야 하지만 실제로는 그렇지 않은 데이터를 다루는 상황에 있을 수 있습니다. 예를 들어 HTTP 요청을 서버에 보내는 클라이언트 측 코드가 있지만 분명히 잘못된 형식 일 수 있습니다. 이는 사용자가 데이터를 조작하거나 클라이언트 코드가 실패하여 발생할 수 있습니다. 대부분의 경우 해당 상황에서 400 Bad Request로 응답하는 것은 괜찮지만 때로는 그렇게 하지 않고 코드가 계속 작동 해야 되는 경우도 있습니다.

수상한 일이 발생했음을 여전히 기록 할 수 있습니다. 이것은 로거가 유용한 곳입니다. Flask 0.3부터 로거는 사용자가 사용할 수 있도록 미리 구성되어 있습니다.

```py
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

첨부 된 로거는 표준 로깅 로거이므로 자세한 내용은 공식 로깅 문서를 참조하십시오.

[응용 프로그램 오류](https://flask.palletsprojects.com/en/1.1.x/errorhandling/#application-errors)에 대해 자세히 알아보십시오.

## Hooking in WSGI Middleware

Flask 애플리케이션에 WSGI 미들웨어를 추가하려면 애플리케이션의 wsgi_app 속성을 래핑합니다. 예를 들어 Nginx 뒤에서 실행하기 위해 Werkzeug의 ProxyFix 미들웨어를 적용하려면 :

```py
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
```

app 대신 app.wsgi_app을 래핑하면 앱이 여전히 미들웨어가 아닌 Flask 애플리케이션을 가리 키므로 앱을 계속 사용하고 직접 구성 할 수 있습니다.

## Using Flask Extensions

확장은 일반적인 작업을 수행하는 데 도움이되는 패키지입니다. 예를 들어 Flask-SQLAlchemy는 Flask에서 간단하고 쉽게 사용할 수 있도록 SQLAlchemy 지원을 제공합니다.

Flask 확장에 대한 자세한 내용은 [확장](https://flask.palletsprojects.com/en/1.1.x/extensions/#extensions)을 참조하세요.

## Deploying to a Web Server

새로운 Flask 앱을 배포 할 준비가 되셨습니까? [배포 옵션](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment)으로 이동합니다.

## 참조
- https://flask.palletsprojects.com/en/1.1.x/quickstart/