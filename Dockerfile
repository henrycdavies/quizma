FROM python:3.11.1-slim
ARG UNAME=app
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID -o $UNAME && \
    useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

USER $UNAME

WORKDIR /home/app

COPY ./app ./start.sh ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["./start.sh"]
