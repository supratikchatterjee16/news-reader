from setuptools import setup, Extension, find_packages

with open('README.md') as f:
	extd_desc = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements_noversion = [
	'pandas',
    'sqlalchemy',
    'deg',
    'argparse',
    'appdirs',
    'werkzeug',
    'fastapi',
    'uvicorn',
    'newsapi-python'
]
setup(
	# Meta information
	name				= 'news_reader',
	version				= '0.1.0',
	author				= 'Supratik Chatterjee',
	author_email			= 'supratikdevm96@gmail.com',
	url				= 'https://github.com/supratikchatterjee16/news_reader',
	description			= 'Read news from everywhere.',
	keywords			= ["data", "anonymize", "obfuscate", "migrate", "backup", "archive", "purge", "rdbms", "oracle", "postgres"],
	install_requires		= requirements_noversion,
	# build information
	py_modules			= ['news_reader'],
	packages			= find_packages(),
	package_dir			= {'news_reader' : 'news_reader'},
	long_description		= extd_desc,
	long_description_content_type	= 'text/markdown',
	include_package_data		= True,
	package_data			= {
            'news_reader' : [
						'data/*',
						'res/**',
						]},
    entry_points		= {'console_scripts' : ['news_reader = news_reader:run'],},
	zip_safe			= True,
	# https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
	classifiers			= [
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	license 			= license
)