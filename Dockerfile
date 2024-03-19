FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update 

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "simulador.py",]