# See https://packaging.python.org/en/latest/distributing.html
# and https://docs.python.org/2/distutils/setupscript.html
# and https://pypi.python.org/pypi?%3Aaction=list_classifiers
from setuptools import setup, find_packages


def read(path):
    with open(path, "r") as f:
        contents = f.read()
        f.close()
    return contents

setup(
    name='django-htmgel-bootstrap4',
    version=read("VERSION.txt"),
    description=read("DESCRIPTION.txt"),
    long_description=read("README.markdown"),
    author='Shawn Davis',
    author_email='shawn@develmaycare.com',
    url='https://github.com/develmaycare/django-htmgel-bootstrap4',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "bs4",
        # "django-htmgel",
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
    ],
    zip_safe=False,
    tests_require=["bs4"],
    test_suite='runtests.runtests'
)
