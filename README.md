# Setup

* create / rename source directory

```
mv grpctest <projectname>
```

* setup Makefile

```
vim Makefile
...
PROJECT := <projectname>
```

* create python venv

```
python3 -m venv <.projectname>
```

* source venv

```
source <.projectname>/bin/activate
```

* upgrade pip

```
pip3 install --upgrade pip
```

* install requirements

```
pip3 install -r requirements.txt
```

* install dependencies

```
make deps
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

curl -sSk -XPOST localhost:8080/v1/echo -d {"name": "yeah"}
