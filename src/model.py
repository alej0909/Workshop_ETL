from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CandidatesRaw(Base):
    __tablename__ = 'CandidatesRaw'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    First_Name = Column(String(100), nullable=False)
    Last_Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    Application_Date = Column(Date, nullable=False)
    Country = Column(String(100), nullable=False)
    YOE = Column(Integer, nullable=False)  
    Seniority = Column(String(100), nullable=False)
    Technology = Column(String(100), nullable=False)
    Code_Challenge_Score = Column(Integer, nullable=False)
    Technical_Interview_Score = Column(Integer, nullable=False)


class CandidatesTransformed(Base):
    __tablename__ = 'CandidatesTransformed'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    First_Name = Column(String(100), nullable=False)
    Last_Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    Application_Date = Column(Date, nullable=False)
    Country = Column(String(100), nullable=False)
    YOE = Column(Integer, nullable=False)  
    Seniority = Column(String(100), nullable=False)
    Technology = Column(String(100), nullable=False)
    Code_Challenge_Score = Column(Integer, nullable=False)
    Technical_Interview_Score = Column(Integer, nullable=False)
    Hired = Column(Integer, nullable=False)
