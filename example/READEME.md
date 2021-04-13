# SqlAlchemy

# Flask migrate
- https://flask-migrate.readthedocs.io/en/latest/

Flask-Migrate는 Flask 및 Flask-SQLAlchemy 애플리케이션과 함께 작동하는 적절한 방식으로 Alembic을 구성하는 확장입니다. 실제 데이터베이스 마이그레이션 측면에서 모든 것이 Alembic에서 처리되므로 정확히 동일한 기능을 사용할 수 있습니다. 

```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

- 해당 라이브러리를 사용해야 하는가?
- MySQL DB를 사용하고, 마이그레이션이 필요 없는 경우에도 사용해야 되는가?
- 스키마를 관리할 수 있으므로 사용해도 좋을 것으로 보이긴 함.
- 데이터 까진 관리 하지 못하지 않나?

# Flask-SQLalchemy
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/

Flask-SQLAlchemy는 애플리케이션에 SQLAlchemy에 대한 지원을 추가하는 Flask 용 확장입니다. 일반적인 작업을 더 쉽게 수행 할 수 있도록 유용한 기본값과 추가 도우미를 제공하여 Flask와 함께 SQLAlchemy 사용을 단순화하는 것을 목표로합니다.

ORM에 대한 심도있는 작업 방법은 SQLAlchemy 문서를 참조하십시오. 다음 문서는 가장 일반적인 작업과 Flask-SQLAlchemy와 관련된 기능에 대한 간략한 개요입니다.

Flask-SQLAlchemy는 사용하기 쉽고 기본 응용 프로그램에는 매우 쉬우며 대규모 응용 프로그램에도 쉽게 확장 할 수 있습니다. 전체 가이드를 보려면 SQLAlchemy 클래스에 대한 API 문서를 확인하세요.


# Alembic
- 데이터베이스 마이그레이션 도구
