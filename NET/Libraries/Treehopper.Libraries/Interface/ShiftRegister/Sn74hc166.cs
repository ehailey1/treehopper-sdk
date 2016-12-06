﻿using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using Treehopper;

namespace Treehopper.Libraries.Interface.ShiftRegister
{
    /// <summary>
    /// 74HC166-series shift input register
    /// </summary>
    public class Sn74hc166
    {
        /// <summary>
        /// Collection of pins
        /// </summary>
        public Collection<DigitalInPin> Pins { get; set; } = new Collection<DigitalInPin>();

        /// <summary>
        /// Construct a new instance of the Sn74hc166
        /// </summary>
        /// <param name="spiModule">SPI module to use</param>
        /// <param name="loadPin">latch pin</param>
        public Sn74hc166(Spi spiModule, DigitalOutPin loadPin)
        {
            loadPin.MakeDigitalPushPullOut();
            spiModule.Enabled = true;
        }
    }
}
