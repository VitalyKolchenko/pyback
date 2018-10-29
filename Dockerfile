FROM python:3
ADD main.py /
RUN pip install sanic
CMD [ "python", "./main.py" ]