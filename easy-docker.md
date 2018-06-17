# Easy Docker


# Questions

# X. WHY / Outline

## THEME: no surprises
- single artifact re-use btw Dev, QA,and Prod: 
- easily run locally from scratch (Credstore this week!)
- (be super careful about version numbers!)
- 
## Outline
- basics (run package in self-contained unit)
- customize (one-off, temporary work/tools; adapt standard services)
- mission-critical coin flipper, with containerized database

# 1. BASICS // Docker = run package in self-contained unit

*IDEAS*
image ~ package, list of files
container
- separate file system
- separate networking
download package, use it to create a running container
not installed, container is *process*

## DIAGRAM: Docker client-server-service

## docker run -it python:3.6 (use local image)

options: interactive, terminal

    lilbub:randocat2 johnmitchell$ docker run -it python:3.6
    Python 3.6.4 (default, Dec 21 2017, 01:35:12)
    [GCC 4.9.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print(2*3)
    6
    >>>
    lilbub:randocat2 johnmitchell$


## just try something (Figlet)

    $ docker run -it --rm mbentley/figlet Free Beer
    Unable to find image 'mbentley/figlet:latest' locally
    latest: Pulling from mbentley/figlet
    c52e3ed763ff: Pull complete
    bb9a365b28e8: Pull complete
    bbe1c9f335a7: Pull complete
    a3ed95caeb02: Pull complete
    Digest: sha256:9545f0a713bf48a192ad522c739fa458a41786c72517d183fb777b9ba23f1593
    Status: Downloaded newer image for mbentley/figlet:latest
     _____                ____
    |  ___| __ ___  ___  | __ )  ___  ___ _ __
    | |_ | '__/ _ \/ _ \ |  _ \ / _ \/ _ \ '__|
    |  _|| | |  __/  __/ | |_) |  __/  __/ |
    |_|  |_|  \___|\___| |____/ \___|\___|_|

