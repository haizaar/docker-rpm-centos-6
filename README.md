# docker-rpm-centos-6
Repackaged official docker-ce static builds for CentOS 6
including upstart boot script.

Recent Docker versions will only work if you've custom-upgraded
your CentOS 6 kernel to version 3.10 and above.

Build dependencies are not specified on purpose - it does not compile
anything, only downloads and repackages. Hence it should be possible to
build it anywhere, even on Ubuntu with `rpmbuild` installed.

## How to build
```
make rpm
```
