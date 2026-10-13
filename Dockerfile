# import python
FROM python:3.15.0-slim

# set environment
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# set working directory
WORKDIR /code

# copy requirements
COPY ./requirements.txt /code/requirements.txt

# install requirments with minimal capacity
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy app
COPY ./app /code/app

# create temp user
RUN useradd -r appuser && chown -R appuser /code
USER appuser

# expose 8000 out of container
EXPOSE 8000

# run command
CMD ["uvicorn", "app.fastapi_demo:app", "--host", "0.0.0.0", "--port", "8000"]
