from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD


engine = create_async_engine(
    f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()
