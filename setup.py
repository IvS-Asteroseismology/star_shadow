"""STAR SHADOW

Code written by: Luc IJspeert
"""

from setuptools import setup


# package version
MAJOR = 1
MINOR = 1
ATTR = '7'
# full acronym
ACRONYM = ('Satellite Time-series Analysis Routine using Sinusoids and Harmonics Automatedly '
           'for Double stars with Occultations and Waves')

setup(name="star_shadow",
      version=f'{MAJOR}.{MINOR}.{ATTR}',
      author='Luc IJspeert',
<<<<<<< HEAD
=======
      url='https://github.com/LucIJspeert/star_shadow',
>>>>>>> b0e00e0c4be3a4b2faca0b23498d1af8592f94ce
      license='GNU General Public License v3.0',
      description=ACRONYM,
      long_description=open('README.md').read(),
      packages=['star_shadow'],
      package_dir={'star_shadow': 'star_shadow'},
<<<<<<< HEAD
      package_data={'star_shadow': ['star_shadow/data/tess_sectors.dat', 'star_shadow/data/mpl_stylesheet.dat'
                                    'star_shadow/data/sim_000_lc.dat']},
=======
      package_data={'star_shadow': ['data/tess_sectors.dat', 'data/mpl_stylesheet.dat', 'data/sim_000_lc.dat']},
>>>>>>> b0e00e0c4be3a4b2faca0b23498d1af8592f94ce
      include_package_data=True,
      python_requires='>=3.6',
      install_requires=['numpy', 'scipy', 'numba', 'h5py', 'astropy', 'matplotlib', 'arviz', 'corner'],
      extras_require={'ellc': ['ellc'], 'mcmc': ['pymc3', 'fastprogress', 'theano']}
     )
