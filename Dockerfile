FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt "fastapi[standard]" "uvicorn[standard]"

COPY app/ ./app/
COPY static/ ./static/
COPY templates/ ./templates/
COPY techlog.db ./

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]