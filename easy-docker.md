# Easy Docker
















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
