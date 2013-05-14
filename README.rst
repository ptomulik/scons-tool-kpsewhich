scons-tool-kpsewhich
====================

This tool provides `SCons`_ with interface to kpsewhich utility. The kpsewhich
program is a part of `kpathsea`_ library, which in turn is a part of TeX Live
distribution. Its purpose is to search within the `TeX directory structure`_
(TDS) for files such as TeX classes, styles, BibTeX databases, fonts etc. For
more informations see `kpathsea manual`_ and informations about `TeX directory
structure`_ (TDS).

This tool appends new methods to the SCons Environment. It does not provide any
builders, but rather equips SCons Environment with methods that call
``kpsewhich`` program during the SConscript-reading phase. This tool does not
produce any files, it is thought as an extension for obtaining textual
information from external program.

INSTALLATION
------------

Copy the ``kpathsea.py`` file to your project's ``site_scons/site_tools/``
(per-project installation) or to ``~/.scons/site_scons/site_tools/`` (per user
installation). See SCons manual for details about installation of tools.

USAGE EXAMPLES
--------------

Find files ``article.cls`` and ``amsmath.sty`` used by ``latex``::

    env = Environment(tools = ['tex', 'kpsewhich'])
    files = env.KPSFindFiles(['article.cls','amsmath.sty'], progname='$LATEX')

Find all occurrences of ``unicode.sty`` file in TDS::

    env = Environment(tools = ['kpsewhich'])
    files = env.KPSFindAllFiles('unicode.sty')

Other functions (correspond directly to ``kpsewhich`` function options):: 

    texmf = env.KPSExpandBraces('a{b:c}d')# kpsewhich -expand-braces 'a{b,c}d'
    texmf = env.KPSExpandPath('$TEXMF')   # kpsewhich -expand-path '$TEXMF'
    texmf = env.KPSExpandVar('$TEXMF')    # kpsewhich -expand-var '$TEXMF'
    texpath = env.KPSShowPath('tex')      # kpsewhich -show-path 'tex'
    home = env.KPSVarValue('TEXMFHOME')   # kpsewhich -var-value 'TEXMFHOME'
    


CONSTRUCTION VARIABLES
``````````````````````

The following construction variables may be used to configure the ``DVIPDFM``
builder:

============================== ==============================================
        Variable                                Description
============================== ==============================================
 ``KPSEWHICH``                    the ``kpsewhich`` executable
------------------------------ ----------------------------------------------
 ``KPSEWHICHFLAGS``               additional flags to ``kpsewhich``
------------------------------ ----------------------------------------------
 ``KPSVARIABLES``                 (re)define variables seen by ``kpsewhich``
============================== ==============================================

``KPSVARIABLES`` must be a dictionary in form ``{ NAME : VALUE }``, 
for example::

  KPSVARIABLES = {"TEXMFHOME" : "/home/ptomulik/texmf"}

ARGUMENTS
`````````

These arguments are accepted by some ``KPSXxx`` methods. All the methods accept
``progname``. All other arguments are accepted by ``KPSFindFiles`` and
``KPSFindAllFiles``.

============================== ==============================================
        Variable                                Description
============================== ==============================================
 ``dpi``                         corresponds to ``-dpi`` flag,
------------------------------ ----------------------------------------------
 ``format``                      corresponds to ``-format`` flag,
------------------------------ ----------------------------------------------
 ``path``                        corresponds to ``-path`` flag
------------------------------ ----------------------------------------------
 ``progname``                    corresponds to ``-progname`` flag
------------------------------ ----------------------------------------------
 ``subdir``                      corresponds to ``-subdir`` flag
============================== ==============================================


DOWNLOADING TEST FRAMEWORK
--------------------------

To run tests you will need the `SCons test framework`_. On GNU systems you may
quickly download it with the script ``bin/download-deps.sh``::

    bin/download-deps.sh

The development tree may be later cleaned-up from the downloaded files by::

    bin/delete-deps.sh

The script uses the `mercurial`_ VCS (hg) tools to download latest version.

If the above script does not work on your platform download the following files
from the `SCons test framework`_.

 ========================= ==================================================
  source file/directory                   target file/directory
 ========================= ==================================================
  ``QMTest/``               ``QMTest/``
 ------------------------- --------------------------------------------------
  ``runtest.py``            ``runtest.py``
 ========================= ==================================================

All downloaded files are ignored from the repository by ``.gitignore``, so you
don't have to worry about deleting them before doing commits.


RUNNING TESTS
-------------

To run all the tests type::
  
    python runtest.py -a

This requires the presence of the testing framework in the development tree.

LICENSE
-------
Copyright (c) 2013 by Pawel Tomulik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

.. _SCons: http://scons.org
.. _SCons test framework: https://bitbucket.org/dirkbaechle/scons_test_framework
.. _mercurial: http://mercurial.selenic.com/
.. _TeX directory structure: http://tug.org/twg/tds/
.. _kpathsea: http://tug.org/kpathsea/
.. _kpathsea manual: http://tug.org/texinfohtml/kpathsea.html
