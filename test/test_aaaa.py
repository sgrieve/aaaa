import pytest
from aaaa import aaaa


class Testaaaa():
    @pytest.mark.parametrize('length', [1, 2, 3, 4, 5])
    def test_output_length(self, length):
        names = aaaa(length)
        assert len(next(names)) == length

    @pytest.mark.parametrize('length', [1, 2, 3, 4, 5])
    def test_total_size(self, length):
        names = aaaa(length)

        assert len(names._sequence) == (26 ** length)

    def test_init_no_arg(self):
        names = aaaa()
        assert next(names) == 'aa'

    def test_next(self):
        names = aaaa(3)

        next(names)
        next(names)
        next(names)
        next(names)

        assert next(names) == 'aae'

    def test_loop(self):
        names = aaaa(3)

        for n in names:
            name = n

        assert name == 'zzz'

    def test_out_of_bounds(self):
        names = aaaa(1)

        with pytest.raises(StopIteration):
            for _ in range(30):
                next(names)

    def test_zero_length_arg(self):
        names = aaaa(0)

        assert next(names) == ''
