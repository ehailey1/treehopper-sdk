/// This file was auto-generated by RegisterGenerator. Any changes to it will be overwritten!
package io.treehopper.libraries.sensors.inertial.lsm303d;

 enum FifoModes
{
    Bypass (0),
    Fifo (1),
    Stream (2),
    StreamToFifo (3),
    BypassToStream (4);

int val;

FifoModes(int val) { this.val = val; }
public int getVal() { return val; }
}
