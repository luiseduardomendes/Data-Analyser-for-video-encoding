# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/luispmendes/VVCSoftware_VTM

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/luispmendes/Data-Analyser-for-video-encoding

# Include any dependencies generated for this target.
include source/App/EncoderApp/CMakeFiles/EncoderApp.dir/depend.make

# Include the progress variables for this target.
include source/App/EncoderApp/CMakeFiles/EncoderApp.dir/progress.make

# Include the compile flags for this target's objects.
include source/App/EncoderApp/CMakeFiles/EncoderApp.dir/flags.make

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncApp.cpp.o: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/flags.make
source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncApp.cpp.o: /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncApp.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/luispmendes/Data-Analyser-for-video-encoding/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncApp.cpp.o"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/EncoderApp.dir/EncApp.cpp.o -c /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncApp.cpp

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncApp.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/EncoderApp.dir/EncApp.cpp.i"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncApp.cpp > CMakeFiles/EncoderApp.dir/EncApp.cpp.i

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncApp.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/EncoderApp.dir/EncApp.cpp.s"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncApp.cpp -o CMakeFiles/EncoderApp.dir/EncApp.cpp.s

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.o: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/flags.make
source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.o: /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncAppCfg.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/luispmendes/Data-Analyser-for-video-encoding/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.o"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.o -c /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncAppCfg.cpp

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.i"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncAppCfg.cpp > CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.i

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.s"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/EncAppCfg.cpp -o CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.s

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/encmain.cpp.o: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/flags.make
source/App/EncoderApp/CMakeFiles/EncoderApp.dir/encmain.cpp.o: /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/encmain.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/luispmendes/Data-Analyser-for-video-encoding/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object source/App/EncoderApp/CMakeFiles/EncoderApp.dir/encmain.cpp.o"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/EncoderApp.dir/encmain.cpp.o -c /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/encmain.cpp

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/encmain.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/EncoderApp.dir/encmain.cpp.i"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/encmain.cpp > CMakeFiles/EncoderApp.dir/encmain.cpp.i

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/encmain.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/EncoderApp.dir/encmain.cpp.s"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp/encmain.cpp -o CMakeFiles/EncoderApp.dir/encmain.cpp.s

# Object files for target EncoderApp
EncoderApp_OBJECTS = \
"CMakeFiles/EncoderApp.dir/EncApp.cpp.o" \
"CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.o" \
"CMakeFiles/EncoderApp.dir/encmain.cpp.o"

# External object files for target EncoderApp
EncoderApp_EXTERNAL_OBJECTS =

/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncApp.cpp.o
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/EncAppCfg.cpp.o
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/encmain.cpp.o
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/build.make
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: /home/luispmendes/VVCSoftware_VTM/lib/umake/gcc-9.4/x86_64/release/libCommonLib.a
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: /home/luispmendes/VVCSoftware_VTM/lib/umake/gcc-9.4/x86_64/release/libEncoderLib.a
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: /home/luispmendes/VVCSoftware_VTM/lib/umake/gcc-9.4/x86_64/release/libDecoderLib.a
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: /home/luispmendes/VVCSoftware_VTM/lib/umake/gcc-9.4/x86_64/release/libUtilities.a
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: /home/luispmendes/VVCSoftware_VTM/lib/umake/gcc-9.4/x86_64/release/libCommonLib.a
/home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp: source/App/EncoderApp/CMakeFiles/EncoderApp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/luispmendes/Data-Analyser-for-video-encoding/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable /home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp"
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/EncoderApp.dir/link.txt --verbose=$(VERBOSE)
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && /usr/bin/cmake -E copy  /home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp    /home/luispmendes/VVCSoftware_VTM/bin/EncoderAppStatic  

# Rule to build all files generated by this target.
source/App/EncoderApp/CMakeFiles/EncoderApp.dir/build: /home/luispmendes/VVCSoftware_VTM/bin/umake/gcc-9.4/x86_64/release/EncoderApp

.PHONY : source/App/EncoderApp/CMakeFiles/EncoderApp.dir/build

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/clean:
	cd /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp && $(CMAKE_COMMAND) -P CMakeFiles/EncoderApp.dir/cmake_clean.cmake
.PHONY : source/App/EncoderApp/CMakeFiles/EncoderApp.dir/clean

source/App/EncoderApp/CMakeFiles/EncoderApp.dir/depend:
	cd /home/luispmendes/Data-Analyser-for-video-encoding && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/luispmendes/VVCSoftware_VTM /home/luispmendes/VVCSoftware_VTM/source/App/EncoderApp /home/luispmendes/Data-Analyser-for-video-encoding /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp /home/luispmendes/Data-Analyser-for-video-encoding/source/App/EncoderApp/CMakeFiles/EncoderApp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : source/App/EncoderApp/CMakeFiles/EncoderApp.dir/depend

