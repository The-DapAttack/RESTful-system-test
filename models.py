from sqlalchemy import Column,ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, relationship


#   DEFINE DECLARATIVE BASE OBJECT
Base = declarative_base()

#   DEFINE CLASS FOR TABLE CREATION

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type = Column(String, nullable=False)
    username = Column(String, nullable=False)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    date_of_birth = Column(String, nullable=False)
    email = Column(String(45), nullable=False)
    password_hash = Column(String(60), nullable=False)
    created_at = Column(String, nullable=False)

#   RELATION TO AUTH TABLE
    auth = relationship("UserAuth", uselist=False, back_populates="user")

class UserAuth(Base):
    __tablename__ = 'user_auth'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    last_login = Column(DateTime)

    user = relationship("User", back_populates="auth")


