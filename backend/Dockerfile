FROM python:3.11-slim

ENV PIP_DISABLE_PIP_VESION_CHECK=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "4000"]