# Easy Docker



THEME: single artifact re-use btw Dev, QA,and Prod: no surprises

## 1. BASICS: Docker ~ run package in self-contained unit
separate file system
separate networking

## docker run -it python:3.6
download package, use it to create a process
not installed, container is process
image ~ package, list of files (link)
    images are versioned like packages
options: interactive, terminal

## Node // docker run -it bitnami/node
https://hub.docker.com/r/bitnami/node/

## image can be tiny or huge
docker run ubuntu / redhat
single-use container, e.g. Apache Benchmark
docker run --rm jordi/ab -v 2 https://www.docker.com/

## great for temporary tools
docker-apache-benchmark

## image ~ package
list local images // docker images
search in dockerhub // docker search hello --limit 5

# 2. CUSTOMIZE
THEME: customize standard tool/service
## docker run  -e POSTGRES_PASSWORD=beer -p 5432:5432 postgres:9.6.5
Dbeaver
'out of beer' => error in console
## ? map port, containers have private fs in addition to network

## TBD db changes saves with commit ; create own image: powerful but opaque
? VS: SQL file
TBD multiple Mongo versions (awkward => trivial)

# 3. WEBAPP

## Python randocat
Dockerfile ~ image specification
map host drive
map port
webapp w/ database
docker-compose
randocat w/ database

# XX goodies
image is just list of files
save interactive changes into new image: docker commit
networking: use guest to operate w/ another guest
? community: apachebench

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
















# simple use cases

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
