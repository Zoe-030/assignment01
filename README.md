# Assignment 01 - Health Check API

## 1. Introduction

This is a backend web application for CSYE6225 Assignment 01.  
This project implements a simple Health Check API using FastAPI and PostgreSQL.

**Main Purpose:**
1. Practice how to choose and use a proper backend tech stack  
2. Understand and implement cloud-native application principles  
3. Provide one API that has all required functions  

---

## 2. Tech Stack

- Language: Python 3.13  
- Framework: FastAPI (modern, async-friendly web framework)  
- ORM: SQLAlchemy (for database models and operations)  
- Database: PostgreSQL 14 (relational database)  
- Environment Variables: python-dotenv (for config management)  
- Server: Uvicorn (ASGI server to run FastAPI)  

### 2.1 Project Structure
```
assignment01/
├─ alembic/                # Database migration configuration
│  └─ migrations/          # Alembic-generated migration scripts
├─ app/                    # Application package
│  ├─ __init__.py          # Package initializer
│  ├─ main.py              # FastAPI entry point
│  ├─ models.py            # SQLAlchemy data models
│  ├─ crud.py              # Database CRUD operations
│  ├─ db.py                # Database connection and session management
│  ├─ config.py            # Configuration loader (.env support)
│  └─ __pycache__/         # Python cache files (ignored in git)
├─ test_db.py              # Database test script
├─ alembic.ini             # Alembic main configuration file
├─ requirements.txt        # Project dependencies
└─ README.md               # Project documentation
```

---

## 3. Installation

### 3.1 Create virtual environment
```bash
cp ~/assignment01/.env ~/new_assignment01/ #if download one new file need copy .eny
cd ~/Downloads/Yadi_Zhao_002317736_01
python3 -m venv venv
source venv/bin/activate
```

### 3.2 Install dependencies
```bash
pip install -r requirements.txt
```

### 3.3 Set up database
a. Install PostgreSQL 14  
b. Create database `healthdb`  
c. Make sure there is one database account and password  
d. Modify the `.env` file:
```env
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=healthdb
```

### 3.4 Run database migration
```bash
# Create migration
alembic revision --autogenerate -m "create health_checks table"

# Apply migration
alembic upgrade head

# Verify table created
psql -U postgres -d healthdb -c "\d health_checks"
```

**Expected structure:**

| Column        | Type                         | Default   |
|---------------|------------------------------|-----------|
| check_id      | integer (PK, autoincrement)  | nextval(...) |
| check_datetime| timestamp with time zone     | now()     |

**Indexes:**
- `idx_check_datetime` btree (check_datetime)

### 3.5 Start application
```bash
cd ~/assignment01
source venv/bin/activate
brew services start postgresql@14
uvicorn app.main:app --reload
```

---

## 4. API Usage

### 4.1 Health Check - Success
```bash
curl -i http://127.0.0.1:8000/healthz
```
**Return:**
```
200 OK
date: Wed, 17 Sep 2025 19:01:15 GMT
server: uvicorn
cache-control: no-cache
content-length: 0
```

### 4.2 Invalid Request (Query params or body)
```bash
curl -i "http://127.0.0.1:8000/healthz?foo=bar"
```
**Return:**
```
400 Bad Request
```

```bash
curl -i -X GET http://127.0.0.1:8000/healthz -d '{"test":1}'
```
**Return:**
```
400 Bad Request
```

### 4.3 Wrong Method
```bash
curl -i -X POST http://127.0.0.1:8000/healthz
```
**Return:**
```
405 Method Not Allowed
```

### 4.4 Database Down
```bash
brew services stop postgresql@14
curl -i http://127.0.0.1:8000/healthz
```
**Return:**
```
503 Service Unavailable
```

---

## 5. Cloud-Native Design Compliance

1. **No saved sessions**: The app does not keep user info or memory. Every request is new and does not depend on old ones.  
2. **Settings outside code**: Database username, password, and host are not written inside the code. They are stored in `.env` file, so we can change them without changing the code.  
3. **Health check**: The `/healthz` API is used to check if the service is alive. If the database is down, it will return an error.  
4. **Handle database down**: When the database is not working, the app will return `503 Service Unavailable`. It will not crash or show `500 Internal Server Error`.  
5. **Tracking**: Each `/healthz` call is saved in the database table `health_checks`. Logs are also written by FastAPI and Uvicorn, so we can see what happens in the app.  
6. **Auto table creation**: Database tables are created by Alembic tool. We do not need to write SQL by hand. Just run `alembic upgrade head` and the table will be created automatically.  

---

## 6. Demo Instructions 

1. **Clone repository and setup environment**  
   Download the project code. Make a virtual environment and install all packages.  

2. **Run alembic upgrade head to auto-create tables**  
   Run this command to let Alembic build the `health_checks` table.  

3. **Start app**  
   ```bash
   uvicorn app.main:app --reload
   ```
   The FastAPI app will run on `http://127.0.0.1:8000`.  

4. **Test API with curl (see section 4)**  
   - Correct call will return `200 OK`.  
   - Wrong calls return `400` or `405`.  

5. **Stop DB and test error case**  
   ```bash
   brew services stop postgresql@14
   curl -i http://127.0.0.1:8000/healthz
   ```
   Should return `503 Service Unavailable`.  

---
