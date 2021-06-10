# Copyright (C) 2020,2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods,missing-class-docstring
# pylint: disable=missing-function-docstring
"""Test cases for the rule, BlockedModules.
"""
from rules import BlockedModules as TT
from tests import common


class Base:
    this_py: common.MaybeModNameT = __file__
    this_mod: common.MaybeModT = TT
    rule_memoized = ['blocked_modules']

    use_lint_v2 = True


class RuleTestCase(Base, common.RuleTestCase):
    pass


class CliTestCase(Base, common.CliTestCase):
    pass
