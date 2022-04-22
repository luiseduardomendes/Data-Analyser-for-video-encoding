# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


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

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/usr/bin/cmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "No interactive CMake dialog available..."
	/usr/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /home/luispmendes/Data-Analyser-for-video-encoding/CMakeFiles /home/luispmendes/Data-Analyser-for-video-encoding/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /home/luispmendes/Data-Analyser-for-video-encoding/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named CommonLib

# Build rule for target.
CommonLib: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 CommonLib
.PHONY : CommonLib

# fast build rule for target.
CommonLib/fast:
	$(MAKE) -f source/Lib/CommonLib/CMakeFiles/CommonLib.dir/build.make source/Lib/CommonLib/CMakeFiles/CommonLib.dir/build
.PHONY : CommonLib/fast

#=============================================================================
# Target rules for targets named CommonAnalyserLib

# Build rule for target.
CommonAnalyserLib: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 CommonAnalyserLib
.PHONY : CommonAnalyserLib

# fast build rule for target.
CommonAnalyserLib/fast:
	$(MAKE) -f source/Lib/CommonAnalyserLib/CMakeFiles/CommonAnalyserLib.dir/build.make source/Lib/CommonAnalyserLib/CMakeFiles/CommonAnalyserLib.dir/build
.PHONY : CommonAnalyserLib/fast

#=============================================================================
# Target rules for targets named DecoderAnalyserLib

# Build rule for target.
DecoderAnalyserLib: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 DecoderAnalyserLib
.PHONY : DecoderAnalyserLib

# fast build rule for target.
DecoderAnalyserLib/fast:
	$(MAKE) -f source/Lib/DecoderAnalyserLib/CMakeFiles/DecoderAnalyserLib.dir/build.make source/Lib/DecoderAnalyserLib/CMakeFiles/DecoderAnalyserLib.dir/build
.PHONY : DecoderAnalyserLib/fast

#=============================================================================
# Target rules for targets named DecoderLib

# Build rule for target.
DecoderLib: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 DecoderLib
.PHONY : DecoderLib

# fast build rule for target.
DecoderLib/fast:
	$(MAKE) -f source/Lib/DecoderLib/CMakeFiles/DecoderLib.dir/build.make source/Lib/DecoderLib/CMakeFiles/DecoderLib.dir/build
.PHONY : DecoderLib/fast

#=============================================================================
# Target rules for targets named EncoderLib

# Build rule for target.
EncoderLib: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 EncoderLib
.PHONY : EncoderLib

# fast build rule for target.
EncoderLib/fast:
	$(MAKE) -f source/Lib/EncoderLib/CMakeFiles/EncoderLib.dir/build.make source/Lib/EncoderLib/CMakeFiles/EncoderLib.dir/build
.PHONY : EncoderLib/fast

#=============================================================================
# Target rules for targets named Utilities

# Build rule for target.
Utilities: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 Utilities
.PHONY : Utilities

# fast build rule for target.
Utilities/fast:
	$(MAKE) -f source/Lib/Utilities/CMakeFiles/Utilities.dir/build.make source/Lib/Utilities/CMakeFiles/Utilities.dir/build
.PHONY : Utilities/fast

#=============================================================================
# Target rules for targets named DecoderAnalyserApp

# Build rule for target.
DecoderAnalyserApp: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 DecoderAnalyserApp
.PHONY : DecoderAnalyserApp

# fast build rule for target.
DecoderAnalyserApp/fast:
	$(MAKE) -f source/App/DecoderAnalyserApp/CMakeFiles/DecoderAnalyserApp.dir/build.make source/App/DecoderAnalyserApp/CMakeFiles/DecoderAnalyserApp.dir/build
.PHONY : DecoderAnalyserApp/fast

#=============================================================================
# Target rules for targets named DecoderApp

# Build rule for target.
DecoderApp: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 DecoderApp
.PHONY : DecoderApp

# fast build rule for target.
DecoderApp/fast:
	$(MAKE) -f source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build.make source/App/DecoderApp/CMakeFiles/DecoderApp.dir/build
.PHONY : DecoderApp/fast

#=============================================================================
# Target rules for targets named EncoderApp

# Build rule for target.
EncoderApp: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 EncoderApp
.PHONY : EncoderApp

# fast build rule for target.
EncoderApp/fast:
	$(MAKE) -f source/App/EncoderApp/CMakeFiles/EncoderApp.dir/build.make source/App/EncoderApp/CMakeFiles/EncoderApp.dir/build
.PHONY : EncoderApp/fast

#=============================================================================
# Target rules for targets named SEIRemovalApp

# Build rule for target.
SEIRemovalApp: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 SEIRemovalApp
.PHONY : SEIRemovalApp

# fast build rule for target.
SEIRemovalApp/fast:
	$(MAKE) -f source/App/SEIRemovalApp/CMakeFiles/SEIRemovalApp.dir/build.make source/App/SEIRemovalApp/CMakeFiles/SEIRemovalApp.dir/build
.PHONY : SEIRemovalApp/fast

#=============================================================================
# Target rules for targets named parcat

# Build rule for target.
parcat: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 parcat
.PHONY : parcat

# fast build rule for target.
parcat/fast:
	$(MAKE) -f source/App/Parcat/CMakeFiles/parcat.dir/build.make source/App/Parcat/CMakeFiles/parcat.dir/build
.PHONY : parcat/fast

#=============================================================================
# Target rules for targets named StreamMergeApp

# Build rule for target.
StreamMergeApp: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 StreamMergeApp
.PHONY : StreamMergeApp

# fast build rule for target.
StreamMergeApp/fast:
	$(MAKE) -f source/App/StreamMergeApp/CMakeFiles/StreamMergeApp.dir/build.make source/App/StreamMergeApp/CMakeFiles/StreamMergeApp.dir/build
.PHONY : StreamMergeApp/fast

#=============================================================================
# Target rules for targets named BitstreamExtractorApp

# Build rule for target.
BitstreamExtractorApp: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 BitstreamExtractorApp
.PHONY : BitstreamExtractorApp

# fast build rule for target.
BitstreamExtractorApp/fast:
	$(MAKE) -f source/App/BitstreamExtractorApp/CMakeFiles/BitstreamExtractorApp.dir/build.make source/App/BitstreamExtractorApp/CMakeFiles/BitstreamExtractorApp.dir/build
.PHONY : BitstreamExtractorApp/fast

#=============================================================================
# Target rules for targets named SubpicMergeApp

# Build rule for target.
SubpicMergeApp: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 SubpicMergeApp
.PHONY : SubpicMergeApp

# fast build rule for target.
SubpicMergeApp/fast:
	$(MAKE) -f source/App/SubpicMergeApp/CMakeFiles/SubpicMergeApp.dir/build.make source/App/SubpicMergeApp/CMakeFiles/SubpicMergeApp.dir/build
.PHONY : SubpicMergeApp/fast

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... rebuild_cache"
	@echo "... edit_cache"
	@echo "... CommonLib"
	@echo "... CommonAnalyserLib"
	@echo "... DecoderAnalyserLib"
	@echo "... DecoderLib"
	@echo "... EncoderLib"
	@echo "... Utilities"
	@echo "... DecoderAnalyserApp"
	@echo "... DecoderApp"
	@echo "... EncoderApp"
	@echo "... SEIRemovalApp"
	@echo "... parcat"
	@echo "... StreamMergeApp"
	@echo "... BitstreamExtractorApp"
	@echo "... SubpicMergeApp"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system
