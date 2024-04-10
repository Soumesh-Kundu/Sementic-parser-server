FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install flask
RUN pip install llama-index
RUN pip install python-dotenv
ENV API_KEY=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
EXPOSE 5000
CMD python ./main.py