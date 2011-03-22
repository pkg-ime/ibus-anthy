#!/bin/sh
set -e
set -x

autopoint --force || exit 1
libtoolize --automake --copy --force || exit 1
intltoolize --copy --force || exit 1
aclocal -I m4 --force || exit 1
autoheader --force || exit 1
automake --add-missing --copy --force || exit 1
autoconf --force || exit 1
export CFLAGS="-Wall -g -O0 -Wl,--no-undefined"
export CXXFLAGS="$CFLAGS"
./configure --enable-maintainer-mode $* || exit 1
