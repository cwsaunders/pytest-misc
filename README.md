# pytest-misc
Miscellaneous Pytest Code<br><br>

Running Pytest:<br>
1. pytest (FILENAME) (-v)           # Add -v for different information<br>
2. py.test          # Faster version of pytest (FILENAME) etc<br>
3. pytest (FILENAME::FUNCTION NAME)             # Only test specific function within file<br>
4. pytest -v -k "(FUNCTION NAME AFTER TEST_ KEYWORD)"           # Only test specific function(s) thayt match the keyword<br>
5. pytest -v -m (MARKER NAME)           # Run tests that have marker decorators (i.g pytest.mark.number)<br>
6. pytest -v -x             # Exit test after failure<br>
7. pytest -v --maxfail=(NUMBER)         # exit after specific number of failed tests<br>
8. pytest -v -s             # use print statements designated within testing code<br>
9. pytest -v -q             # Quiet mode. Only shows how many tests passed/failed<br>


<br>
Pytest Convention Notes:<br>
1. test_ prefix required before tests within test file && test file name.<br>
2.<br><br>

Running unittest:<br>
1. python -m unittest (FILENAME)<br>
2. python (FILENAME) # Assuming the __name__ = __main__ unittest. etc etc etc