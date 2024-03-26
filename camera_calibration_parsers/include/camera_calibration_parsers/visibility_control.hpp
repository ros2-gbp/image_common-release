// Copyright 2018 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef CAMERA_CALIBRATION_PARSERS__VISIBILITY_CONTROL_HPP_
#define CAMERA_CALIBRATION_PARSERS__VISIBILITY_CONTROL_HPP_

#if __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define CAMERA_CALIBRATION_PARSERS_EXPORT __attribute__ ((dllexport))
    #define CAMERA_CALIBRATION_PARSERS_IMPORT __attribute__ ((dllimport))
  #else
    #define CAMERA_CALIBRATION_PARSERS_EXPORT __declspec(dllexport)
    #define CAMERA_CALIBRATION_PARSERS_IMPORT __declspec(dllimport)
  #endif
  #ifdef CAMERA_CALIBRATION_PARSERS_BUILDING_DLL
    #define CAMERA_CALIBRATION_PARSERS_PUBLIC CAMERA_CALIBRATION_PARSERS_EXPORT
  #else
    #define CAMERA_CALIBRATION_PARSERS_PUBLIC CAMERA_CALIBRATION_PARSERS_IMPORT
  #endif
  #define CAMERA_CALIBRATION_PARSERS_PUBLIC_TYPE CAMERA_CALIBRATION_PARSERS_PUBLIC
  #define CAMERA_CALIBRATION_PARSERS_LOCAL
#else
  #define CAMERA_CALIBRATION_PARSERS_EXPORT __attribute__ ((visibility("default")))
  #define CAMERA_CALIBRATION_PARSERS_IMPORT
  #if __GNUC__ >= 4
    #define CAMERA_CALIBRATION_PARSERS_PUBLIC __attribute__ ((visibility("default")))
    #define CAMERA_CALIBRATION_PARSERS_LOCAL  __attribute__ ((visibility("hidden")))
  #else
    #define CAMERA_CALIBRATION_PARSERS_PUBLIC
    #define CAMERA_CALIBRATION_PARSERS_LOCAL
  #endif
  #define CAMERA_CALIBRATION_PARSERS_PUBLIC_TYPE
#endif

#if __cplusplus
}
#endif

#endif  // CAMERA_CALIBRATION_PARSERS__VISIBILITY_CONTROL_HPP_
