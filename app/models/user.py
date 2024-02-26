from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String

from app.core.database import Base
from app.models.base import Timestamp


class User(Timestamp, Base):
    __tablename__ = "user"
    __table_args__ = {"comment": "회원"}

    id = Column(Integer, primary_key=True, index=True, comment="PK")
    username = Column(String(256), nullable=False, comment="이름")
    password = Column(String(256), nullable=False, comment="비밀번호")
