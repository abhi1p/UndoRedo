from setuptools import setup

with open('Readme.md') as file:
    longDescription = file.read()

setup(name='UndoRedo',
      version='1.0',
      description='Implementation of Undo, Redo',
      long_description=longDescription,
      url='https://github.com/abhi1p/UndoRedo',
      author='Abhishek Anand',
      author_email="abhishekanand2a@gmail.com",
      license='MIT',
      packages=['UndoRedo'],
      install_requires=[],
      )