FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt .
ENV ACCOUNT_SID=AC0eeef15ff1ac19864fdd0717979ccdec
ENV AUTH_TOKEN=d4db30cfbeb35325c7a7cc8137651384
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]