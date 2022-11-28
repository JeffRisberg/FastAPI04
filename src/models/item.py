from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return "<Item(name='%s', description='%s', price=%d)>" % (
            self.name,
            self.description,
            self.price,
        )
