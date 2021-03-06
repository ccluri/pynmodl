import os
from textx.metamodel import metamodel_from_file

mm = metamodel_from_file(
    os.path.join(os.path.dirname(__file__), '../../grammar/units.tx'))


def test_unit():
    from textwrap import dedent
    u = dedent('''UNITS {
        (mV) = (millivolt)
        (mA) = (milliamp)
    }
    ''')
    ud = mm.model_from_str(u).unit_defs[1]
    l = ud.name
    r = ud.base_unit
    assert((l, r) == ('(mA)', '(milliamp)'))

