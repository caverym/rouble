pkgname=rouble-git
pkgver=0.0.1
pkgrel=1
pkgdesc="Rouble dictionary"
arch=('any')
url="https://github.com/caverym/rouble"
depends=('python')
binname=rouble

source=("git+https://github.com/caverym/rouble.git")
sha256sums=('SKIP')

pkgver() {
	cd rouble
	git describe --long --targs | sed 's/\([^-]*-g\)/r\1;s/-/./g'
}

build() {
	cd rouble
	git submodule init
	make
}

package() {
	cd rouble
	install -Dm 744 english-words/words_alpha.txt "${pkgdir}/usr/share/rouble/words"
	install -Dm 755 rouble "${pkgdir}/usr/bin/rouble"
}
