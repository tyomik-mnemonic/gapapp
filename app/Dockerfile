FROM python:3.8.12

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["bash"]
CMD ["run_service.sh"]