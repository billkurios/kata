from setuptools import find_packages, setup


setup(
    name='kata',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    entry_points="""
        [console_scripts]
        kata=kata:cli
    """
)