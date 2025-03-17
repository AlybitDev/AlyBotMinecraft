FROM python:3.9

ADD main.py .

RUN python3 -m pip install -U javascript openai

CMD ["python","./main.py"]
