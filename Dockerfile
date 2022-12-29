FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --upgrade -r ./requirements.txt
# RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
EXPOSE 8000
WORKDIR /app
ENV PYTHONPATH=/app/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]