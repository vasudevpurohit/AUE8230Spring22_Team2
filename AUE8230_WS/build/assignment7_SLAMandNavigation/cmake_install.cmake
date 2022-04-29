# Install script for directory: /home/vasudev/Desktop/AUE8230Spring22_Team2/AUE8230Spring22_Team2/AUE8230_WS/src/assignment7_SLAMandNavigation

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/vasudev/Desktop/AUE8230Spring22_Team2/AUE8230Spring22_Team2/AUE8230_WS/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/vasudev/Desktop/AUE8230Spring22_Team2/AUE8230Spring22_Team2/AUE8230_WS/build/assignment7_SLAMandNavigation/catkin_generated/installspace/assignment7_SLAMandNavigation.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/assignment7_SLAMandNavigation/cmake" TYPE FILE FILES
    "/home/vasudev/Desktop/AUE8230Spring22_Team2/AUE8230Spring22_Team2/AUE8230_WS/build/assignment7_SLAMandNavigation/catkin_generated/installspace/assignment7_SLAMandNavigationConfig.cmake"
    "/home/vasudev/Desktop/AUE8230Spring22_Team2/AUE8230Spring22_Team2/AUE8230_WS/build/assignment7_SLAMandNavigation/catkin_generated/installspace/assignment7_SLAMandNavigationConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/assignment7_SLAMandNavigation" TYPE FILE FILES "/home/vasudev/Desktop/AUE8230Spring22_Team2/AUE8230Spring22_Team2/AUE8230_WS/src/assignment7_SLAMandNavigation/package.xml")
endif()

