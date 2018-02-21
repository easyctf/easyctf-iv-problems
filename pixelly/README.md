# pixelly

docker and nsjail are good fun

when using docker start with `--privileged` because nsjail needs to use cgroups or something like that lmao

something needs to be fixed with the docker uid probably to get rid of the nsjail warning but idk

if you want to test haxxor without being annoying, uncomment the first eval inside `run.py` and then upload `haxxor.py`, you should get a seccomp violation

if you get a seccomp violation and want to see what syscall triggered it, uncomment the `service rsyslog start` in `Dockerfile` and look inside `/var/log/syslog` probably

idk what im doing

references in my long journey towards competence

- https://nodejs.org/en/docs/guides/nodejs-docker-webapp/
- https://offbyinfinity.com/2017/12/sandboxing-imagemagick-with-nsjail/
- https://github.com/google/kafel/blob/master/src/syscalls/amd64_syscalls.c
- https://unix.stackexchange.com/questions/395841/docker-debian-jessie-cant-find-var-log-syslog
- https://github.com/google/nsjail
- https://medium.com/@mccode/understanding-how-uid-and-gid-work-in-docker-containers-c37a01d01cf

