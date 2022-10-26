import os
import numpy
from setuptools import setup
from setuptools import Command, Extension, find_packages
from Cython.Build import cythonize

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bcflight.setup")

PROJECT = "bcflight"

def get_project_configuration():
    """Returns project arguments for setup"""
    # Use installed numpy version as minimal required version
    # This is useful for wheels to advertise the numpy version they were built with
    numpy_requested_version = ">=%s" % numpy.version.version    
    logger.info("Install requires: numpy %s", numpy_requested_version)

    install_requires = [
        # for most of the computation
        "numpy%s" % numpy_requested_version,
        ]

    # bcf2nexus.third_party
    ext_modules = [Extension(name= "bcflight.third_party.unbcf_fast",
                             sources=['src/bcflight/third_party/unbcf_fast.pyx'])]

    ext_modules = cythonize(ext_modules,
                            compiler_directives={'language_level' : "3"})

    package_dir = {"": "src"}
    packages = ['bcflight',
                'bcflight.third_party']
    return dict(
        name=PROJECT,
        version="0.0.1",
        license="GPL",
        description="Light-dependencies version of hyperspy.io_plugins.bruker",
        packages=packages,
        package_dir=package_dir,
        ext_modules=ext_modules,
        )

if __name__ == "__main__":
    from setuptools import setup
    setup(**get_project_configuration())
