FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	curl \
	git \
	&& pip install flake8 \
	&& rm -rf /var/lib/apt/lists/*