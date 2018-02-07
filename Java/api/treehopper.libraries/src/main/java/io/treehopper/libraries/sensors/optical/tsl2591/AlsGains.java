package io.treehopper.libraries.sensors.optical.tsl2591;

public enum AlsGains
{
    Low (0),
    Medium (1),
    High (2),
    Max (3);

int val;

AlsGains(int val) { this.val = val; }
public int getVal() { return val; }
}
