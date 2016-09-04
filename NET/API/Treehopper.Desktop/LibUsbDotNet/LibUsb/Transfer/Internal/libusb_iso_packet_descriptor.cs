using System.Runtime.InteropServices;

namespace LibUsb.Transfer.Internal
{
    /// <remarks>
    /// This class is never instantiated in .NET.  Instead it is used as a template by the <see cref="LibUsbIsoPacket"/> class.
    /// </remarks>
    [StructLayout(LayoutKind.Sequential, Pack = LibUsbApi.LIBUSB_PACK)]
    internal class libusb_iso_packet_descriptor
    {
        /// <summary>
        /// Length of data to request in this packet 
        /// </summary>
        uint length;

        /// <summary>
        /// Amount of data that was actually transferred 
        /// </summary>
        uint actual_length;

        /// <summary>
        /// Status code for this packet 
        /// </summary>
        LibUsbTansferStatus status;

        private libusb_iso_packet_descriptor() { }

    }
}