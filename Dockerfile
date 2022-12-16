FROM public.ecr.aws/lambda/python:3.8

RUN mkdir -p /app
COPY . main.py /app/
COPY . db_set_up.py /app/
COPY . covid_19_cases.csv /app/
COPY . requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
RUN python3 db_set_up.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
