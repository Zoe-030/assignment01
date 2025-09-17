from sqlalchemy import create_engine, text
from app.config import config

engine = create_engine(config.db_url)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT now()")).fetchone()
        print("✅ Connected! Current time:", result[0])
except Exception as e:
    print("❌ Connection failed:", e)

