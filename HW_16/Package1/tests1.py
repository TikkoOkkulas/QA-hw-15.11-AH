
import pytest

class TestPackOne:

    @pytest.mark.from_class
    def test_one(self):
        print(f'\nrun test 1')
        pass

    @pytest.mark.from_class
    def test_two(self):
        print('\nrun test 2')
        pass

    @pytest.mark.from_class
    def test_three(self):
        print('\nrun test 3')
        pass

    @pytest.mark.from_class
    def test_four(self):
        print('\nrun test 4')
        pass

    @pytest.mark.from_class
    def test_five(self):
        print('\nrun test 5')
        pass

