from setuptools import setup

setup(
    name='ntlk-stemming-lite',
    version='1.0.0',
    description='Stemming from the NTLK library usable on AppEngine',
    url='https://github.com/bimblehq/nltk-stemming-lite',
    author='Tomi Novak',
    author_email='tomi@bimble.com',
    license='MIT',
    packages=['ntlk_stemming_lite'],
    include_package_data=False,
    zip_safe=False
)