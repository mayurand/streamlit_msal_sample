FROM python:3.9-slim

# Create user to avoid running as root
RUN useradd --create-home app

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.4.0

# Update pip
RUN pip install --upgrade pip

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy project files
COPY app ./app
COPY pyproject.toml poetry.lock ./

# Install application
RUN poetry install

EXPOSE 8080
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health
ENTRYPOINT ["streamlit", "run", "dashboard.py", "--server.port=8080", "--server.address=0.0.0.0"]
