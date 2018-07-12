# Setup

```
$ cd grpctest
$ python3 -m venv
$ source venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
$ make deps
```

# TESTING:

## Run components

```
# listen: localhost:50001
./grpctest/server/server.py

# connect: localhost:50001
./grpctest/client/client.py

# listen: localhost:8080
# connect: localhost:50001
./gateway -v 2
```

## Test gRPC Gateway:

```
curl -sSk -XPOST localhost:8080/v1/echo -d {"name": "yeah"}
```
