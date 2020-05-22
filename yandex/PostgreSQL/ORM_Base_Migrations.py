"""
Naming conventions
models/base.py
"""
from sqlalchemy import MetaData, Column, DateTime, text, Integer, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr

convention = {
    'all_columns_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(all_column_names)s',
    'uq': 'uq__%(table_name)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__'
        '%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}
metadata = MetaData(naming_convention=convention)


@as_declarative(metadata=metadata)
class Base:
    """
    Базовый класс для моделей
    """
    @declared_attr  # позволяет нормально наследоваться потом
    def created_at(cls):
        """ Это будет столбец в наследниках """
        return Column(DateTime(timezone=True),
                      server_default=text('clock_timestamp()'),
                      nullable=False)


class Domain(Base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    owner = Column(String)

    def __repr__(self):
        return f"<Domain(name='{self.name}', owner='{self.owner}'"

    def get_zone(self) -> str:
        return self.name.split('.')[-1]