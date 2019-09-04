
ARCH = x86_64
DOCKER_VERSION = 19.03.2
RPM_RELEASE = 1

BUILDDIR = $(CURDIR)/build
TARBALL = docker-$(DOCKER_VERSION).tgz
TARBALLPATH = $(BUILDDIR)/$(TARBALL)
RPMPATH=$(BUILDDIR)/RPMS/$(ARCH)/docker-$(DOCKER_VERSION)-$(RPM_RELEASE).$(ARCH).rpm

SPEC_FILE = docker.spec
RPMBUILD = /usr/bin/rpmbuild

rpm: $(RPMPATH)
tarball: $(TARBALLPATH)

$(TARBALLPATH):
	mkdir -p $(BUILDDIR)
	wget -O $(TARBALLPATH) https://download.docker.com/linux/static/stable/$(ARCH)/$(TARBALL)

$(RPMPATH): $(TARBALLPATH) docker.spec dockerd.default dockerd.conf.upstart
	$(RPMBUILD) -bb $(SPEC_FILE) \
		--buildroot=$(BUILDDIR)/rpmbuild \
		--define "_tarball $(TARBALLPATH)" \
		--define "_version $(DOCKER_VERSION)" \
		--define "_release $(RPM_RELEASE)" \
        --define "_sourcedir $(CURDIR)" \
        --define "_rpmdir $(BUILDDIR)/RPMS" \
        --define "_tmppath $(BUILDDIR)/tmp"
	@echo -e "\n\nGrab your RPM from:\n$(RPMPATH)"

.PHONY: clean
clean:
	rm -rf $(BUILDDIR)
