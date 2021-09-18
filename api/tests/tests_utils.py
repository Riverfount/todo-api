import pytest

from api.utils.pydantic_oid import PyObjectId


def test_validate_object_id_ok():
    o_id = '60a693cfdd6b08c271d48bbe'
    assert PyObjectId.validate(o_id)


def test_validate_object_id_raise_type_error():
    o_id = '1'
    with pytest.raises(TypeError) as err:
        PyObjectId.validate(o_id)
        assert err.value == 'ObjectId required or invalid'
