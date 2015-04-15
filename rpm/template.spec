Name:           ros-hydro-rail-segmentation
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS rail_segmentation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rail_segmentation
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-pcl-conversions
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-rail-manipulation-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-roslib
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-srvs
Requires:       ros-hydro-tf
Requires:       ros-hydro-tf2
Requires:       ros-hydro-tf2-ros
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-rail-manipulation-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-tf2
BuildRequires:  ros-hydro-tf2-ros
BuildRequires:  yaml-cpp-devel

%description
Segmentation Functionality from the RAIL Lab

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Apr 15 2015 Russell Toris <rctoris@wpi.edu> - 0.1.5-0
- Autogenerated by Bloom

* Tue Apr 14 2015 Russell Toris <rctoris@wpi.edu> - 0.1.4-0
- Autogenerated by Bloom

