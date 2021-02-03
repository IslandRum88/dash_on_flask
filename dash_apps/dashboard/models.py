from sqlalchemy import Column, DateTime, Integer, String, TEXT, ForeignKey

from models import Base


class Plotter(Base):
    __tablename__ = 'Plotters'

    Id = Column(Integer, primary_key=True)
    Title = Column(String(100), nullable=False)
    CreatedAt = Column(DateTime, nullable=False)
    Body = Column(String(100))
