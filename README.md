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
