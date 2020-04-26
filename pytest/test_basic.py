import pytest

from source.defenitions_fib import lijstmaker_uit_posixpad_csv
from source.paden import pad_tmp

def test_lijstmaker():
    te_maken_lijst = lijstmaker_uit_posixpad_csv(pad_tmp)
    tegen_lijst = []
    assert te_maken_lijst == []