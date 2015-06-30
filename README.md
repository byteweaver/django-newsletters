# django-newsletters

WARNING: This app is in early development (pre-alpha) and may not work as intended, change rapidly or break something. Please wait for a stable release or at least for an alpha or beta release.

Template for reusable django applications.

All following sections are just dummies and may not work as excepted.

## Key features

* Reusable template for new reusable django applications
* ...

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-newsletters

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-newsletters#egg=django-newsletters

Add `newsletters` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'newsletters',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^your-url/$', include('newsletters.urls', namespace='newsletters')),
        ...
    )
