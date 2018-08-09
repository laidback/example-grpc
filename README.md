# Setup

```
$ python --version
>3.6
$ pip --version
>3.6
$ go --version
>1.9
$ export GOPATH=$(go env GOPATH)
$ export PATH=$PATH:$(go env GOBIN)
$ make --version
>4.2
```

```
# inside repo
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
$ make deps       # takes usually longer
$ make all
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
