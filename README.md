# MediPro Clinic

A web-based clinic management system designed to streamline appointment booking, service catalog, and client communication — built with Django.

---

## 📌 Project Management
All tasks, sprints, and progress tracking are managed in **Asana**.  
🔗 **Asana Board:** [View Board](https://app.asana.com/1/1210988392005543/project/1211005386873495/overview)

## 📂 Project Documentation
Full documentation (UML diagrams, user stories, technical specifications) is available in the project folder.  
🔗 **Docs:** [View Docs](https://github.com/GoGei/medi-pro/tree/main/docs)

---

## ⚙️ Setup Project

### 1. Clone & Configure
```bash
git clone https://github.com/GoGei/medi-pro.git
uv venv env --python=/usr/bin/python3.11
source env/bin/activate
uv pip install -r requirements.lock
cp configs/settings_example.py configs/settings.py
```

### 2. Add Hosts
**Locations:**
- **Linux / MacOS:** `/etc/hosts`
- **Windows:** `C:\Windows\System32\drivers\etc\hosts`

Add:
```
127.0.0.1 medi-pro.local
127.0.0.1 api.medi-pro.local
127.0.0.1 admin.medi-pro.local
127.0.0.1 clinic.medi-pro.local
```

### 3. Create Database (PostgreSQL)
> ⚠️ Ensure `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD` in settings match these values.

```sql
CREATE USER medipro_user WITH ENCRYPTED PASSWORD 'medi_password';
ALTER ROLE medipro_user CREATEDB; -- allow creating databases for tests
CREATE DATABASE medipro WITH OWNER medipro_user ENCODING 'UTF-8';
```

### 4. Complete Setup
```bash
./manage.py migrate
fab compilemessages
```

### 5. Create Default Superuser
```bash
export DJANGO_SUPERUSER_EMAIL=example@localhost.com
export DJANGO_SUPERUSER_PASSWORD=strongpassword
./manage.py create_default_superuser
```

---

## 🛠 Useful Commands
| Command | Description |
|---------|-------------|
| `fab runserver` | Start server |
| `fab compilerequirements` | Compile requirements using `uv` |
| `fab makemessages` | Create i18n messages |
| `fab compilemessages` | Compile i18n messages |
| `fab check` | Run code checks (flake8, etc.) |
| `fab celeryrun` | Start Celery |
| `fab celerybeat` | Start Celery Beat |

---

## 🌐 Subdomains
Example for `.medi-pro.local` (default port `8000`):
- [http://medi-pro.local:8000/](http://medi-pro.local:8000/)
- [http://api.medi-pro.local:8000/](http://api.medi-pro.local:8000/)
- [http://admin.medi-pro.local:8000/](http://admin.medi-pro.local:8000/)
- [http://clinic.medi-pro.local:8000/](http://clinic.medi-pro.local:8000/)
