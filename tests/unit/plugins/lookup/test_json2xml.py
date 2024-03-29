# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import os
import unittest

from ansible.errors import AnsibleLookupError

from ansible_collections.ansible.yang.plugins.lookup.json2xml import LookupModule


YANG_FILE_SEARCH_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "../../../fixtures/files",
)
OC_INTF_JSON_CONFIG_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "../../../fixtures/config/openconfig/interface_oc_json_valid.json",
)
OC_INTF_YANG_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "../../../fixtures/files/openconfig/interfaces/openconfig-interfaces.yang",
)
LOOKUP_VARIABLES = {}


class TestValidate(unittest.TestCase):
    def setUp(self):
        self._lp = LookupModule()

    def test_invalid_argspec(self):
        """Check passing invalid argspec"""

        # missing required arguments
        kwargs = {}
        with self.assertRaises(AnsibleLookupError) as error:
            self._lp.run(
                [OC_INTF_JSON_CONFIG_FILE_PATH],
                LOOKUP_VARIABLES,
                **kwargs,
            )
        self.assertIn(
            "value of 'yang_file' must be specified",
            str(error.exception),
        )

        # invalid json file value arguments
        kwargs = {"yang_file": OC_INTF_JSON_CONFIG_FILE_PATH}
        with self.assertRaises(AnsibleLookupError) as error:
            self._lp.run(["invalid path"], LOOKUP_VARIABLES, **kwargs)
        self.assertIn(
            "Failed to load json configuration",
            str(error.exception),
        )

    def test_valid_json2xml_data(self):
        """Check passing valid data as per criteria"""

        terms = [OC_INTF_JSON_CONFIG_FILE_PATH]
        variables = {}
        kwargs = {
            "yang_file": OC_INTF_YANG_FILE_PATH,
            "search_path": YANG_FILE_SEARCH_PATH,
        }
        result = self._lp.run(terms, variables, **kwargs)
        self.assertIn(
            '<nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"',
            result[0],
        )
