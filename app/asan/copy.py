#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import platform
import shutil
import sys


class NdkPath:
    def __init__(self):
        self.__lib_path = ""
        ndk = os.environ["ANDROID_NDK_HOME"]
        ndk += "/toolchains/llvm/prebuilt/{}-x86_64".format(platform.system().lower())

        with open(ndk + "/AndroidVersion.txt", "r") as f:
            version = f.readline()
            version = version.strip()
            self.__lib_path = ndk + "/lib64/clang/{}/lib/linux/".format(version)

    def copy_lib(self, dst_folder, lib_name):
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)
        print("copy {} {}".format(self.__lib_path + lib_name, dst_folder + lib_name))
        if os.path.exists(dst_folder + lib_name):
            os.remove(dst_folder + lib_name)
        shutil.copyfile(self.__lib_path + lib_name, dst_folder + lib_name)

    def copy_asan(self, dst_folder):
        if not dst_folder.endswith("/") and not dst_folder.endswith("\\"):
            dst_folder += "/"
        self.copy_lib(dst_folder + "lib/armeabi-v7a/", "libclang_rt.asan-arm-android.so")
        self.copy_lib(dst_folder + "lib/arm64-v8a/", "libclang_rt.asan-aarch64-android.so")
        self.copy_lib(dst_folder + "lib/x86/", "libclang_rt.asan-i686-android.so")
        self.copy_lib(dst_folder + "lib/x86_64/", "libclang_rt.asan-x86_64-android.so")


def main():
    ndk_path = NdkPath()
    ndk_path.copy_asan(sys.argv[1])


if __name__ == "__main__":
    main()
