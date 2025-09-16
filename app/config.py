
import os
from dotenv import load_dotenv

# Load all the stuff we wrote inside the .env file
# (like username, password, db name, etc.)
load_dotenv()

class Config:
    
    db_user: str = os.getenv("DB_USER", "postgres")       # who logs in to the database
    db_password: str = os.getenv("DB_PASSWORD", "password")  # the key 
    db_host: str = os.getenv("DB_HOST", "localhost")      # where the database
    db_port: str = os.getenv("DB_PORT", "5432")           
    db_name: str = os.getenv("DB_NAME", "healthdb")       # name of the database 

    @property
    def db_url(self):
       
        return f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

# we make one Config object we can import anywhere else in our code
config = Config()
