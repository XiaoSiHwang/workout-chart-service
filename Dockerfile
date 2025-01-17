# 
FROM python:3.12.2

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ /code/app

# 
CMD ["uvicorn", "app.main", "--host", "0.0.0.0", "--port", "80"]