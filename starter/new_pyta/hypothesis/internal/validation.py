# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Most of this work is copyright (C) 2013-2020 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.
#
# END HEADER

import decimal
import math
from numbers import Rational, Real

from hypothesis.errors import InvalidArgument
from hypothesis.internal.coverage import check_function


@check_function
def check_type(typ, arg, name):
    if not isinstance(arg, typ):
        if isinstance(typ, tuple):
            assert len(typ) >= 2, "Use bare type instead of len-1 tuple"
            typ_string = "one of %s" % (", ".join(t.__name__ for t in typ))
        else:
            typ_string = typ.__name__

            if typ_string == "SearchStrategy":
                from hypothesis.strategies import SearchStrategy

                # Use hypothesis.strategies._internal.strategies.check_strategy
                # instead, as it has some helpful "did you mean..." logic.
                assert typ is not SearchStrategy, "use check_strategy instead"

        raise InvalidArgument(
            "Expected %s but got %s=%r (type=%s)"
            % (typ_string, name, arg, type(arg).__name__)
        )


@check_function
def check_valid_integer(value, name):
    """Checks that value is either unspecified, or a valid integer.

    Otherwise raises InvalidArgument.
    """
    if value is None:
        return
    check_type(int, value, name)


@check_function
def check_valid_bound(value, name):
    """Checks that value is either unspecified, or a valid interval bound.

    Otherwise raises InvalidArgument.
    """
    if value is None or isinstance(value, (int, Rational)):
        return
    if not isinstance(value, (Real, decimal.Decimal)):
        raise InvalidArgument("%s=%r must be a real number." % (name, value))
    if math.isnan(value):
        raise InvalidArgument("Invalid end point %s=%r" % (name, value))


@check_function
def check_valid_magnitude(value, name):
    """Checks that value is either unspecified, or a non-negative valid
    interval bound.

    Otherwise raises InvalidArgument.
    """
    check_valid_bound(value, name)
    if value is not None and value < 0:
        raise InvalidArgument("%s=%r must not be negative." % (name, value))
    if value is None and name == "min_magnitude":
        from hypothesis._settings import note_deprecation

        note_deprecation(
            "min_magnitude=None is deprecated; use min_magnitude=0 "
            "or omit the argument entirely.",
            since="2020-05-13",
        )


@check_function
def try_convert(typ, value, name):
    if value is None:
        return None
    if isinstance(value, typ):
        return value
    try:
        return typ(value)
    except (TypeError, ValueError, ArithmeticError):
        raise InvalidArgument(
            "Cannot convert %s=%r of type %s to type %s"
            % (name, value, type(value).__name__, typ.__name__)
        )


@check_function
def check_valid_size(value, name):
    """Checks that value is either unspecified, or a valid non-negative size
    expressed as an integer.

    Otherwise raises InvalidArgument.
    """
    if value is None and name != "min_size":
        return
    check_type(int, value, name)
    if value < 0:
        raise InvalidArgument("Invalid size %s=%r < 0" % (name, value))


@check_function
def check_valid_interval(lower_bound, upper_bound, lower_name, upper_name):
    """Checks that lower_bound and upper_bound are either unspecified, or they
    define a valid interval on the number line.

    Otherwise raises InvalidArgument.
    """
    if lower_bound is None or upper_bound is None:
        return
    if upper_bound < lower_bound:
        raise InvalidArgument(
            "Cannot have %s=%r < %s=%r"
            % (upper_name, upper_bound, lower_name, lower_bound)
        )


@check_function
def check_valid_sizes(min_size, max_size):
    check_valid_size(min_size, "min_size")
    check_valid_size(max_size, "max_size")
    check_valid_interval(min_size, max_size, "min_size", "max_size")