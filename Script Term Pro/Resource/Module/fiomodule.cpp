#include "python.h"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

const char* filename = "favoriteList";


static PyObject * 
fio_save(PyObject *self, PyObject *args)
{
    PyObject* pyList;
    if (!PyArg_ParseTuple(args, "O", &pyList)) {
        return NULL;
    }

    if (!PyList_Check(pyList)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list");
        return NULL;
    }

    std::ofstream outFile(filename);
    if (!outFile) {
        PyErr_SetString(PyExc_IOError, "Could not open file for writing");
        return NULL;
    }

    Py_ssize_t numItems = PyList_Size(pyList);
    for (Py_ssize_t i = 0; i < numItems; ++i) {
        PyObject* pyItem = PyList_GetItem(pyList, i);
        if (!PyUnicode_Check(pyItem)) {
            PyErr_SetString(PyExc_TypeError, "List items must be strings");
            return NULL;
        }
        const char* item = PyUnicode_AsUTF8(pyItem);
        outFile << item << std::endl;
    }

    outFile.close();
    Py_RETURN_NONE;
}

static PyObject *
fio_load(PyObject *self, PyObject *args)
{
    std::ifstream inFile(filename);
    if (!inFile) {
        PyErr_SetString(PyExc_IOError, "Could not open file for reading");
        return NULL;
    }

    PyObject* pyList = PyList_New(0);
    if (!pyList) {
        inFile.close();
        return NULL;
    }

    std::string line;
    while (std::getline(inFile, line)) {
        PyObject* pyLine = PyUnicode_FromString(line.c_str());
        if (!pyLine) {
            Py_DECREF(pyList);
            inFile.close();
            return NULL;
        }
        PyList_Append(pyList, pyLine);
        Py_DECREF(pyLine);
    }

    inFile.close();
    return pyList;
}

static PyMethodDef FioMethods[] = {
    {"save", fio_save, METH_VARARGS,
    "Save string list to file"},
    {"load", fio_load, METH_VARARGS,
    "Load string list from file"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fiomodule = {
    PyModuleDef_HEAD_INIT,
    "fio",
    "file input output module",
    -1,FioMethods
};

PyMODINIT_FUNC
PyInit_fio(void)
{
    return PyModule_Create(&fiomodule);
}
