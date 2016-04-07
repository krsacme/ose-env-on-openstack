#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION='''
---
module: atomic_host
short_description: Manage the atomic host platform
description:
    - Manage the atomic host platform
version_added: "2.1"
author: "Saravanan KR @krsacme"
notes:
    - Host should be an atomic platform (verified by existence of '/run/ostree-booted' file)
requirements:
  - atomic
options:
    state:
        description:
          - The state of the atomic host to be in
        required: true
        choices: ["rollback", "status", "upgrade", "rebase"]
        default: null
'''

EXAMPLES = '''

# Upgrade the atomic host platform (atomic host upgrade)
- atomic_host: state=upgrade

'''

RETURN = '''
msg:
    description: The command standard output
    returned: always
    type: string
    sample: 'No upgrades available'
'''

import os
import sys

def core(module):
    state = module.params['state']
    args = ['atomic', 'host']
    args.append(state)

    out = {}
    err = {}
    rc = 0

    rc, out, err = module.run_command(args, check_rc=False)

    if rc == 77:
        module.exit_json(msg="No upgrades available")
    elif rc != 0:
        module.fail_json(rc=rc, msg=err)
    else:
        module.exit_json(msg=out)


def main():
    module = AnsibleModule(
                argument_spec = dict(
                    state = dict(default=None, choices=['rollback', 'status', 'upgrade', 'rebase'], required=True),
                )
            )

    # Verify that the platform is atomic host
    if not os.path.exists("/run/ostree-booted"):
      module.fail_json(msg="Module atomic is applicable only for Atomic Host Platforms only")

    try:
        core(module)
    except Exception, e:
        module.fail_json(msg=str(e))


# import module snippets
from ansible.module_utils.basic import *
main()
