from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, Text, SmallInteger


Base = declarative_base()

class wiki_pages_revs(Base):

	__tablename__ = 'Wiki_pages_revs'

	id = Column(Integer, nullable = False, primary_key = True)
	rev_id = Column(Integer)
	user = Column(String(255), nullable = False)
	date = Column(DateTime, nullable = False)
	comment = Column(Text)
	__table_args__ = { 'mysql_engine': 'MyISAM', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci' }



class wiki_pages (Base):

	__tablename__ = 'Wiki_pages'

	page_id = Column(Integer, primary_key = True, autoincrement = False)
	namespace = Column(SmallInteger)
	title = Column(String(255), nullable = False)
	__table_args__ = { 'mysql_engine': 'MyISAM', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci' }



class people(Base):

	__tablename__ = 'People'

	id = Column(Integer, nullable = False, primary_key = True)
	name = Column(String(255), nullable = False)
	__table_args__ = { 'mysql_engine': 'MyISAM', 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci' }

	 























