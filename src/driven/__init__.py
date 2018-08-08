# -*- coding: utf-8 -*-

# Copyright (c) 2015 Novo Nordisk Foundation Center for Biosustainability,
# Technical University Denmark
# Copyright (c) 2018 Novo Nordisk Foundation Center for Biosustainability,
# Technical University Denmark
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Integrate omics' data with genome-scale constraint-based metabolic models."""

from __future__ import absolute_import

__author__ = 'Novo Nordisk Foundation Center for Biosustainability, ' \
             'Technical University Denmark'
__email__ = 'niso@biosustain.dtu.dk'

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from driven.data_sets import *
from driven.omics import *
from driven.utils import *
