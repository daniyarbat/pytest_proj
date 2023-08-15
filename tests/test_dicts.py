import pytest
from utils import dicts

def test_existing_key():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, "vcs") == "mercurial"

def test_existing_key_with_default():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, "vcs", "git") == "mercurial"

def test_non_existing_key_with_default():
    data = {}
    assert dicts.get_val(data, "vcs", "git") == "git"
