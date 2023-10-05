using System;
using System.Runtime.InteropServices;

namespace Hyvart.WifiManager
{
    // http://jonathanpeppers.com/Blog/xamarin-ios-under-the-hood-calling-objective-c-from-csharp
    public static class NativeApis
	{
		[DllImport("/usr/lib/libobjc.dylib", EntryPoint = "objc_getClass")]
		public static extern IntPtr IntPtr_objc_getClass(IntPtr receiver, IntPtr selector);
    }
}