## great for temporary tools, single-use container, e.g. Apache Benchmark

    $ docker run --rm jordi/ab https://www.docker.com/

    This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking www.docker.com (be patient).....done


    Server Software:        nginx
    Server Hostname:        www.docker.com
    Server Port:            443
    SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128
    TLS Server Name:        www.docker.com

    Document Path:          /
    Document Length:        57926 bytes

    Concurrency Level:      1
    Time taken for tests:   0.154 seconds
    Complete requests:      1
    Failed requests:        0
    Total transferred:      58743 bytes
    HTML transferred:       57926 bytes
    Requests per second:    6.50 [#/sec] (mean)
    Time per request:       153.826 [ms] (mean)
    Time per request:       153.826 [ms] (mean, across all concurrent requests)
    Transfer rate:          372.93 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:       99   99   0.0     99      99
    Processing:    55   55   0.0     55      55
    Waiting:       25   25   0.0     25      25
    Total:        154  154   0.0    154     154


## DIAGRAM: computer, computer+VM, computer+containers



## ? image ~ package

### list local images // docker images

### search in dockerhub // docker search hello --limit 5

### image > package

- really awkward to install specific version (Node)
- only one at a time

## ? Clean up (--rm)

By default a container’s file system persists even after the container exits. This makes debugging a lot easier (since you can inspect the final state) and you retain all your data by default. But if you are running short-term foreground processes, these container file systems can really pile up. If instead you’d like Docker to automatically clean up the container and remove the file system when the container exits, you can add the --rm flag:


## OUTBOX
### node


    $ docker run -it bitnami/node:8
    
    > console.log('beer')
    beer
    undefined

### ? docker run -it python:2.7 (download image)


    lilbub:randocat2 johnmitchell$ docker run -it python:2.7
    Unable to find image 'python:2.7' locally
    2.7: Pulling from library/python
    cc1a78bfd46b: Already exists
    d2c05365ee2a: Pull complete
    231cb0e216d3: Pull complete
    3d2aa70286b8: Pull complete
    e80dfb6a4adf: Pull complete
    48409f4a5045: Pull complete
    782e083f6fb3: Pull complete
    05f1881bbfa0: Pull complete
    34ef48addd12: Pull complete
    Digest: sha256:cbe8cc0e224c4aa49e300dd4092a9bbeb8e0ec419a6b130e93a053cfedd44c03
    Status: Downloaded newer image for python:2.7
    Python 2.7.15 (default, Jun  6 2018, 19:38:24)
    [GCC 6.3.0 20170516] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print 2*3
    6
    >>>
    lilbub:randocat2 johnmitchell$

### ? docker run -it bitnami/node

    images are versioned like packages
    ALWAYS version your packages, and containers!
    ? compare w/ "brew install node@8" -- very awkward!

    ## image can be tiny or huge

        $ docker run ubuntu:18.04 du -sh
        75M .

    ## this is odd, as the 18.04 compressed ISO is almost 2GB!
    - _minimal_ image with only 94 packages installed



# 2. CUSTOMIZE // adapt standard services
*Ideas*
- customize standard tool/service
- minor variation of standard services
- one-off, temporary work

## docker run  -e POSTGRES_PASSWORD=beer -p 5432:5432 postgres:9.6.5
- logs go to terminal
- run Dbeaver
- map port, containers have private network

## run multiple versions of same server!

    $ docker run -d -p 10034:27017 mongo:3.4
    a8afd65c59646d8b9855aaac9eeecde904caeedccf520caa46c38c8cfae5c1f5
    $ docker run -d -p 10032:27017 mongo:3.2
    353116ba50500bf7e030147c43667579f48603229f2df932018a4aee91af2f9f

    $ docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                      NAMES
    353116ba5050        mongo:3.2           "docker-entrypoint.s…"   44 seconds ago       Up 47 seconds       0.0.0.0:10032->27017/tcp   xenodochial_colden
    a8afd65c5964        mongo:3.4           "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:10034->27017/tcp   gifted_goldstine
    016646dc2e66        mongo:3.6           "docker-entrypoint.s…"   2 minutes ago        Up 2 minutes        0.0.0.0:10036->27017/tcp   inspiring_cray

- compare with how you'd do with with packages installed on the host!
-- awkward => trivial!

## ? TBD db changes saves with commit ; create own image: powerful but opaque
? VS: SQL file


# 3. WEBAPP

*Ideas*
(Dockerfile = image specification for _files_ and metadata)
- docker-compose = wrapper dev container / cluster specification
Randocat
- map host drive
randocat w/ database

## Django Hello World w/ Database

### XXXX be super-careful about versions!

Compose example specifies Django < 2.0, default Django docs is 2.0, and is confusingly different!

https://docs.docker.com/compose/django/#define-the-project-components

### docker-compose run web django-admin.py startproject composeexample .

    $ ls -l composeexample/ manage.py
    -rwxr-xr-x  1 johnmitchell  staff  812 Jun 17 11:46 manage.py*

    composeexample/:
    total 24
    -rw-r--r--  1 johnmitchell  staff     0 Jun 17 11:46 __init__.py
    -rw-r--r--  1 johnmitchell  staff  3121 Jun 17 11:46 settings.py
    -rw-r--r--  1 johnmitchell  staff   771 Jun 17 11:46 urls.py
    -rw-r--r--  1 johnmitchell  staff   406 Jun 17 11:46 wsgi.py

### add database to composeexample/settings.py

### run: dc up

    Successfully built d081cebc7445
    Successfully tagged randocatdjango_web:latest
    Starting randocatdjango_database_1 ... done
    Recreating randocatdjango_web_1 ... done
    Attaching to randocatdjango_database_1, randocatdjango_web_1
    database_1  | 2018-06-17 18:53:09.903 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
    database_1  | 2018-06-17 18:53:09.903 UTC [1] LOG:  listening on IPv6 address "::", port 5432
    database_1  | 2018-06-17 18:53:09.907 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    database_1  | 2018-06-17 18:53:09.934 UTC [23] LOG:  database system was shut down at 2018-06-17 18:52:06 UTC
    database_1  | 2018-06-17 18:53:09.940 UTC [1] LOG:  database system is ready to accept connections
    web_1       | Performing system checks...
    web_1       |
    web_1       | System check identified no issues (0 silenced).
    web_1       |
    web_1       | You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    web_1       | Run 'python manage.py migrate' to apply them.
    web_1       | June 17, 2018 - 18:53:11
    web_1       | Django version 1.11.13, using settings 'composeexample.settings'
    web_1       | Starting development server at http://0.0.0.0:8000/
    web_1       | Quit the server with CONTROL-C.

### note: dc build web && dc up

## Randocat Django w/ Database

### dc run web python manage.py startapp randocat

    $ find randocat/
    randocat/
    randocat//migrations
    randocat//migrations/__init__.py
    randocat//models.py
    randocat//__init__.py
    randocat//apps.py
    randocat//admin.py
    randocat//tests.py
    randocat//views.py

### randocat/views.py

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Cats &gt; dogs")

#### database from container (testability, flexibility)

- add psql install to Dockerfile

    RUN apt -qq update && apt -qq install postgresql-client

    dc build && dc run --service app bash

Note lack of "-it", easier network/storage mappings

    root@3dea71452be1:/app# psql -h database -Upostgres -c 'select version()'
                                                                 version

    -------------------------------------------------------------------------------
    ---------------------------------------------------
     PostgreSQL 10.3 (Debian 10.3-1.pgdg90+1) on x86_64-pc-linux-gnu, compiled by g
    cc (Debian 6.3.0-18+deb9u1) 6.3.0 20170516, 64-bit
    (1 row)

#### access db from host (testability, flexibility, better tools)

- add port to compose
- rerun

    $ dc build && dc run --service app bash
    database uses an image, skipping
    Building app
    Step 1/6 : FROM python:3.6
     ---> c1e459c00dc3
    Step 2/6 : WORKDIR /app
     ---> Using cache
     ---> 87c3e53f617f
    Step 3/6 : EXPOSE 8080
     ---> Using cache
     ---> d530945630f3
    Step 4/6 : RUN apt -qq update && apt -qq install postgresql-client
     ---> Using cache
     ---> a42fc0a9ab4a
    Step 5/6 : COPY requirements.txt /app/
     ---> Using cache
     ---> 5e24310ce4db
    Step 6/6 : RUN pip install -qr requirements.txt
     ---> Using cache
     ---> 686e3740de1d
    Successfully built 686e3740de1d
    Successfully tagged randocat2_app:latest
    Creating network "randocat2_default" with the default driver
    Creating randocat2_database_1 ... done
    root@892ee5dcf7f5:/app#

- connect to database from host, do "create table cat" IMAGE
- insert two rows
- ? verify

    root@892ee5dcf7f5:/app# psql -hdatabase -c 'select * from cat' -Upostgres
                                         image

    -------------------------------------------------------------------------------
    -
     http://i0.kym-cdn.com/entries/icons/mobile/000/005/608/nyan-cat-01-625x450.jpg
     https://pbs.twimg.com/profile_images/796521014041706497/sP2bB10n_400x400.jpg
    (2 rows)


# XX goodies
image is just list of files
## (docker commit -- save interactive changes into new image: docker commit)
networking: use guest to operate w/ another guest

# XX sharp edges
host vs docker kernel
host vs guest networking (macos)
crashed container keeps state
unfamiliar toolset for similar ideas. hung container = 'dc down' not kill-process
host-guest editing/updates

# X practical tips

## docker kill $(docker ps -aq)
"death grip"
docker-compose gets confused
Docker gets confused too! (won't release unused port)

## (docker ps parent-image)















# OUTBOX

## hello world
image ~ package, list of files
similar: docker, brew, apt
XX list image contents
list local images // docker images

## run python
not installed, container is process
run -it bash
run -it (python)
run -it postgres bash

    # customize

    ## psql host, postgres guest
    Dbeaver
    map port

    ## db changes saves with commit
    create own image: powerful but opaque
    ? VS: SQL file

    ? run multiple versions of a database at once

    # webapp

    ## Python randocat
    Dockerfile ~ image specification
    map host drive
    map port

    ## randocat w/ database
    docker-compose

    ## goodies
    image is just list of files
    save interactive changes into new image: docker commit

    ## sharp edges
    host vs docker kernel
    host vs guest networking (macos)
    crashed container keeps state
    unfamiliar toolset for similar ideas. hung container = 'dc down' not kill-process
    host-guest editing/updates


    networking: use guest to operate w/ another guest
    ? community: apachebench
    terms/ideas
    TERMs: host, guest
    IDEA: private file system (& network)
    IDEA: image ~package, bunch of files
    IDEA: default command, override w/ bash


    ? images on DockerHub/Store
    search; stars
    probably use web first
    "official" images
    ? security concerns
    ? run ubuntu / redhat
    test packaging


## Randocat Pyramid (Docker)

- IMAGE: storage-ports across container-host
- 
    docker run -p 8080:8080 -it -v $PWD:/app randocat:1 python randocat.py

## Randocat Pyramid (Compose)

- move fiddly "docker run" bits into Compose file
- now we can build, run, and get logs in one command!
- 
    $ dc up
    Creating randocat2_app_1 ... done
    Attaching to randocat2_app_1
    app_1  | INFO:root:randocat.py now running on port 8080!

### add database

- add "database" stanza to Compose
- how do we access the database? a) in container, b) from host

# Resources

- Docker-Compose and Django https://docs.docker.com/compose/django/
