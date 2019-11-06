FROM nginx/unit:1.12.0-python2.7

COPY requirements.txt /config/requirements.txt

RUN apt update && apt install -y python-pip                               \
    && pip install -r /config/requirements.txt                            \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list
