from sqlalchemy import Boolean, Column, ForeignKey, Integer, Integer, String, Table, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
from typing import List

engine = create_engine('mysql+mysqlconnector://root:Jahvante.97.mysql@localhost/Assignments')


class Base(DeclarativeBase):
    pass

user_orders = Table(
    'user_orders', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('order_id', Integer, ForeignKey('orders.id'))
)

product_orders = Table(
    'product_orders', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('order_id', Integer, ForeignKey('orders.id'))
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable = False)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    orders: Mapped[List['Order']] = relationship('Order', secondary=user_orders, back_populates='users')

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    orders: Mapped[List['Order']] = relationship('Order', secondary=product_orders, back_populates='products')

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    users: Mapped[List['User']] = relationship('User', secondary=user_orders, back_populates='orders')
    products: Mapped[List['Product']] = relationship('Product', secondary=product_orders, back_populates='orders')

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session(engine)