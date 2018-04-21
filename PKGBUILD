# Script generated with Bloom
pkgdesc="ROS - Package to programmatically spawn message, service, and action relays. To add support for a message/service dependency, please add to the build dependencies in package.xml and CMakeLists.txt"


pkgname='ros-kinetic-message-relay'
pkgver='0.0.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-cheetah'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-controller-manager-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-gazebo-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-map-msgs'
'ros-kinetic-move-base-msgs'
'ros-kinetic-multimaster-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-robot-localization'
'ros-kinetic-roscpp'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-roslaunch'
'ros-kinetic-roslint'
'ros-kinetic-sensor-msgs'
'ros-kinetic-shape-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf2-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-actionlib-msgs'
'ros-kinetic-controller-manager-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-gazebo-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-map-msgs'
'ros-kinetic-move-base-msgs'
'ros-kinetic-multimaster-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-robot-localization'
'ros-kinetic-roscpp'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-sensor-msgs'
'ros-kinetic-shape-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf2-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=message_relay
source=()
md5sums=()

prepare() {
    cp -R $startdir/message_relay $srcdir/message_relay
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

