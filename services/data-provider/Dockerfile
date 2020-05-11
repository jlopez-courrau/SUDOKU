FROM python:3.8.1-slim-buster as base

# Install system dependencies
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
      netcat
RUN pip install poetry==1.0.5

# Set up and become kip user
RUN useradd -m kip
USER kip
RUN mkdir /home/kip/src
RUN mkdir /home/kip/src/data
WORKDIR /home/kip/src/data

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project setup files
COPY --chown=kip:kip poetry.lock .
COPY --chown=kip:kip pyproject.toml .
COPY --chown=kip:kip entrypoint.sh .
COPY --chown=kip:kip app.py .
COPY --chown=kip:kip mypy.ini .


#Copy remaining directories
COPY --chown=kip:kip project project
COPY --chown=kip:kip tests tests

# Install project requirements
RUN poetry config virtualenvs.in-project true
RUN poetry install -v --no-dev

# Run entrypoint.sh
ENTRYPOINT ["/home/kip/src/data/entrypoint.sh"]
