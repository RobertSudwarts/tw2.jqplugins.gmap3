from setuptools import setup, find_packages

setup(
    name='tw2.jqplugins.gmap3',
    version='0.1',
    description='toscawidgets 2 wrapper for gmap3',
    author='Robert Sudwarts',
    author_email='robert.sudwarts@gmail.com',
    url='',
    install_requires=[
        "tw2.core",
        "tw2.jquery",   # v. >= 1.4.4  
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.tw2.jqplugins.gmap3
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
