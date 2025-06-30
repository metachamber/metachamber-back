# MetaChamber Backend

Django REST API for metadata discovery platform.

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

## Docker

```bash
docker build -t metachamber-backend .
docker run -p 8000:8000 metachamber-backend
```

## API Endpoints

- `/admin/` - Django admin
- `/api/datasources/` - Data sources
- `/api/owners/` - Data owners  
- `/api/datasets/` - Datasets
- `/api/fields/` - Dataset fields