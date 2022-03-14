# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix

pkgname=strawberry-full-git
pkgver=1.0.2.r8.gd40a67ce
pkgrel=1
pkgdesc="A music player aimed at audio enthusiasts and music collectors, all options and engines"
arch=(x86_64)
url="https://www.strawberrymusicplayer.org/"
license=(GPL3)
depends=(chromaprint protobuf gst-plugins-base gst-plugins-good
         qt5-x11extras sqlite3 udisks2 dbus alsa-lib fftw
         libcdio vlc libgpod
         libpulse  libmtp  libusbmuxd libplist libimobiledevice)
makedepends=(git cmake boost qt5-tools gtest gmock)
optdepends=('gst-libav: additional codecs (i.e. AAC)'
            'gst-plugins-bad: additional codecs (i.e. AAC)'
            'gst-plugins-ugly: additional codecs')
provides=(strawberry)
conflicts=(strawberry)
source=("git+https://github.com/jonaski/strawberry.git")
sha256sums=('SKIP')

pkgver() {
  cd "${pkgname/-full-git/}"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "${pkgname/-full-git/}"
  install -d strawberry-build
}

build() {
  cd "${pkgname/-full-git/}/strawberry-build"
  cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_WITH_QT5=ON

  make
}

package() {
  cd "${pkgname/-full-git/}/strawberry-build"
  make DESTDIR="${pkgdir}" install
}
