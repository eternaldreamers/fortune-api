from sqlalchemy import create_engine

from src.common.utils import module_path

def configure():
    engine = create_engine(module_path(), echo=True)
    return engine

sqlalchemy = configure()