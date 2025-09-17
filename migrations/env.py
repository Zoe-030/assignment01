import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 这是 Alembic 的 Config 对象，提供了对 alembic.ini 的访问
config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


from app.models import HealthCheck
from app.db import Base


# target_metadata 用于自动生成迁移脚本
target_metadata = Base.metadata


def run_migrations_offline():
    """在 offline 模式下运行迁移"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """在 online 模式下运行迁移"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
