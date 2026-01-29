from io import StringIO
import sys
import structures as st


class TestAssessment3:

    def test_unique_numbers_basic(self):
        assert st.unique_numbers([1, 2, 2, 3, 4, 4]) == {1, 2, 3, 4}

    def test_unique_numbers_empty(self):
        assert st.unique_numbers([]) == set()

    def test_unique_numbers_single(self):
        assert st.unique_numbers([5]) == {5}

    def test_word_lengths_basic(self):
        assert st.word_lengths(["apple", "banana", "kiwi"]) == {
            "apple": 5,
            "banana": 6,
            "kiwi": 4
        }

    def test_word_lengths_empty(self):
        assert st.word_lengths([]) == {}

    def test_format_report_basic(self):
        assert st.format_report("Zinhle", 85) == "Student: Zinhle | Score: 85%"

    def test_format_report_zero(self):
        assert st.format_report("Alex", 0) == "Student: Alex | Score: 0%"

    def test_recursive_sum_basic(self):
        assert st.recursive_sum([1, 2, 3, 4]) == 10

    def test_recursive_sum_single(self):
        assert st.recursive_sum([5]) == 5

    def test_recursive_sum_empty(self):
        assert st.recursive_sum([]) == 0

    def test_group_by_parity(self):
        assert st.group_by_parity([1, 2, 3, 4, 5]) == {
            "even": [2, 4],
            "odd": [1, 3, 5]
        }

    def test_group_by_parity_empty(self):
        assert st.group_by_parity([]) == {"even": [], "odd": []}

    def test_countdown_print(self, monkeypatch):
        captured = StringIO()
        sys.stdout = captured
        st.countdown(3)
        sys.stdout = sys.__stdout__

        output = captured.getvalue().strip().split("\n")
        assert output == ["3", "2", "1", "Blast off!"]

    def test_student_average_basic(self):
        data = {
            "Math": 80,
            "Science": 70,
            "English": 90
        }
        assert st.student_average(data) == "Average Score: 80.00"

    def test_student_average_empty(self):
        assert st.student_average({}) == "No data available."
