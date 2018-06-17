# Easy Docker


# Questions

# X. WHY

THEME: single artifact re-use btw Dev, QA,and Prod: no surprises
- easily run from scratch (Credstore this week!)


# 1. BASICS: Docker ~ run package in self-contained unit

*IDEAS*
image ~ package, list of files
container
- separate file system
- separate networking
download package, use it to create a process
not installed, container is *process*

## docker run -it python:3.6

options: interactive, terminal

? Clean up (--rm)
By default a container’s file system persists even after the container exits. This makes debugging a lot easier (since you can inspect the final state) and you retain all your data by default. But if you are running short-term foreground processes, these container file systems can really pile up. If instead you’d like Docker to automatically clean up the container and remove the file system when the container exits, you can add the --rm flag:


## DIAGRAM: computer, computer+VM, computer+containers

## docker run -it bitnami/node

    $ docker run -it bitnami/node:8
    
    > console.log('beer')
    beer
    undefined


single-use container, e.g. Apache Benchmark

$ docker run --rm jordi/ab -v 2 https://www.docker.com/


## great for temporary tools
$ docker run --rm jordi/ab https://www.docker.com/
just try something

$ docker run -it --rm mbentley/figlet holy ship!
Unable to find image 'mbentley/figlet:latest' locally
latest: Pulling from mbentley/figlet
c52e3ed763ff: Pull complete
bb9a365b28e8: Pull complete
bbe1c9f335a7: Pull complete
a3ed95caeb02: Pull complete
Digest: sha256:9545f0a713bf48a192ad522c739fa458a41786c72517d183fb777b9ba23f1593
Status: Downloaded newer image for mbentley/figlet:latest
 _           _             _     _       _
| |__   ___ | |_   _   ___| |__ (_)_ __ | |
| '_ \ / _ \| | | | | / __| '_ \| | '_ \| |
| | | | (_) | | |_| | \__ \ | | | | |_) |_|
|_| |_|\___/|_|\__, | |___/_| |_|_| .__/(_)
               |___/              |_|

## image ~ package

### list local images // docker images

### search in dockerhub // docker search hello --limit 5

### image > package

- really awkward to install specific version (Node)
- only one at a time

## OUTBOX

    images are versioned like packages
    ALWAYS version your packages, and containers!
    ? compare w/ "brew install node@8" -- very awkward!

    ## image can be tiny or huge

        $ docker run ubuntu:18.04 du -sh
        75M .

    ## this is odd, as the 18.04 compressed ISO is almost 2GB!
    - _minimal_ image with only 94 packages installed


# 2. CUSTOMIZE
THEME: customize standard tool/service

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

## TBD db changes saves with commit ; create own image: powerful but opaque
? VS: SQL file

# 3. WEBAPP

*Ideas*
(Dockerfile = image specification)
Randocat
- map host drive
randocat w/ database
- docker-compose = cluster specification

## Python randocat

    docker run -p 8080:8080 -it -v $PWD:/app randocat:1 python randocat.py

## Randocat w/ Database



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
