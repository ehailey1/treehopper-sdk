\mainpage Welcome

\section intro_sec Introduction

This documentation contains all C++-specific information for interfacing with Treehopper. For hardware documentation, or for documentation for other languages, visit <a href="https://docs.treehopper.io/">https://docs.treehopper.io/</a>.


\subsection features Features
Treehopper's cross-platform C++ API can be compiled on Windows, macOS, Linux, and other UNIX-like operating systems. 

\subsection libraries Libraries
In addition to the main API that allows you to manipulate and sample pins on the Treehopper, the C++ API also includes an ever-growing library full of drivers for many different peripheral ICs, including IMUs and other sensors; GPIO expanders, DACs and ADCs; LED drivers, character and graphical displays; and motor drivers, rotary encoders, and other motion devices.

\subsection Modules
There are two modules in the C++ source tree:
- Treehopper: the base library. Provides GPIO, PWM, I2C, SPI, and base interface support. Exposes the Treehopper namespace. If compiled under Windows, Treehopper will call directly into native WinUSB functions, so there are no external dependencies. If compiled under macOS, Linux, or other UNIX-like operating system, Treehopper will call into LibUSB. You'll need to make sure you have both the LibUSB runtime library and LibUSB development headers/libs installed. This is not an issue on Linux, but macOS users will need to fetch this from brew, or whatever package manager they use. 
- Treehopper.Libraries: provides support for more than 100 commonly-used ICs and peripherals.
