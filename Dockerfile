FROM rust

RUN apt-get update -y && apt-get install -y python3 python3-pip make

RUN mkdir /cargo
RUN cargo install stork-search --locked --root /cargo

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD [ "python3" ]
