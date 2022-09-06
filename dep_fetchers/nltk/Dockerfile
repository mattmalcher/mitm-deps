FROM python:3.9.2
COPY mitmproxy-ca.crt /usr/local/share/ca-certificates/mitmproxy-ca.crt
RUN update-ca-certificates --fresh
ENV CURL_CA_BUNDLE=/usr/local/share/ca-certificates/mitmproxy-ca.crt
RUN pip install -U pip
RUN pip install nltk
CMD python3 -m nltk.downloader all -d  "/host/content"

