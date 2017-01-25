Name:           ros-kinetic-message-relay
Version:        0.0.1
Release:        0%{?dist}
Summary:        ROS message_relay package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-controller-manager-msgs
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-gazebo-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-map-msgs
Requires:       ros-kinetic-move-base-msgs
Requires:       ros-kinetic-multimaster-msgs
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-robot-localization
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosgraph-msgs
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-shape-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-stereo-msgs
Requires:       ros-kinetic-tf2-msgs
Requires:       ros-kinetic-trajectory-msgs
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  python-cheetah
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-manager-msgs
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-gazebo-msgs
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-map-msgs
BuildRequires:  ros-kinetic-move-base-msgs
BuildRequires:  ros-kinetic-multimaster-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-robot-localization
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rosgraph-msgs
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-shape-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-stereo-msgs
BuildRequires:  ros-kinetic-tf2-msgs
BuildRequires:  ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-visualization-msgs

%description
Package to programmatically spawn message, service, and action relays. To add
support for a message/service dependency, please add to the build dependencies
in package.xml and CMakeLists.txt

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Jan 25 2017 Paul Bovbel <pbovbel@clearpath.ai> - 0.0.1-0
- Autogenerated by Bloom

