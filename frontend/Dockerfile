FROM python:3.10.8

LABEL org.label-schema.name="Weather-app"

WORKDIR /frontend

RUN apt-get update 

COPY ./requirments.txt /app/requirments.txt

RUN pip install -r requirments.txt

#COPY Weatherapp/.env.local /app/.env.local

COPY . /frontend

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

# docker build -t frontend .
# docker run -d -p 8501:8501 frontend