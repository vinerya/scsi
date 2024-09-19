from setuptools import setup, find_packages

setup(
    name='scsi',
    version='0.1.0',
    author='Moudather Chelbi',
    author_email='Moudather Chelbi',
    description='Satellite Constellation Spatial Index (SCSI) for geospatial data on spherical surfaces',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vinerya/scsi',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
    install_requires=[
        # List dependencies here
    ],
)
