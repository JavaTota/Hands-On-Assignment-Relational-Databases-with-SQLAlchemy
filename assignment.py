from sqlalchemy import Boolean, Column, ForeignKey, Integer, Integer, String, Table, create_engine, select
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

# user1 = User(name="Alice", email="alice@gmail.com")
# user2 = User(name="Marco", email="marco@gmail.com")

# product1 = Product(name="Laptop", price=1200)
# product2 = Product(name="Phone", price=800)
# product3 = Product(name="Headphones", price=150)

# order1 = Order(quantity=1, status=True)
# order2 = Order(quantity=2, status=False)
# order3 = Order(quantity=3, status=True)
# order4 = Order(quantity=4, status=False)

# order1.users.append(user1)
# order2.users.append(user1)
# order3.users.append(user2)
# order4.users.append(user2)

# order1.products.append(product1)
# order2.products.extend([product2, product3])
# order3.products.append(product1)
# order4.products.extend([product1, product2, product3])

# session.add_all([
#     user1, user2,
#     product1, product2, product3,
#     order1, order2, order3, order4
# ])
# session.commit()

# Retrieve all users and print their information.

# query = session.query(User)
# users = session.execute(query).scalars().all()

# for user in users:
#     print(f"User: {user.name}, Email: {user.email}")

# Retrieve all products and print their name and price.
# query = session.query(Product)
# products = session.execute(query).scalars().all()

# for product in products:
#     print(f"Product: {product.name}, Price: {product.price}")

print("----------------------------------------------------------")

# Retrieve all orders, showing the user’s name, product name, and quantity.
orders = session.scalars(select(Order)).all()
print("Orders found:")

for order in orders:
    for user in order.users:
            for product in order.products:
                print(f"User: {user.name}, Product: {product.name}, Quantity: {order.quantity}")

print("----------------------------------------------------------")

# Update a product’s price.
query = select(Product).where(Product.name == "Laptop")
laptop = session.execute(query).scalars().first()

laptop.price = 1100
session.commit()

print(f"Updated Laptop Price: {laptop.price}")

print("----------------------------------------------------------")

# Delete a user by ID.
# query = select(User).where(User.id == 1)
# user_to_delete = session.execute(query).scalars().first()

# session.delete(user_to_delete)
# session.commit()

# Query all orders that are not shipped.
query = select(Order).where(Order.status == False)
unshipped_orders = session.execute(query).scalars().all()

print("Unshipped Orders found:", len(unshipped_orders))


for order in unshipped_orders:
    for user in order.users:
        print(f"User: {user.name} - Product: {', '.join([p.name for p in order.products])} - Quantity: {order.quantity}")

print("----------------------------------------------------------")


# Count the total number of orders per user.
order_counts = {}
for order in orders:
    for user in order.users:
        order_counts[user.name] = order_counts.get(user.name, 0) + 1

print("Total Orders per User:")
for user_name, count in order_counts.items():
    print(f"User: {user_name}, Total Orders: {count}")


print("----------------------------------------------------------")