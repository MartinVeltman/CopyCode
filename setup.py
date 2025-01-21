from setuptools import setup, find_packages

setup(
    name='copycode',
    version='0.2.3',
    description='Copy all your code to your clipboard or a file with one command.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='MartinVeltman',
    author_email='martin.veltman@winvent.nl',
    license='MIT',
    url='https://github.com/MartinVeltman/CopyCode',
    project_urls={
        "Source Code": "https://github.com/MartinVeltman/CopyCode",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyperclip',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'copycode=copycode.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)