from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Domain(Base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    owner = Column(String)

    def __repr__(self):
        return f"<Domain(name='{self.name}', owner='{self.owner}'"

    def get_zone(self) -> str:
        return self.name.split('.')[-1]


print(Domain.__table__)  # {Table} domains
print(Domain.metadata)  # MetaData(bind=None)

engine = create_engine(
    'postgresql://andrey:andrey@0.0.0.0/mydb', echo=True
)
Session = sessionmaker(bind=engine)
session = Session()

# domain = Domain(name='example4.com', owner='Joe Cooker')
# session.add(domain)
# session.commit()

with session.transaction:
    domain = Domain(name='example4.com', owner='Joe Cooker')
    session.add(domain)


