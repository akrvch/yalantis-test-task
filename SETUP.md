### Installation
There are several ways to get the project on your pc.
#### HTTPS

```bash
# Clone repository via HTTPS
$ git clone https://github.com/akrvch/yalantis-test-task.git
```

#### SSH

```bash
# Clone repository via SSH
$ git clone git@github.com:akrvch/yalantis-test-task.git
```

#### Download

You can also download .zip archive from GitHub:

<a class="button" href="//github.com/akrvch/yalantis-test-task/archive/refs/heads/master.zip">Download .zip</a>

### Set up Virtual Environment

#### Install `virtualenv`
```bash
$ pip install virtualenv
```
#### Create Virtual Environment
```bash
$ cd yalantis-test-task
$ python virtualenv venv
```
#### Activate Virtual Environment
```bash
$ cd venv/Scripts
$ activate
```

### Install requirements

After activating your virtual environment (check `(venv)` badge on command prompt) you have to install project requirements.

```bash
$ pip install -r requirements.txt
```

### Run Server
```bash
$ python manage.py runserver
```