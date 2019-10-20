#include <jni.h>
#include <android/log.h>

static const char *TAG = "native-code";

extern "C"
{

JNIEXPORT void Java_com_jean_android_1asan_1test_NativeHelper_HeapUseAfterFree(JNIEnv *, jclass)
{
    // https://github.com/google/sanitizers/wiki/AddressSanitizerExampleUseAfterFree
    int *array = new int[100];
    delete [] array;
    __android_log_print(ANDROID_LOG_DEBUG, TAG, "heap-use-after-free %d", array[0]);
}

}