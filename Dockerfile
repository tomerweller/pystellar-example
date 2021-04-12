FROM python:3
ADD main.py /
RUN pip install requests stellar-sdk
CMD [ "python", "./main.py" ]
