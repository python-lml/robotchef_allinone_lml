import sys

from mock import patch

PY2 = sys.version_info[0] == 2

if PY2:
    from StringIO import StringIO
else:
    from io import StringIO


@patch("sys.stdout", new_callable=StringIO)
def test_cornish_scone(stdout):
    arguments = ["robotchef", "Cornish Scone"]
    from robotchef_allinone_lml.main import main

    with patch.object(sys, "argv", arguments):
        main()
        assert stdout.getvalue() == "I can bake Cornish Scone\n"
