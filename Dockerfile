FROM python:3.9.2-slim-buster
LABEL org.opencontainers.image.created="2021-03-10T00:00:00Z" \
    org.opencontainers.image.authors="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/shagen/some-lint/" \
    org.opencontainers.image.documentation="https://sthagen.github.io/verbose-pancake/" \
    org.opencontainers.image.source="https://github.com/sthagen/verbose-pancake/" \
    org.opencontainers.image.version="0.0.1" \
    org.opencontainers.image.revision="39f0b68c3833926f195c52a89330b6f685bf7836" \
    org.opencontainers.image.vendor="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.licenses="MIT License" \
    org.opencontainers.image.ref.name="shagen/some-lint" \
    org.opencontainers.image.title="Experimental lint." \
    org.opencontainers.image.description="later)."

RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y --no-install-recommends tini && \
apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home action
USER action
COPY some_lint /app/some_lint
ENV PYTHONFAULTHANDLER=1
ENTRYPOINT ["tini", "--", "python", "-m", "some_lint"]
