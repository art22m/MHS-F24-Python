FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    --no-install-recommends

COPY . /app
WORKDIR /app
RUN python setup.py install

CMD python 2.2.py && pdflatex artifacts/out2.2.tex