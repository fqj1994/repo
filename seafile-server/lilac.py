#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

depends = ['seafile', 'ccnet', 'ccnet-server', 'libevhtp-seafile', 'libsearpc']

if __name__ == '__main__':
  single_main()
