#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : html5lib
Version  : 1.0.1
Release  : 40
URL      : https://files.pythonhosted.org/packages/85/3e/cf449cf1b5004e87510b9368e7a5f1acd8831c2d6691edd3c62a0823f98f/html5lib-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/3e/cf449cf1b5004e87510b9368e7a5f1acd8831c2d6691edd3c62a0823f98f/html5lib-1.0.1.tar.gz
Summary  : HTML parser based on the WHATWG HTML specification
Group    : Development/Tools
License  : MIT
Requires: html5lib-license = %{version}-%{release}
Requires: html5lib-python = %{version}-%{release}
Requires: html5lib-python3 = %{version}-%{release}
Requires: chardet
Requires: lxml
Requires: six
Requires: webencodings
BuildRequires : buildreq-distutils3
BuildRequires : chardet
BuildRequires : lxml
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : webencodings

%description
html5lib
========

.. image:: https://travis-ci.org/html5lib/html5lib-python.png?branch=master
  :target: https://travis-ci.org/html5lib/html5lib-python

html5lib is a pure-python library for parsing HTML. It is designed to
conform to the WHATWG HTML specification, as is implemented by all major
web browsers.


Usage
-----

Simple usage follows this pattern:

.. code-block:: python

  import html5lib
  with open("mydocument.html", "rb") as f:
      document = html5lib.parse(f)

or:

.. code-block:: python

  import html5lib
  document = html5lib.parse("<p>Hello World!")

By default, the ``document`` will be an ``xml.etree`` element instance.
Whenever possible, html5lib chooses the accelerated ``ElementTree``
implementation (i.e. ``xml.etree.cElementTree`` on Python 2.x).

Two other tree types are supported: ``xml.dom.minidom`` and
``lxml.etree``. To use an alternative format, specify the name of
a treebuilder:

.. code-block:: python

  import html5lib
  with open("mydocument.html", "rb") as f:
      lxml_etree_document = html5lib.parse(f, treebuilder="lxml")

When using with ``urllib2`` (Python 2), the charset from HTTP should be
pass into html5lib as follows:

.. code-block:: python

  from contextlib import closing
  from urllib2 import urlopen
  import html5lib

  with closing(urlopen("http://example.com/")) as f:
      document = html5lib.parse(f, transport_encoding=f.info().getparam("charset"))

When using with ``urllib.request`` (Python 3), the charset from HTTP
should be pass into html5lib as follows:

.. code-block:: python

  from urllib.request import urlopen
  import html5lib

  with urlopen("http://example.com/") as f:
      document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())

To have more control over the parser, create a parser object explicitly.
For instance, to make the parser raise exceptions on parse errors, use:

.. code-block:: python

  import html5lib
  with open("mydocument.html", "rb") as f:
      parser = html5lib.HTMLParser(strict=True)
      document = parser.parse(f)

When you're instantiating parser objects explicitly, pass a treebuilder
class as the ``tree`` keyword argument to use an alternative document
format:

.. code-block:: python

  import html5lib
  parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("dom"))
  minidom_document = parser.parse("<p>Hello World!")

More documentation is available at https://html5lib.readthedocs.io/.


Installation
------------

html5lib works on CPython 2.7+, CPython 3.3+ and PyPy.  To install it,
use:

.. code-block:: bash

    $ pip install html5lib


Optional Dependencies
---------------------

The following third-party libraries may be used for additional
functionality:

- ``datrie`` can be used under CPython to improve parsing performance
  (though in almost all cases the improvement is marginal);

- ``lxml`` is supported as a tree format (for both building and
  walking) under CPython (but *not* PyPy where it is known to cause
  segfaults);

- ``genshi`` has a treewalker (but not builder); and

- ``chardet`` can be used as a fallback when character encoding cannot
  be determined.


Bugs
----

Please report any bugs on the `issue tracker
<https://github.com/html5lib/html5lib-python/issues>`_.


Tests
-----

Unit tests require the ``pytest`` and ``mock`` libraries and can be
run using the ``py.test`` command in the root directory.

