from sqlalchemy import Column, String, Integer
from linebot.models import *
from models.database import Base, db_session

class Products(Base):
    __tablename__='preducts'

    id = Column(Integer, primary_key=True) #主鍵
    name = Column(String) #產品名稱
    price = Column(Integer) #產品價格
    description = Column(String) #產品說明
    product_image_url = Column(String) #產品圖片

