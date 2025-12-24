FROM python:3.13-slim
WORKDIR /app
RUN pip install flask
COPY . .
EXPOSE 4567
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "-p", "4567"]