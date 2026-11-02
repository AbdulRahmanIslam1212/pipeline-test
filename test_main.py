from main import add


class TestClass:
    def test_fail_add(self):
        assert add(2, 3) == 4

    def test_add(self):
        assert add(2, 3) == 5
