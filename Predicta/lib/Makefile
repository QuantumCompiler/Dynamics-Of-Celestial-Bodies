CXX = g++

# Detect OS
UNAME_S := $(shell uname -s)

# Python paths - with error handling
PYTHON_CONFIG := $(shell which python3-config 2>/dev/null)
ifeq ($(PYTHON_CONFIG),)
    # Fallback: try to find Python include and lib paths manually
    PYTHON_VERSION := $(shell python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null)
    PYTHON_INCLUDE := $(shell python3 -c "import sysconfig; print(sysconfig.get_path('include'))" 2>/dev/null)
    PYTHON_LIBDIR := $(shell python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))" 2>/dev/null)
    PYTHON_CFLAGS := -I$(PYTHON_INCLUDE)
    PYTHON_LDFLAGS := -L$(PYTHON_LIBDIR) -lpython$(PYTHON_VERSION)
else
    PYTHON_CFLAGS := $(shell $(PYTHON_CONFIG) --cflags)
    PYTHON_LDFLAGS := $(shell $(PYTHON_CONFIG) --ldflags --embed 2>/dev/null || $(PYTHON_CONFIG) --ldflags)
endif

# Numpy include - with error handling
NUMPY_INCLUDE := $(shell python3 -c "import numpy; print(numpy.get_include())" 2>/dev/null)
ifeq ($(NUMPY_INCLUDE),)
    NUMPY_INCLUDE := 
endif

# LibTorch paths - support both macOS (Homebrew) and Linux
ifeq ($(UNAME_S),Darwin)
    LIBTORCH_PREFIX ?= /opt/homebrew/opt/pytorch
    JSON_INCLUDE ?= /opt/homebrew/opt/nlohmann-json/include
    CXX11_ABI ?= 0
else
    # Linux paths - adjust these to your LibTorch installation
    LIBTORCH_PREFIX ?= /usr/local/libtorch
    JSON_INCLUDE ?= /usr/include/nlohmann
    CXX11_ABI ?= 1
endif

LIBTORCH_INCLUDE = $(LIBTORCH_PREFIX)/include
LIBTORCH_LIB = $(LIBTORCH_PREFIX)/lib

# Compiler flags
CXXFLAGS = -std=c++17 -w \
	-I./matplotlib-cpp \
	-I$(LIBTORCH_INCLUDE) \
	-I$(LIBTORCH_INCLUDE)/torch/csrc/api/include \
	-I$(JSON_INCLUDE) \
	$(if $(NUMPY_INCLUDE),-I$(NUMPY_INCLUDE)) \
	$(PYTHON_CFLAGS) \
	-DWITHOUT_NUMPY \
	-D_GLIBCXX_USE_CXX11_ABI=$(CXX11_ABI)

# Linker flags
LDFLAGS = $(PYTHON_LDFLAGS) \
	-L$(LIBTORCH_LIB) \
	-ltorch \
	-ltorch_cpu \
	-lc10 \
	-Wl,-rpath,$(LIBTORCH_LIB)

TARGET = build/main
SOURCES = main.cpp celestial_bodies.cpp models.cpp rk4.cpp solvers.cpp predicta.cpp utilities.cpp plotters.cpp machine_learning.cpp single_body_torch.cpp
OBJECTS = $(SOURCES:%.cpp=build/%.o)

all: $(TARGET)

$(TARGET): $(OBJECTS) | build
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

build/%.o: %.cpp | build
	$(CXX) $(CXXFLAGS) -c $< -o $@

build:
	mkdir -p build

execute: clean all
	cd build && ./main

clean:
	rm -rf build/*.o
	rm -rf build/main

clean_results:
	rm -rf build/results

nuke:
	rm -rf build

run:
	cd build &&	./main

.PHONY: all clean execute run