FROM python:3.9
WORKDIR /shift
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry
RUN poetry install
COPY . .
CMD ["poetry", "run", "uvicorn", "shift.main:app", "--host", "0.0.0.0", "--port", "8000"]
