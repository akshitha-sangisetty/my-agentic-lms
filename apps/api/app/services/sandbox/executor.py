"""
Code sandbox executor — manages Firecracker microVM lifecycle for student code.
"""


async def execute_code(code: str, language: str, test_suite: str | None = None) -> dict:
    """Execute student code in an isolated Firecracker microVM.

    Returns: {"stdout": str, "stderr": str, "exit_code": int,
              "test_results": [...], "execution_time_ms": int}
    """
    # TODO(agent): Implement Firecracker sandbox execution:
    #   1. Select VM image for language (python, javascript, java, cpp)
    #   2. Boot Firecracker microVM (<125ms target)
    #   3. Write student code to VM filesystem
    #   4. If test_suite provided, write test file
    #   5. Execute with resource limits:
    #      - CPU: 1 vCPU
    #      - Memory: 256 MB
    #      - Time: 30 seconds max
    #      - Network: disabled
    #      - Disk: 50 MB
    #   6. Capture stdout/stderr
    #   7. Parse test results if test suite was run
    #   8. Destroy VM (no persistent state)
    return {
        "stdout": "",
        "stderr": "Sandbox not implemented",
        "exit_code": 1,
        "test_results": None,
        "execution_time_ms": 0,
    }
