package io.treehopper.libraries.sensors.inertial.mpu6050;

public enum GyroScales
{
    Dps_250 (0),
    Dps_500 (1),
    Dps_1000 (2),
    Dps_2000 (3);

int val;

GyroScales(int val) { this.val = val; }
public int getVal() { return val; }
}