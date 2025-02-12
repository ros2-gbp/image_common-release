%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-camera-calibration-parsers
Version:        3.1.11
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS camera_calibration_parsers package

License:        BSD
URL:            http://ros.org/wiki/camera_calibration_parsers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-rclcpp
Requires:       ros-humble-rcpputils
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-yaml-cpp-vendor
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake-ros
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rcpputils
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-yaml-cpp-vendor
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
camera_calibration_parsers contains routines for reading and writing camera
calibration parameters.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Feb 12 2025 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.11-1
- Autogenerated by Bloom

* Tue Nov 26 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.10-1
- Autogenerated by Bloom

* Tue Mar 26 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.9-1
- Autogenerated by Bloom

* Wed Jan 24 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.8-2
- Autogenerated by Bloom

* Wed Jan 24 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.8-1
- Autogenerated by Bloom

* Mon Aug 14 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.7-1
- Autogenerated by Bloom

* Thu Jul 27 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.6-1
- Autogenerated by Bloom

* Wed Nov 16 2022 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.5-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.4-2
- Autogenerated by Bloom

* Fri Mar 25 2022 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.4-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.3-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.2-2
- Autogenerated by Bloom

