FROM ubuntu:22.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install ubuntu-dbgsym-keyring
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gdb binutils less moreutils expect git python3 ruby bc bzip2 curl gcc busybox file gettext bsdmainutils bind9-host systemd net-tools jq psmisc kmod landscape-common login lsb-release util-linux make wget
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y debuginfod openbox
RUN wget -O c.zip https://github.com/rpetrich/callander/releases/download/v0.3/callander-x86_64.zip && \
unzip c.zip && tar xfz callander-x86_64-*.tgz && mv callander callander.debug /bin/
COPY hello-world/cprog hello-world/asm /bin/
ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com"
