=============================
zdm_api
=============================

.. image:: https://badge.fury.io/py/zdm_api.png
    :target: https://badge.fury.io/py/zdm_api

.. image:: https://travis-ci.org/pghalliday/zdm_api.png?branch=master
    :target: https://travis-ci.org/pghalliday/zdm_api

Zipped dependency manager API

Documentation
-------------

The full documentation is at https://zdm_api.readthedocs.org.

Quickstart
----------

Install zdm_api::

    pip install zdm_api

Then integrate into a Django project `settings.py`::

		INSTALLED_APPS = [

				...

				'zdm_api',
				'rest_framework',
				'rest_framework_swagger',
		]

    ...

    # settings for rest_framework
    REST_FRAMEWORK = {
      'PAGE_SIZE': 10
    }

		...

		# settings for swagger
    SWAGGER_SETTINGS = {
      'LOGIN_URL': 'rest_framework:login'
      'LOGOUT_URL': 'rest_framework:logout'
    }

And add to Django project `urls.py`::

	from django.conf.urls import url, include

	urlpatterns = [

			...

			url(r'^api/', include('zdm_api.urls', namespace='zdm_api')),
			url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	]

Note that the namespace parameters must be as shown but the urls can change.

Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
