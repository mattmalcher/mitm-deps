FROM python:3.9.13
COPY mitmproxy-ca.crt /usr/local/share/ca-certificates/mitmproxy-ca.crt
RUN update-ca-certificates --fresh
ENV CURL_CA_BUNDLE=/usr/local/share/ca-certificates/mitmproxy-ca.crt

# sys deps from https://github.com/pytorch/pytorch/blob/master/Dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        ccache \
        cmake \
        curl \
        git \
        libgl1 \
        libjpeg-dev \
        libpng-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

# get smaller - cpu only version of torch
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install -qr https://raw.githubusercontent.com/hustvl/YOLOP/main/requirements.txt  # install dependencies

ENV TORCH_HOME = "/host/content"
CMD python3 -c "import torch; model = torch.hub.load('hustvl/yolop', 'yolop', pretrained=True, trust_repo=True)"

