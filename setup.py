# LOCKHEED MARTIN PROPRIETARY INFORMATION
from setuptools import setup

setup(
    name='ticc',
    version='1.0.0',
    description="Timeseries segmenting algorithm.",
    author='Matthew Trudeau',
    author_email='',
    url='https://github.com/mtrudeau314/TICC.git',
    install_requires=['matplotlib', 'sklearn', 'numpy'],
    test_requires=[],
    packages=['ticc'],
    license='',
    python_requires='~=3.6',
    package_data={'ticc': ['TICC_solver.py']},
)
