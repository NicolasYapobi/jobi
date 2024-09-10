FROM python:3.10.8-slim

COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app/app.py"]