from tasks.dict_tasks.check_in import check_in


def test_check_in(new_set):
    assert check_in(new_set, 2)
    assert not check_in(new_set, 500)
