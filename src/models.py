from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Sequence
from db import engine

Base = declarative_base()


class Row(Base):
    __tablename__ = 'row'
    id = Column(Integer, Sequence('row_id_seq'), primary_key=True)
    item_id = Column(String)
    detail = Column(String)
    d_o_d = Column(String)
    f_name = Column(String)
    m_name = Column(String)
    s_name = Column(String)
    address = Column(String)

    def __repr__(self):
        return "<Row(item_id='{}', detail='{}', d_o_d='{}', f_name='{}', m_name='{}', s_name='{}', address='{}')>".format(
            self.item_id, self.detail, self.d_o_d, self.f_name, self.m_name, self.s_name, self.address)


Base.metadata.create_all(engine)
