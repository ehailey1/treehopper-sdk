﻿namespace Treehopper
{
    /// <summary>
    ///     An enumeration representing the different supported modes of this pin.
    /// </summary>
    public enum PinMode
    {
        /// <summary>
        ///     Pin is reserved for other use
        /// </summary>
        Reserved,

        /// <summary>
        ///     Pin is a digital input
        /// </summary>
        DigitalInput,

        /// <summary>
        ///     Pin is a push-pull output
        /// </summary>
        PushPullOutput,

        /// <summary>
        ///     Pin is an open-drain output (with a weak internal pull-up)
        /// </summary>
        OpenDrainOutput,

        /// <summary>
        ///     Pin is an analog input
        /// </summary>
        AnalogInput,

        /// <summary>
        ///     Pin is a SoftPWM output
        /// </summary>
        SoftPwm,

        /// <summary>
        ///     Pin is unassigned
        /// </summary>
        Unassigned
    }
}