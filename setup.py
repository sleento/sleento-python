from setuptools import find_packages, setup

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='sleento',
    packages=find_packages(),
    version='0.0.1',
    description='SleentO Python package for sending sms to your customer',
    author='Ged-flod',
    author_email='magenta.sleento@gmail.com',
    license='MIT',
    long_description_content_type="text/markdown",
    long_description=README,
    keywords=['sleento', 'sleento-python', 'sleento-code'],
    install_requires=['requests>=2.22.0'],
    setup_requires=['pytest-runner'],   
    url='https://github.com/sleento/sleento-python',
    tests_requires=['pytest'],
    test_suite='tests',
    python_requires='>=3.6',
    
    include_package_data=True
)