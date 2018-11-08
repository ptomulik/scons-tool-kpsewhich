#
# Copyright (c) 2013-2018 by Pawel Tomulik <ptomulik@meil.pw.edu.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

__docformat__ = "restructuredText"

"""
TODO: Write documentation
"""

import sys
import TestSCons

if sys.platform == 'win32':
    test = TestSCons.TestSCons(program='scons.bat', interpreter=None)
else:
    test = TestSCons.TestSCons()

test.dir_fixture('image')
test.subdir(['share'])
test.dir_fixture('share', 'share')
test.subdir(['site_scons'])
test.subdir(['site_scons', 'site_tools'])
test.subdir(['site_scons', 'site_tools', 'kpsewhich'])
test.file_fixture('../../../../../../__init__.py', 'site_scons/site_tools/kpsewhich/__init__.py')
test.file_fixture('../../../../../../about.py', 'site_scons/site_tools/kpsewhich/about.py')

# Normal invocation
test.run()
test.must_exist('stdout.txt')
test.must_contain('stdout.txt','./share/texmf/tex/latex/local/foo.cls', 'rt')
test.must_contain('stdout.txt','./share/texmf/tex/latex/local/bar.sty', 'rt')
test.must_not_contain('stdout.txt','./share/texmf/tex/amstex/local/foo.cls', 'rt')
test.must_not_contain('stdout.txt','./share/texmf/tex/amstex/local/bar.sty', 'rt')

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
