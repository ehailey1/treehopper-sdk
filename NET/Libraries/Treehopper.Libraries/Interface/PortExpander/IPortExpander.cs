﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Treehopper.Libraries.Sensors;

namespace Treehopper.Libraries.Interface.PortExpander
{
    /// <summary>
    /// A port expander
    /// </summary>
    /// <typeparam name="TPortExpanderPin">The port expander's pin type</typeparam>
    public interface IPortExpander<TPortExpanderPin> : IFlushableOutputPort<TPortExpanderPin> where TPortExpanderPin : IPortExpanderPin
    {
    }

    /// <summary>
    /// Parent port expander type. Separated from IPortExpander to eliminate circular references
    /// </summary>
    public interface IPortExpanderParent : IPollable
    {
        /// <summary>
        /// Called by a port expander pin when its value needs to be updated
        /// </summary>
        /// <param name="portExpanderPin">The port expander pin to update</param>
        void OutputValueChanged(IPortExpanderPin portExpanderPin);

        /// <summary>
        /// Called by a port expander pin when its value needs to be updated
        /// </summary>
        /// <param name="portExpanderPin"></param>
        void OutputModeChanged(IPortExpanderPin portExpanderPin);

        /// <summary>
        /// Gets or sets the polling period used when AwaitDigitalValueChanged() is used by the port expander
        /// </summary>
        int AwaitPollingInterval { get; set; }
    }
}
