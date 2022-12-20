FROM python:3.9
WORKDIR /blog
COPY . .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
EXPOSE 8000
WORKDIR /blog
ENV PYTHONPATH=/blog
CMD ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "8000"]