import sys
import TestSCons

if sys.platform == 'win32':
    test = TestSCons.TestSCons(program='scons.bat', interpreter=None)
else:
    test = TestSCons.TestSCons()

test.dir_fixture('image')
test.subdir(['site_scons'])
test.subdir(['site_scons', 'site_tools'])
test.subdir(['site_scons', 'site_tools', 'kpsewhich'])
test.file_fixture('../../../../../../__init__.py', 'site_scons/site_tools/kpsewhich/__init__.py')
test.file_fixture('../../../../../../about.py', 'site_scons/site_tools/kpsewhich/about.py')

test.subdir(['site_scons', 'site_tools', 'ci'])
test.file_fixture('../../../../support/ci/__init__.py', 'site_scons/site_tools/ci/__init__.py')
