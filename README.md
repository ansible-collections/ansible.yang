# Ansible Collection - ansible.yang

This repo hosts the `ansible.yang` Ansible Collection.

The collection includes the ansible plugins to help support Yang mainly with network devices.

<!--start requires_ansible-->

## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.14.0**.

For collections that support Ansible 2.9, please ensure you update your `network_os` to use the
fully qualified collection name (for example, `cisco.ios.ios`).
Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.

<!--end requires_ansible-->

### Supported connections

The Ansible yang collection supports `netconf` connections.

## Included content

<!--start collection content-->

### Lookup plugins

| Name                                                                                                                         | Description                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [ansible.yang.json2xml](https://github.com/ansible-collections/ansible.yang/blob/main/docs/ansible.yang.json2xml_lookup.rst) | Validates json configuration against yang data model and convert it to xml.                                                                   |
| [ansible.yang.spec](https://github.com/ansible-collections/ansible.yang/blob/main/docs/ansible.yang.spec_lookup.rst)         | This plugin reads the content of given yang document and generates json and xml configuration skeleton and a tree structure of yang document. |
| [ansible.yang.xml2json](https://github.com/ansible-collections/ansible.yang/blob/main/docs/ansible.yang.xml2json_lookup.rst) | Converts xml input to json structure output by mapping it against corresponding Yang model                                                    |

### Modules

| Name                                                                                                                                   | Description                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [ansible.yang.configure](https://github.com/ansible-collections/ansible.yang/blob/main/docs/ansible.yang.configure_module.rst)         | Reads the input configuration in JSON format and pushes to the remote host over netconf |
| [ansible.yang.fetch](https://github.com/ansible-collections/ansible.yang/blob/main/docs/ansible.yang.fetch_module.rst)                 | Fetch given yang model and it's dependencies                                            |
| [ansible.yang.generate_spec](https://github.com/ansible-collections/ansible.yang/blob/main/docs/ansible.yang.generate_spec_module.rst) | Generate JSON/XML schema and tree representation for given YANG model                   |
| [ansible.yang.get](https://github.com/ansible-collections/ansible.yang/blob/main/docs/ansible.yang.get_module.rst)                     | Fetch the device configuration and render it in JSON format defined by RFC7951          |

<!--end collection content-->

## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using the Ansible Yang collection, you need to install it with the `ansible-galaxy` CLI:

    ansible-galaxy collection install ansible.yang

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
---
collections:
  - name: ansible.yang
```

### Platforms test against

    1. Cisco IOSXR 6.1.3

### Use modules from the yang Collection in your playbooks

It's preferable to use content in this collection using their Fully Qualified Collection Namespace (FQCN), for example `ansible.yang.configure`:

```yaml
---
- hosts: iosxr
  gather_facts: false
  connection: ansible.netcommon.netconf

  tasks:
    - name: "Fetch given yang model and all the dependent models from remote host"
      ansible.yang.fetch:
        name: Cisco-IOS-XR-ifmgr-cfg

    - name: get interface configuration in json/xml format
      ansible.yang.get:
        filter: |
          <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"><interface-configuration>
          </interface-configuration></interface-configurations>
        file: "./files/cisco/iosxr/*.yang"
        search_path: "./files/cisco/iosxr"
      register: result

    - name: Configure interface description providing json input file
      ansible.yang.configure:
        config: "{{ lookup('file', config_file) }}"
        file: "{{ yang_file }}"
        search_path: "{{ search_path }}"
      register: result

    - name: Configure interface description with json input
      ansible.yang.configure:
        config:
          {
              "Cisco-IOS-XR-ifmgr-cfg:interface-configurations": {
                  "interface-configuration": [
                      {
                          "active": "act",
                          "description": "test for ansible 400",
                          "interface-name": "Loopback888",
                          "interface-virtual": [
                              null
                          ],
                          "shutdown": [
                              null
                          ]
                      },
                      {
                          "active": "act",
                          "description": "This interface is configures with Ansible",
                          "interface-name": "GigabitEthernet0/0/0/4"
                      }
                  ]
              }
          }
        file: "{{ yang_file }}"
        search_path: "{{ search_path }}"
      register: result

    - name: generate spec from open-config interface yang model data and represent in xml, json and yang tree
      ansible.yang.generate_spec:
        file: "{{ spec_yang_file }}"
        search_path: "{{ spec_search_path }}"
        doctype: config
        json_schema:
          path: "./output/{{ inventory_hostname }}/openconfig-interfaces-config.json"
          defaults: True
        xml_schema:
          path: "./output/{{ inventory_hostname }}/openconfig-interfaces-config.xml"
          defaults: True
          annotations: True
        tree_schema:
          path: "./output/{{ inventory_hostname }}/openconfig-interfaces-config.tree"t
```

For documentation on how to use individual modules and other content included in this collection, please see the links in the 'Included content' section earlier in this README.

## Testing and Development

If you want to develop new content for this collection or improve what's already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

### Testing with `ansible-test`

The `tests` directory contains configuration for running sanity and integration tests using [`ansible-test`](https://docs.ansible.com/ansible/latest/dev_guide/testing_integration.html).

To run these network integration tests, use ansible-test network-integration --inventory </path/to/inventory> <tests_to_run>:

    ansible-test network-integration  --inventory ~/myinventory -vvv <name of the plugin>

## Publishing New Versions

Releases are automatically built and pushed to Ansible Galaxy for any new tag. Before tagging a release, make sure to do the following:

1. Update `galaxy.yml` and this README's `requirements.yml` example with the new `version` for the collection.
2. Update the CHANGELOG:
3. Make sure you have [`antsibull-changelog`](https://pypi.org/project/antsibull-changelog/) installed.
4. Make sure there are fragments for all known changes in `changelogs/fragments`.
5. Run `antsibull-changelog release`.
6. Commit the changes and create a PR with the changes. Wait for tests to pass, then merge it once they have.
7. Tag the version in Git and push it to GitHub.
   ```
   After the version is published, verify it exists on the [Ansible Yang Community Collection Galaxy page](https://galaxy.ansible.com/ansible/yang).
   ```

### See Also:

- [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Ansible Yang collection repository](https://github.com/ansible-collections/ansible.yang).

1. Make changes
2. Detail changes in a [fragment](changelogs/fragments). [example](https://github.com/ansible-collections/ansible.yang/pull/58/files)
3. Submit PR

You can also join us on:

- IRC - the `#ansible-network` [libera.chat](https://libera.chat/) channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

## Changelogs

[Change log](changelogs/CHANGELOG.rst)

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible Collection Overview](https://github.com/ansible-collections/overview)
- [Ansible User Guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Support

As a Red Hat Ansible [Certified Content](https://catalog.redhat.com/software/search?target_platforms=Red%20Hat%20Ansible%20Automation%20Platform), this collection is entitled to [support](https://access.redhat.com/support/) through [Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) (AAP).

If a support case cannot be opened with Red Hat and the collection has been obtained either from [Galaxy](https://galaxy.ansible.com/ui/) or [GitHub](https://github.com/ansible-collections/ansible.yang), there is community support available at no charge.

You can join us on [#network:ansible.com](https://matrix.to/#/#network:ansible.com) room or the [Ansible Forum Network Working Group](https://forum.ansible.com/g/network-wg).

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
