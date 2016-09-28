# coding=utf-8
from __future__ import unicode_literals

import grp
import os
import pwd

JUDGER_WORKSPACE_BASE = "/judger_run"
LOG_BASE = "/log"

COMPILER_LOG_PATH = os.path.join(LOG_BASE, "compile.log")
JUDGER_RUN_LOG_PATH = os.path.join(LOG_BASE, "judger.log")

LOW_PRIVILEDGE_UID = pwd.getpwnam("nobody").pw_uid
LOW_PRIVILEDGE_GID = grp.getgrnam("nogroup").gr_gid

TEST_CASE_DIR = "/test_case"
