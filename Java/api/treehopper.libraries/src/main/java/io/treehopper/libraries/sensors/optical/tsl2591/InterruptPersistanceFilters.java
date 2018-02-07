package io.treehopper.libraries.sensors.optical.tsl2591;

public enum InterruptPersistanceFilters
{
    EveryAlsCycle (0),
    AnyValueOutsideThreshold (1),
    Consecutive_2 (2),
    Consecutive_3 (3),
    Consecutive_5 (4),
    Consecutive_10 (5),
    Consecutive_15 (6),
    Consecutive_20 (7),
    Consecutive_25 (8),
    Consecutive_30 (9),
    Consecutive_35 (10),
    Consecutive_40 (11),
    Consecutive_45 (12),
    Consecutive_50 (13),
    Consecutive_55 (14),
    Consecutive_60 (15);

int val;

InterruptPersistanceFilters(int val) { this.val = val; }
public int getVal() { return val; }
}
