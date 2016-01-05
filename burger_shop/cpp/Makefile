appname := test 

CXX := g++
CXXFLAGS := -Wall -g -std=gnu++11 -Wpedantic -Weffc++

srcfiles := $(shell find . -maxdepth 1 -name "*.cpp")
objects  := $(patsubst %.cpp, %.o, $(srcfiles))

all: $(appname)

$(appname): $(objects) ; $(CXX) $(CXXFLAGS) $(LDFLAGS) -o $(appname) $(objects) $(LDLIBS)

depend: .depend

.depend: $(srcfiles);  rm -f ./.depend ; $(CXX) $(CXXFLAGS) -MM $^>>./.depend;

clean: ; rm -f $(objects) $(appname)

dist-clean: clean ; rm -f *~ .depend 

include .depend
