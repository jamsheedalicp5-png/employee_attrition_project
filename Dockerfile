FROM python:3.13-slim

WORKDIR app/

COPY requirements.txt /app/requirements.txt

COPY clsf.pkl /app/clsf.pkl

COPY app.py /app/app.py

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]