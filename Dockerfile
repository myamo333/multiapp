FROM python:3.9.19-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get -y upgrade && pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["./app/🏠_Home_Page.py"]