# $Id$
# Copyright (c) 2009 Oliver Beckstein <orbeckst@gmail.com>
# Released under the GNU Public License 3 (or higher, your choice)
# See the file COPYING for details.
"""
:mod:`analysis.plugins` -- Plugin Modules
=========================================

Classes for :class:`gromacs.analysis.core.Simulation` that provide
code to analyze trajectory data.

New analysis plugins should follow the API sketched out in
:mod:`gromacs.analysis.core`; see an example for use there.


List of plugins
---------------

Right now the number of plugins is limited. Feel free to contribute your own by
sending it to the `package author`_. You will be acknowledged in the list below.

.. _`package author`: oliver.beckstein@bioch.ox.ac.uk

==========================  =======================  ===============================
plugin                      author                   description
==========================  =======================  ===============================
:class:`CysAccessibility`   Oliver Beckstein [#OB]_  estimate accessibility of Cys
                                                     residues by water
:class:`Distances`          Oliver Beckstein [#OB]_  time series of distances
==========================  =======================  ===============================


.. rubric:: Footnotes
.. [#OB] oliver.beckstein@bioch.ox.ac.uk


Plugin classes
--------------

..autoclass:: CysAccessibility
  :members:
..autoclass:: Distances
  :members:


Developer notes
---------------

In principle all that needs to be done to automatically load plugins
is to add their name to :data:`__plugins__`. See the source code for
further comments and how the auto loading of plugins is done.

.. autodata:: __plugins__
.. autodata:: __plugin_classes__

"""
__docformat__ = "restructuredtext en"

#: All available plugin names are listed here. Because this is used to
#: automatically set up imports a module file *must* be named like the
#: plugin class it contains but in all lower case. For example, the
#: *Distances* plugin class is contained in the module *distances* (the
#: file ``plugins/distances.py``).
__plugins__ = ['CysAccessibility', 'Distances']
__all__ = []
__all__.extend(__plugins__)


# 1. Load all modules
#    (module is plugin name in lower case)
#    ('__import__(m.lower(), fromlist=[m])' does not work like 'from m.lower() import m'
_modules = dict([(p, __import__(p.lower(), globals(), locals())) for p in __plugins__])
# 2. Get the classes
#: Gives access to all available plugin classes (or use the module __dict__)
__plugin_classes__ = dict([(p, M.__dict__[p]) for p,M in _modules.items()])
# 3. add to the name space (bind classes to names)
globals().update(__plugin_classes__)

del p, M
del _modules


