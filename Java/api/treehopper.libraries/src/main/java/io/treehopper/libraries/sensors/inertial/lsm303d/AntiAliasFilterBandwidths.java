/// This file was auto-generated by RegisterGenerator. Any changes to it will be overwritten!
package io.treehopper.libraries.sensors.inertial.lsm303d;

 enum AntiAliasFilterBandwidths
{
    Hz_773 (0),
    Hz_194 (1),
    Hz_362 (2),
    Hz_50 (3);

int val;

AntiAliasFilterBandwidths(int val) { this.val = val; }
public int getVal() { return val; }
}
