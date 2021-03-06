﻿namespace Treehopper
{
    /// <summary>
    ///     Select the reference to use for the analog input of the pin
    /// </summary>
    public enum AdcReferenceLevel
    {
        /// <summary>
        ///     3.3V rail generated by on-board LDO, rated at 1.5% accuracy.
        /// </summary>
        Vref_3V3,

        /// <summary>
        ///     1.65V reference rated at 1.8% accuracy.
        /// </summary>
        Vref_1V65,

        /// <summary>
        ///     1.85V reference. Accuracy TBD.
        /// </summary>
        Vref_1V85,

        /// <summary>
        ///     2.4V reference rated at 2.1% accuracy.
        /// </summary>
        Vref_2V4,

        /// <summary>
        ///     3.3V supply derived from the 1.65V reference rated at 3.6% accuracy.
        /// </summary>
        Vref_3V3Derived,

        /// <summary>
        ///     3.7V reference derived from the 1.85V LDO. Accuracy TBD.
        /// </summary>
        Vref_3V7
    }
}