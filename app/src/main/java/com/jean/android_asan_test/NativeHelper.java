package com.jean.android_asan_test;

/**
 * Created on 2019-10-20.
 */
public class NativeHelper {
    static {
        System.loadLibrary("native-code");
    }
    public static native void HeapUseAfterFree();
}
