FROM python:alpine3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirenments.txt

EXPOSE 5005

ENTRYPOINT [ "python" ]

CMD [ "hello_app.py" ]