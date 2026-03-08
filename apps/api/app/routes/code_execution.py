from fastapi import APIRouter, Depends

from app.dependencies import CurrentUser, get_current_student
from app.schemas.submissions import CodeExecutionRequest, CodeExecutionResponse

router = APIRouter()


@router.post("/code/execute", response_model=CodeExecutionResponse)
async def execute_code(
    body: CodeExecutionRequest,
    student: CurrentUser = Depends(get_current_student),
) -> CodeExecutionResponse:
    # TODO(agent): Implement Firecracker sandbox code execution:
    #   1. Spin up Firecracker microVM with appropriate language runtime
    #   2. Write student code to VM filesystem
    #   3. If assignment_id provided, copy hidden test suite into VM
    #   4. Execute code with resource limits (CPU, memory, time)
    #   5. Capture stdout/stderr + test results
    #   6. Tear down VM
    #   7. If compiler/runtime error, call TutorAgent to translate error
    #   See services/sandbox/executor.py for VM management
    #   See infra/docker/Dockerfile.sandbox for sandbox image
    return CodeExecutionResponse(
        stdout="Code execution sandbox not yet implemented.",
        stderr="",
        exit_code=0,
        test_results=None,
        execution_time_ms=0,
    )
