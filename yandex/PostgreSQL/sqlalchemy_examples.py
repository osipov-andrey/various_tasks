from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer, String, select
from datetime import datetime, timedelta


engine = create_engine(
    'postgresql://andrey:andrey@0.0.0.0/mydb', echo=True
)

# with engine.connect() as conn:
#
#     data = conn.execute('SELECT 1').fetchone()
#     print(data)

"""
MetaData -  контейнер, который содержит информацию о схеме базы данных:
            таблицах, индексах, типах данных и т.п.
            
Table -     содержит описание таблиц. Для того, чтобы SQLAlchemy могла 
            генерировать запросы ей требуется информация о таблицах.
"""

metadata = MetaData()
domains = Table(
    'domains',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True),
    Column('owner', String),
)

with engine.connect() as conn:
    metadata.create_all(engine)

"""
Добавление данных с помощью SQLAlchemy
"""

# with engine.begin() as conn:
#
#     query = domains.insert().values([
#         {'name': 'example2.org', 'owner': 'Vin Diesel'},
#         {'name': 'another.org', 'owner': 'Pg Dumpledore'},
#     ]).returning(*domains.columns)
#
#     data = conn.execute(query).fetchall()
#     print(data)

"""
Получение данных с помощью SQLAlchemy
"""

with engine.connect() as conn:
    query = domains.select()
    data = conn.execute(query).fetchall()
    print(data)

"""
Расширение запросов
"""


def get_domains(is_deleted=False) -> 'Select':
    return domains.select().where(
        domains.c.is_deleted == is_deleted
    )


def get_expiring_domains()-> 'Select':
    date = datetime.now() + timedelta(days=2)
    return get_domains().where(domains.expire_at < date)


def get_domains_more(filter_query: 'Select', is_deleted=False) -> 'Select':
    query = domains.select().where(
        domains.c.is_deleted == is_deleted
    )

    if filter_query:
        subquery = filter_query.alias()
        query = select(query.columns).select_from(
            query.join(
                subquery, subquery.c.domain_id == query.c.domain_id
            )
        )

    return query