FROM rust as base

RUN mkdir /cargo
RUN cargo install stork-search --locked --root /cargo

FROM python:alpine3.16

COPY --from=base /cargo /cargo

ENV PATH /cargo/bin:$PATH
COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt && apk update && apk add --no-cache make

CMD [ "python3" ]

