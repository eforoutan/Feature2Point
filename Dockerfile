FROM python:3.9

WORKDIR /app

COPY feature2point.py .

RUN pip install geopandas

ENTRYPOINT [ "python3" , "/app/feature2point.py" ]