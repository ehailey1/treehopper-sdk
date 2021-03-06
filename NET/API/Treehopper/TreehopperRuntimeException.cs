﻿using System;

namespace Treehopper
{
    /// <summary>
    ///     A runtime exception caused in Treehopper
    /// </summary>
    public class TreehopperRuntimeException : Exception
    {
        /// <summary>
        ///     Construct a runtime exception
        /// </summary>
        /// <param name="message">the message to print</param>
        public TreehopperRuntimeException(string message)
        {
            Message = message;
        }

        /// <summary>
        ///     The message of the exception
        /// </summary>
        public override string Message { get; }
    }
}