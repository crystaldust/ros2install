#!/bin/bash
ROSPATH=$HOME/ros/$ROS_DISTRO
echo $ROSPATH
mkdir -p $ROSPATH/src
mkdir -p $ROSPATH/install
touch $ROSPATH/install/setup.bash
echo 'export ROSPATH=$HOME/ros/$ROS_DISTRO' >> $HOME/.bashrc
echo 'source $ROSPATH/install/setup.bash' >> $HOME/.bashrc

