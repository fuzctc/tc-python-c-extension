#include <Python.h>

long long _fib(long long n){
    if(n < 2)
        return n;
    else
        return _fib(n-1) + _fib(n-2);
};


static PyObject *fib(PyObject *self, PyObject *args) {

    // Arguments
   long long n;

   long long res;

   if (!PyArg_ParseTuple(args, "l", &n))
       return NULL;

   res = _fib(n);

   return Py_BuildValue("l", res);
};

static PyMethodDef SpeedupFibMethods[] = {
    {"speedup_fib", (PyCFunction) fib, METH_VARARGS, "fast fib"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef speedup_fib_module = {
    PyModuleDef_HEAD_INIT,
    "speedup_fib",
    "A module containing methods with faster fib.",
    -1,
    SpeedupFibMethods
};


PyMODINIT_FUNC PyInit_speedup_fib() {
  return PyModule_Create(&speedup_fib_module);
}
