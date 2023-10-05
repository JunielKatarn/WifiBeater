using System;
using System.Runtime.InteropServices;

namespace Hyvart.WifiManager
{
    // http://jonathanpeppers.com/Blog/xamarin-ios-under-the-hood-calling-objective-c-from-csharp
    // https://gist.github.com/tsubaki/0fdc6327203a6e54fa80
    // https://pilky.me/dynamic-tips-tricks-with-objective-c/
    // https://developer.apple.com/documentation/objectivec/1418952-objc_getclass
    // https://stackoverflow.com/questions/48616053
    // https://stackoverflow.com/questions/14653058
    // https://stackoverflow.com/questions/26551193
    // https://developer.limneos.net/?ios=16.3&framework=SpringBoard&header=SBWiFiManager.h
    public static class ObjC
	{
        //TODO: Check arguments
        //[DllImport("/usr/lib/libobjc.dylib", EntryPoint = "objc_getClass")]
        [DllImport("__Internal")]
		static extern IntPtr objc_getClass(string name);

        public static IntPtr GetClass(string name)
        {
            return objc_getClass(name);
        }
    }

    public static class SBWifiManager
    {
        static IntPtr classPtr = ObjC.GetClass("SBWifiManager");

        public static bool WifiEnabled
        {
            get
            {
                return false;
            }

            set
            {

            }
        }
    }
}

