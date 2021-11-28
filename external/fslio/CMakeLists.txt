cmake_minimum_required(VERSION 3.15.0)
PROJECT(fslio)

# add_subdirectory(znz)

INCLUDE_DIRECTORIES(.  .. )

set(Srcs fslio.c)

add_library(fslio ${Srcs})

