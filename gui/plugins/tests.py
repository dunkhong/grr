#!/usr/bin/env python
# Copyright 2011 Google Inc. All Rights Reserved.

"""This module loads all the selenium tests for the GUI."""



# pylint: disable=W0611
from grr.gui.plugins import acl_manager_test
from grr.gui.plugins import container_viewer_test
from grr.gui.plugins import crash_view_test
from grr.gui.plugins import cron_view_test
from grr.gui.plugins import fileview_test
from grr.gui.plugins import flow_management_test
from grr.gui.plugins import hunt_view_test
from grr.gui.plugins import inspect_test
from grr.gui.plugins import new_hunt_test
from grr.gui.plugins import notifications_test
from grr.gui.plugins import statistics_test
from grr.gui.plugins import timeline_view_test