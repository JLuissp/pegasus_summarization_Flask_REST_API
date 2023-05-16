FROM python:3.10.10
ARG VERSION
LABEL org.label-schema.version=$VERSION
COPY ./requirements.txt /webapp/requirements.txt
WORKDIR /webapp
RUN pip install -r requirements.txt
COPY webapp/* /webapp
ENTRYPOINT ["python"]
CMD ["app.py"]