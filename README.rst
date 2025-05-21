====================
CUNEIFORM
====================

Use a docx or idml as a jinja2 template with extended formatting for variables to have their type declared.

Introduction
------------

This package uses 2 major packages :

- python-docx for reading, writing and creating sub documents
- jinja2 for managing tags inserted into the template docx

Forked from docxtpl (https://github.com/elapouya/python-docx-template)
Original work © 2014-2021 by Sébastien Lapoire – MIT Licensed

.. The idea is to begin to create an example of the document you want to generate with microsoft word, it can be as complex as you want :
.. pictures, index tables, footer, header, variables, anything you can do with word.
.. Then, as you are still editing the document with microsoft word, you insert jinja2-like tags directly in the document.
.. You save the document as a .docx file (xml format) : it will be your .docx template file.

.. Now you can use python-docx-template to generate as many word documents you want from this .docx template and context variables you will associate.


Documentation
-------------

.. Please, `read the doc <http://docxtpl.readthedocs.org>`_