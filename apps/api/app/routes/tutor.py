from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from jose import JWTError, jwt

from app.config import settings

router = APIRouter()


@router.websocket("/tutor/chat")
async def tutor_chat(websocket: WebSocket) -> None:
    # Authenticate via query param token
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=4001, reason="Missing authentication token")
        return

    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        student_id = payload["sub"]
    except (JWTError, KeyError):
        await websocket.close(code=4001, reason="Invalid authentication token")
        return

    await websocket.accept()

    # TODO(agent): Implement full Socratic tutor chat:
    #   1. Receive student message with assignment_id
    #   2. Retrieve relevant context from Weaviate (RAG)
    #   3. Load conversation history from session
    #   4. Call TutorAgent with context + history + message
    #   5. Stream response back via WebSocket
    #   6. After N failed attempts, offer hint with cost
    #   See packages/agents/agents/tutor/ for agent definition
    #   See packages/rag/rag/retriever.py for RAG retrieval

    try:
        while True:
            data = await websocket.receive_json()
            msg_type = data.get("type", "message")

            if msg_type == "message":
                # Placeholder response
                await websocket.send_json({
                    "type": "stream",
                    "content": "I'm the Socratic tutor. This feature is under development. "
                    "What concept are you trying to understand?",
                    "citations": [],
                })
                await websocket.send_json({
                    "type": "done",
                    "message_id": "placeholder",
                })
    except WebSocketDisconnect:
        pass
