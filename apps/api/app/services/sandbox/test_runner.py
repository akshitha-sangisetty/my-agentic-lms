"""
Test runner — executes hidden test suites against student code.
"""


async def run_tests(code: str, test_suite: str, language: str) -> list[dict]:
    """Run hidden tests against student code.

    Returns: [{"name": "test_add", "passed": True, "output": "..."}]
    """
    # TODO(agent): Implement test execution:
    #   1. Combine student code + test suite
    #   2. Execute in sandbox
    #   3. Parse test framework output (pytest for Python, jest for JS)
    #   4. Return structured test results
    return []
