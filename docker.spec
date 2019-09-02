Name: docker
Version: %{_version}
Release: %{_release}%{?dist}
Source0: engine.tgz
Source1: docker.service
Source2: docker.socket
Summary: The open-source application container engine
Group: Tools/Docker
License: ASL 2.0
URL: https://www.docker.com
Vendor: Docker
Packager: Zaar Hai <haizaar@haizaar.com>

Requires: iptables
Requires: libcgroup
Requires: tar
Requires: xz
Requires: device-mapper-libs >= 1.02.90-1
Requires: bash

%description
Docker is a product for you to build, ship and run any application as a
lightweight container.

Docker containers are both hardware-agnostic and platform-agnostic. This means
they can run anywhere, from your laptop to the largest cloud compute instance and
everything in between - and they don't require you to use a particular
language, framework or packaging system. That makes them great building blocks
for deploying and scaling web apps, databases, and backend services without
depending on a particular stack or provider.

NOTE: This package includes docker CLI command as well.

%install
install -d -m 0755 $RPM_BUILD_ROOT/%{_bindir}
tar -xv -f %{_tarball} --strip-components=1 -C $RPM_BUILD_ROOT/%{_bindir}

# install init scripts and configuration
install -D -m 0644 %{_sourcedir}/dockerd.default $RPM_BUILD_ROOT/etc/default/dockerd
install -d -m 0700 -o root -g root /etc/docker
install -D -m 0644 %{_sourcedir}/daemon.json $RPM_BUILD_ROOT/etc/docker/daemon.json
install -D -m 0644 %{_sourcedir}/dockerd.conf.upstart $RPM_BUILD_ROOT/etc/init/dockerd.conf

%files
/%{_bindir}/*
/etc/*

%post
if ! getent group docker > /dev/null; then
    groupadd --system docker || [[ "9" == "$?" ]]  # Already exists
    useradd --system --no-user-group --no-create-home --groups docker docker || [[ "9" == "$?" ]]  # Already exists
fi

%changelog
