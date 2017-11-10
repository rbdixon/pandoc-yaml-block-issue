import os
import pytest
import subprocess
import shutil
from pathlib import Path
import re

MD = '''
---
ml: |{sep}
    TEST

    BLOCK
...
'''

EXPECTED = '''
    TEST

    BLOCK
'''

VERSIONS = [
    '1.16',
    '1.16.0.2',
    '1.17.0.3',
    '1.17.2',
    '1.18',
    '1.19.2.1',
    '2.0.0.1',
    '2.0.1',
    '2.0.1.1',
    'HEAD-6e832a5',
]

SEP = {
    '': 'none',
    '-': 'minus',
    '+': 'plus',
}

def cmd(cmdline):
    print(cmdline)
    subprocess.call(cmdline, shell=True)

def pytest_generate_tests(metafunc):
    if 'version' in metafunc.fixturenames:
        metafunc.parametrize('version', VERSIONS)
    if 'sep' in metafunc.fixturenames:
        sep = SEP.keys()
        sepstr = [ SEP[key] for key in sep]
        metafunc.parametrize('sep', sep, ids=sepstr)

@pytest.fixture(scope='session')
def workdir():
    res = Path('test_results')

    if res.exists():
        shutil.rmtree(str(res))

    res.mkdir()

    return res

@pytest.fixture()
def report(workdir, version, sep):
    vstr = re.sub('\.', '_', version)
    sstr = SEP[sep]
    testdir = f'{vstr}_{sstr}'

    res = workdir / testdir
    res.mkdir()

    old_cwd = os.getcwd()
    os.chdir(str(res))

    yield Path()

    os.chdir(old_cwd)

def test_compare_versions(report, version, sep):
    md = report / 'report.md'
    outfile = (report / f'report.markdown')

    md.write_text(MD.format(sep=sep))

    cmd(f'brew switch pandoc {version}')
    cmd(f'pandoc --version > version.txt')

    for output in ['markdown', 'native', 'plain']:
        cmd(f'pandoc -f markdown -t {output} -s < report.md > report.{output}')

    assert EXPECTED in outfile.read_text()
