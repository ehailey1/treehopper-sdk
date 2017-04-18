﻿using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows;
using System.Windows.Forms;

namespace Treehopper.WPF
{
    /// <summary>
    ///     A utility class for easily minimizing WPF windows to the system tray
    /// </summary>
    public class MinimizeToSystemTray
    {
        private readonly NotifyIcon ni;
        private readonly Window window;

        /// <summary>
        ///     This is a helper class to rapidly add a minimize-to-tray functionality in WPF Win32 apps.
        /// </summary>
        /// <param name="Window">A reference to the window to control.</param>
        /// <param name="IconPath">A string referencing the .ICO path. The Icon *must* be set for this class to work properly.</param>
        /// <param name="StartMinimized">Should the window be minimized to the tray immediately?</param>
        /// <param name="RequireDoubleClick">Should the tray icon require a double-click, or will a single-click suffice?</param>
        public MinimizeToSystemTray(Window Window, string IconPath, bool StartMinimized = false,
            bool RequireDoubleClick = false) : this(Window, new Icon(IconPath), StartMinimized, RequireDoubleClick)
        {
        }

        /// <summary>
        ///     This is a helper class to rapidly add a minimize-to-tray functionality in WPF Win32 apps.
        /// </summary>
        /// <param name="Window">A reference to the window to control.</param>
        /// <param name="Icon">A string referencing the .ICO path. The Icon *must* be set for this class to work properly.</param>
        /// <param name="StartMinimized">Should the window be minimized to the tray immediately?</param>
        /// <param name="RequireDoubleClick">Should the tray icon require a double-click, or will a single-click suffice?</param>
        public MinimizeToSystemTray(Window Window, Icon Icon, bool StartMinimized = false,
            bool RequireDoubleClick = false)
        {
            if (Icon == null)
                throw new Exception("Icon must be set for this class to function properly.");
            if (Window == null)
                throw new Exception("Window must not be null.");
            window = Window;
            Window.Closing += window_Closing;
            Window.StateChanged += window_StateChanged;
            ni = new NotifyIcon();
            ni.Icon = Icon;
            ni.Visible = true;
            if (RequireDoubleClick)
                ni.DoubleClick += IconClick;
            else
                ni.Click += IconClick;

            if (StartMinimized)
            {
                Window.WindowState = WindowState.Minimized;
                Window.Hide();
            }
        }

        /// <summary>
        ///     Minimize the window to the tray.
        /// </summary>
        public void Minimize()
        {
            window.WindowState = WindowState.Minimized;
            window.Hide();
        }

        /// <summary>
        ///     Restore the window.
        /// </summary>
        public void Restore()
        {
            window.Show();
            window.WindowState = WindowState.Normal;
        }

        private void window_StateChanged(object sender, EventArgs e)
        {
            if (window.WindowState == WindowState.Minimized)
                window.Hide();
        }

        private void window_Closing(object sender, CancelEventArgs e)
        {
            ni.Dispose();
        }

        private void IconClick(object sender, EventArgs e)
        {
            if (window.WindowState == WindowState.Minimized)
                Restore();
            else if (window.WindowState == WindowState.Normal)
                Minimize();
        }
    }
}