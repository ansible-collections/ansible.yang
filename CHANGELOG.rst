=====================================
Ansible Yang Collection Release Notes
=====================================

.. contents:: Topics

v3.0.0
======

Release Summary
---------------

Starting from this release, the minimum `ansible-core` version this collection requires is `2.15.0`. The last known version compatible with ansible-core<2.15 is v2.0.0.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

v2.0.0
======

Release Summary
---------------

Starting from this release, the minimum `ansible-core` version this collection requires is `2.14.0`. The last known version compatible with ansible-core<2.14 is `v1.2.1`.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

Bugfixes
--------

- Update bindep dependencies, and improve pyang import checks.

v1.2.1
======

Release Summary
---------------

Re-releasing version 1.2.0, as 1.2.1.

v1.2.0
======

Release Summary
---------------

Releasing version 1.2.0, featuring various maintenance updates.

v1.1.0
======

Minor Changes
-------------

- Added unit test for xml2json, json2xml and spec lookup plugins (https://github.com/ansible-collections/community.yang/pull/50)
- Refactored module_utils to fix ansible-test sanity issues (https://github.com/ansible-collections/community.yang/pull/50)
- added optional attribute for fetch action to continue if it hits a module that cannot be found
- community.yang.configure - Since ``configure`` module is built on top of ``netconf_config`` we add a new option argument, ``netconf_options``, allowing passing options directly to ``netconf_config``.

Bugfixes
--------

- Fixed json2xml py3 compatibility issues (https://github.com/ansible-collections/community.yang/pull/45)
- Sort yang_files to address dependency issue (https://github.com/ansible-collections/community.yang/pull/46)

v1.0.0
======

Major Changes
-------------

- Add modules get, fetch, configure, generate_spec to ansible.yang collections.
- Added configure module to push json format configuration on to remote host over netconf connection.
