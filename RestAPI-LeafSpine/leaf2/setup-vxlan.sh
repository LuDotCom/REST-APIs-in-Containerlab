#!/bin/bash

ip link add br1 type bridge
ip link set dev br1 up
ip link add br2 type bridge
ip link set dev br2 up
ip link add vxlan10 type vxlan id 10 dstport 4789
ip link add vxlan20 type vxlan id 20 dstport 4789
ip link set dev vxlan10 up
ip link set dev vxlan20 up
ip link set vxlan10 master br1
ip link set vxlan20 master br2
ip link set eth2 master br1
ip link set eth3 master br2
