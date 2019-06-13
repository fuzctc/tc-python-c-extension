/* 定义 module名称 */
%module speedup_fib

/*导入定义的 speedup_fib.h*/
%{
#include "speedup_fib.h"
%}
/* 告诉 SWIG 定义的 function 或 variable */
long long fib(long long n);
