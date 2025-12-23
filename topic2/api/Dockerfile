FROM python:3.13-slim
WORKDIR /app
RUN pip install flask pytz
COPY ./api/app.py .
COPY var.env .
ENV FLASK_APP app.py
EXPOSE 30307
CMD ["flask", "run", "--host=0.0.0.0", "-p", "30307"]