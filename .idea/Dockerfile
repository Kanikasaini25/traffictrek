FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install requests
RUN pip install requests[socks]
RUN pip install selenium
RUN pip install schedule
RUN pip install stem
RUN pip install webdriver-manager

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]