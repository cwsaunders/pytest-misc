# pytest-misc
Miscellaneous Pytest Code<br><br>

Running:<br>
1. pytest (FILENAME) (-v)           # Add -v for different information<br>
2. py.test          # Faster version of pytest (FILENAME) etc<br>
3. pytest (FILENAME::FUNCTION NAME)             # Only test specific function within file<br>
4. pytest -v -k "(FUNCTION NAME AFTER TEST_ KEYWORD)"           # Only test specific function(s) thayt match the keyword<br>
5. pytest -v -m (MARKER NAME)           # Run tests that have marker decorators (i.g pytest.mark.number)<br>
6. pytest -v -x             # Exit test after failure<br>
7. pytest -v --maxfail=(NUMBER)         # exit after specific number of failed tests<br>

<br>
Convention Notes:<br>
1. test_ prefix required before tests within test file && test file name.<br>
2.