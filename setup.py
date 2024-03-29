import os.path, codecs, re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = codecs.open(os.path.join(here, 'AST/README'), encoding='utf8').read()
CHANGES = codecs.open(os.path.join(here, 'AST/CHANGES'), encoding='utf8').read()

with codecs.open(os.path.join(os.path.dirname(__file__), 'AST', '__init__.py'),
                 encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))

setup(name='PyAST',
      version=metadata['version'],
      description='AST 0.0.2 Fixed',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        ],
      author='Diego Fernandez',
      author_email='di3g0bs0n@gmail.com',
      url='https://github.com/di3g0bs0n/PyAST',
      keywords=['AST', 'packaging'],
      license='MIT',
      packages=[
          'AST',
          ],
      extras_require={
          ':python_version=="2.6"': ['argparse'],
          'signatures': ['keyring', 'keyrings.alt'],
          'signatures:sys_platform!="win32"': ['pyxdg'],
          'signatures:python_version=="2.6"': ['importlib'],
          'faster-signatures': ['ed25519ll'],
          'tool': []
          },
      tests_require=['jsonschema', 'pytest', 'coverage', 'pytest-cov'],
      include_package_data=True,
      zip_safe=False,
      entry_points = """\
[console_scripts]
AST = AST.AST:main

[distutils.commands]
bdist_AST = AST.bdist_AST:bdist_AST"""
      )