Test data are contained in a separate `html5lib-tests
<https://github.com/html5lib/html5lib-tests>`_ repository and included
as a submodule, thus for git checkouts they must be initialized::

  $ git submodule init
  $ git submodule update

If you have all compatible Python implementations available on your
system, you can run tests on all of them using the ``tox`` utility,
which can be found on PyPI.


Questions?
----------

There's a mailing list available for support on Google Groups,
`html5lib-discuss <http://groups.google.com/group/html5lib-discuss>`_,
though you may get a quicker response asking on IRC in `#whatwg on
irc.freenode.net <http://wiki.whatwg.org/wiki/IRC>`_.

Change Log
----------

1.0.1
~~~~~

Released on December 7, 2017

Breaking changes:

* Drop support for Python 2.6. (#330) (Thank you, Hugo, Will Kahn-Greene!)
* Remove ``utils/spider.py`` (#353) (Thank you, Jon Dufresne!)

Features:

* Improve documentation. (#300, #307) (Thank you, Jon Dufresne, Tom Most,
  Will Kahn-Greene!)
* Add iframe seamless boolean attribute. (Thank you, Ritwik Gupta!)
* Add itemscope as a boolean attribute. (#194) (Thank you, Jonathan Vanasco!)
* Support Python 3.6. (#333) (Thank you, Jon Dufresne!)
* Add CI support for Windows using AppVeyor. (Thank you, John Vandenberg!)
* Improve testing and CI and add code coverage (#323, #334), (Thank you, Jon
  Dufresne, John Vandenberg, Geoffrey Sneddon, Will Kahn-Greene!)
* Semver-compliant version number.

Bug fixes:

* Add support for setuptools < 18.5 to support environment markers. (Thank you,
  John Vandenberg!)
* Add explicit dependency for six >= 1.9. (Thank you, Eric Amorde!)
* Fix regexes to work with Python 3.7 regex adjustments. (#318, #379) (Thank
  you, Benedikt Morbach, Ville Skyttä, Mark Vasilkov!)
* Fix alphabeticalattributes filter namespace bug. (#324) (Thank you, Will
  Kahn-Greene!)
* Include license file in generated wheel package. (#350) (Thank you, Jon
  Dufresne!)
* Fix annotation-xml typo. (#339) (Thank you, Will Kahn-Greene!)
* Allow uppercase hex chararcters in CSS colour check. (#377) (Thank you,
  Komal Dembla, Hugo!)


1.0
~~~

Released and unreleased on December 7, 2017. Badly packaged release.


0.999999999/1.0b10
~~~~~~~~~~~~~~~~~~

Released on July 15, 2016

* Fix attribute order going to the tree builder to be document order
  instead of reverse document order(!).


0.99999999/1.0b9
~~~~~~~~~~~~~~~~

Released on July 14, 2016

* **Added ordereddict as a mandatory dependency on Python 2.6.**

* Added ``lxml``, ``genshi``, ``datrie``, ``charade``, and ``all``
  extras that will do the right thing based on the specific
  interpreter implementation.

* Now requires the ``mock`` package for the testsuite.

* Cease supporting DATrie under PyPy.

* **Remove PullDOM support, as this hasn't ever been properly
  tested, doesn't entirely work, and as far as I can tell is
  completely unused by anyone.**

* Move testsuite to ``py.test``.

* **Fix #124: move to webencodings for decoding the input byte stream;
  this makes html5lib compliant with the Encoding Standard, and
  introduces a required dependency on webencodings.**

* **Cease supporting Python 3.2 (in both CPython and PyPy forms).**

* **Fix comments containing double-dash with lxml 3.5 and above.**

* **Use scripting disabled by default (as we don't implement
  scripting).**

* **Fix #11, avoiding the XSS bug potentially caused by serializer
  allowing attribute values to be escaped out of in old browser versions,
  changing the quote_attr_values option on serializer to take one of
  three values, "always" (the old True value), "legacy" (the new option,
  and the new default), and "spec" (the old False value, and the old
  default).**

* **Fix #72 by rewriting the sanitizer to apply only to treewalkers
  (instead of the tokenizer); as such, this will require amending all
  callers of it to use it via the treewalker API.**

* **Drop support of charade, now that chardet is supported once more.**

* **Replace the charset keyword argument on parse and related methods
  with a set of keyword arguments: override_encoding, transport_encoding,
  same_origin_parent_encoding, likely_encoding, and default_encoding.**

* **Move filters._base, treebuilder._base, and treewalkers._base to .base
  to clarify their status as public.**

* **Get rid of the sanitizer package. Merge sanitizer.sanitize into the
  sanitizer.htmlsanitizer module and move that to sanitizer. This means
  anyone who used sanitizer.sanitize or sanitizer.HTMLSanitizer needs no
  code changes.**

* **Rename treewalkers.lxmletree to .etree_lxml and
  treewalkers.genshistream to .genshi to have a consistent API.**

* Move a whole load of stuff (inputstream, ihatexml, trie, tokenizer,
  utils) to be underscore prefixed to clarify their status as private.


0.9999999/1.0b8
~~~~~~~~~~~~~~~

Released on September 10, 2015

* Fix #195: fix the sanitizer to drop broken URLs (it threw an
  exception between 0.9999 and 0.999999).


0.999999/1.0b7
~~~~~~~~~~~~~~

Released on July 7, 2015

* Fix #189: fix the sanitizer to allow relative URLs again (as it did
  prior to 0.9999/1.0b5).


0.99999/1.0b6
~~~~~~~~~~~~~

Released on April 30, 2015

* Fix #188: fix the sanitizer to not throw an exception when sanitizing
  bogus data URLs.


0.9999/1.0b5
~~~~~~~~~~~~

Released on April 29, 2015

* Fix #153: Sanitizer fails to treat some attributes as URLs. Despite how
  this sounds, this has no known security implications.  No known version
  of IE (5.5 to current), Firefox (3 to current), Safari (6 to current),
  Chrome (1 to current), or Opera (12 to current) will run any script
  provided in these attributes.

* Pass error message to the ParseError exception in strict parsing mode.

* Allow data URIs in the sanitizer, with a whitelist of content-types.

* Add support for Python implementations that don't support lone
  surrogates (read: Jython). Fixes #2.

* Remove localization of error messages. This functionality was totally
  unused (and untested that everything was localizable), so we may as
  well follow numerous browsers in not supporting translating technical
  strings.

* Expose treewalkers.pprint as a public API.

* Add a documentEncoding property to HTML5Parser, fix #121.


0.999
~~~~~

Released on December 23, 2013

* Fix #127: add work-around for CPython issue #20007: .read(0) on
  http.client.HTTPResponse drops the rest of the content.

* Fix #115: lxml treewalker can now deal with fragments containing, at
  their root level, text nodes with non-ASCII characters on Python 2.


0.99
~~~~

Released on September 10, 2013

* No library changes from 1.0b3; released as 0.99 as pip has changed
  behaviour from 1.4 to avoid installing pre-release versions per
  PEP 440.


1.0b3
~~~~~

Released on July 24, 2013

* Removed ``RecursiveTreeWalker`` from ``treewalkers._base``. Any
  implementation using it should be moved to
  ``NonRecursiveTreeWalker``, as everything bundled with html5lib has
  for years.

* Fix #67 so that ``BufferedStream`` to correctly returns a bytes
  object, thereby fixing any case where html5lib is passed a
  non-seekable RawIOBase-like object.


1.0b2
~~~~~

Released on June 27, 2013

* Removed reordering of attributes within the serializer. There is now
  an ``alphabetical_attributes`` option which preserves the previous
  behaviour through a new filter. This allows attribute order to be
  preserved through html5lib if the tree builder preserves order.

* Removed ``dom2sax`` from DOM treebuilders. It has been replaced by
  ``treeadapters.sax.to_sax`` which is generic and supports any
  treewalker; it also resolves all known bugs with ``dom2sax``.

* Fix treewalker assertions on hitting bytes strings on
  Python 2. Previous to 1.0b1, treewalkers coped with mixed
  bytes/unicode data on Python 2; this reintroduces this prior
  behaviour on Python 2. Behaviour is unchanged on Python 3.


1.0b1
~~~~~

Released on May 17, 2013

* Implementation updated to implement the `HTML specification
  <http://www.whatwg.org/specs/web-apps/current-work/>`_ as of 5th May
  2013 (`SVN <http://svn.whatwg.org/webapps/>`_ revision r7867).

* Python 3.2+ supported in a single codebase using the ``six`` library.

* Removed support for Python 2.5 and older.

* Removed the deprecated Beautiful Soup 3 treebuilder.
  ``beautifulsoup4`` can use ``html5lib`` as a parser instead. Note that
  since it doesn't support namespaces, foreign content like SVG and
  MathML is parsed incorrectly.

* Removed ``simpletree`` from the package. The default tree builder is
  now ``etree`` (using the ``xml.etree.cElementTree`` implementation if
  available, and ``xml.etree.ElementTree`` otherwise).

* Removed the ``XHTMLSerializer`` as it never actually guaranteed its
  output was well-formed XML, and hence provided little of use.

* Removed default DOM treebuilder, so ``html5lib.treebuilders.dom`` is no
  longer supported. ``html5lib.treebuilders.getTreeBuilder("dom")`` will
  return the default DOM treebuilder, which uses ``xml.dom.minidom``.

* Optional heuristic character encoding detection now based on
  ``charade`` for Python 2.6 - 3.3 compatibility.

* Optional ``Genshi`` treewalker support fixed.

* Many bugfixes, including:

  * #33: null in attribute value breaks XML AttValue;

  * #4: nested, indirect descendant, <button> causes infinite loop;

  * `Google Code 215
    <http://code.google.com/p/html5lib/issues/detail?id=215>`_: Properly
    detect seekable streams;

  * `Google Code 206
    <http://code.google.com/p/html5lib/issues/detail?id=206>`_: add
    support for <video preload=...>, <audio preload=...>;

  * `Google Code 205
    <http://code.google.com/p/html5lib/issues/detail?id=205>`_: add
    support for <video poster=...>;

  * `Google Code 202
    <http://code.google.com/p/html5lib/issues/detail?id=202>`_: Unicode
    file breaks InputStream.

* Source code is now mostly PEP 8 compliant.

* Test harness has been improved and now depends on ``nose``.

* Documentation updated and moved to https://html5lib.readthedocs.io/.


0.95
~~~~

Released on February 11, 2012


0.90
~~~~

Released on January 17, 2010


0.11.1
~~~~~~

Released on June 12, 2008


0.11
~~~~

Released on June 10, 2008


0.10
~~~~

Released on October 7, 2007


0.9
~~~

Released on March 11, 2007


0.2
~~~

Released on January 8, 2007

%package license
Summary: license components for the html5lib package.
Group: Default

%description license
license components for the html5lib package.


%package python
Summary: python components for the html5lib package.
Group: Default
Requires: html5lib-python3 = %{version}-%{release}

%description python
python components for the html5lib package.


%package python3
Summary: python3 components for the html5lib package.
Group: Default
Requires: python3-core
Provides: pypi(html5lib)

%description python3
python3 components for the html5lib package.


%prep
%setup -q -n html5lib-1.0.1
cd %{_builddir}/html5lib-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582936303
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/html5lib
cp %{_builddir}/html5lib-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/html5lib/5bd527c7e2297d365b33ea67a400b6ba995e3705
cp %{_builddir}/html5lib-1.0.1/html5lib/tests/testdata/LICENSE %{buildroot}/usr/share/package-licenses/html5lib/2260a4b28dc3f43e07fa45e20334b7cdcab77588
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/html5lib/2260a4b28dc3f43e07fa45e20334b7cdcab77588
/usr/share/package-licenses/html5lib/5bd527c7e2297d365b33ea67a400b6ba995e3705

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
