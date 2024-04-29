from hypothesis import given, strategies as st
import os
from datetime import datetime, timedelta
import mining

# Test cases
def test_giveTimeStamp():
    assert isinstance(mining.giveTimeStamp(), str)

@given(st.text(), st.sampled_from(['TEST', 'REAL']))
def test_deleteRepo(dirName, type_):
    # This will simulate directory operations in a safe environment
    mining.deleteRepo('/tmp/' + dirName, type_)

@given(st.text(), st.text())
def test_dumpContentIntoFile(strP, fileP):
    filePath = '/tmp/' + fileP
    result = mining.dumpContentIntoFile(strP, filePath)
    assert os.path.exists(filePath)
    assert isinstance(result, int)

@given(st.lists(st.integers()), st.integers(min_value=1, max_value=100))
def test_makeChunks(the_list, size_):
    chunks = list(mining.makeChunks(the_list, size_))
    assert all(len(chunk) <= size_ for chunk in chunks)

@given(st.datetimes(), st.datetimes())
def test_days_between(d1_, d2_):
    days = mining.days_between(d1_, d2_)
    assert isinstance(days, int)
    assert days == abs((d2_ - d1_).days)

if __name__ == "__main__":
    test_giveTimeStamp()
    test_deleteRepo()
    test_dumpContentIntoFile()
    test_makeChunks()
    test_days_between()