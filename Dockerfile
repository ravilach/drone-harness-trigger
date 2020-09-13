FROM python:3.7.5-slim

RUN mkdir /opt/app
COPY harness-trigger-plugin.py /opt/app
WORKDIR /opt/app
RUN pip install requests

ENTRYPOINT ["python"]
CMD ["/opt/app/harness-trigger-plugin.py"]
