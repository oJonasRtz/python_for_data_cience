FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	curl \
	git \
	&& pip install flake8 numpy pillow matplotlib\
	&& rm -rf /var/lib/apt/lists/*