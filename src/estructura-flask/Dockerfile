FROM python
RUN mkdir /demo
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv /demo/venv
RUN . /demo/venv/bin/activate
COPY requirements.txt /demo/
COPY app.py /demo/
RUN pip install -r /demo/requirements.txt
ADD ./apiflaskdemo /demo/apiflaskdemo
ADD ./data /demo/data
ENV FLASK_APP=/demo/app.py
EXPOSE 8080
RUN echo "#!/bin/bash\n. /demo/venv/bin/activate\nexport FLASK_APP=app.py\n/usr/local/bin/flask run -h 0.0.0.0 -p 8080\n" > /usr/bin/start.sh
RUN chmod +x /usr/bin/start.sh
WORKDIR /demo/
CMD /usr/bin/start.sh
