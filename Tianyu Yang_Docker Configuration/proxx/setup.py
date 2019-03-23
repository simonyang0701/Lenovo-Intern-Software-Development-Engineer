from setuptools import setup


setup(
    name='proxx',
    version='1.0.0',
    packages=['proxx',],
    include_package_data=True,
    url='https://github.com/simonyang0701/Lenovo-Intern-Software-Development-Engineer/tree/master/Tianyu%20Yang_Docker%20Configuration/proxx',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    author= 'Simon Yang',
    author_email= 'tianyu5041@gmail.com',
    description= '',
    install_requires=[
    ],
    #data_files=[
    #    ('share/icons/hicolor/scalable/apps', ['data/proxx.svg']),
    #    ('share/applications', ['data/proxx.desktop'])
	#    Referred from https://github.com/chris17453/proxx
    #],
    entry_points="""
        [console_scripts]
        proxx = proxx.cli:main
        """    
    
)



