'use client';

import { useState, useRef, useEffect } from 'react';

interface Message {
  id: string;
  role: 'student' | 'tutor';
  content: string;
  citations?: { source: string; page: number }[];
}

interface TutorChatProps {
  assignmentId?: string;
  token: string;
}

export function TutorChat({ assignmentId, token }: TutorChatProps) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [connected, setConnected] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // TODO(agent): Implement WebSocket connection:
    //   const ws = new WebSocket(`ws://localhost:8000/api/v1/tutor/chat?token=${token}`);
    //   wsRef.current = ws;
    //   ws.onopen = () => setConnected(true);
    //   ws.onmessage = (e) => handleMessage(JSON.parse(e.data));
    //   ws.onclose = () => setConnected(false);
    //   return () => ws.close();
  }, [token]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = () => {
    if (!input.trim()) return;

    const newMsg: Message = {
      id: Date.now().toString(),
      role: 'student',
      content: input,
    };
    setMessages((prev) => [...prev, newMsg]);

    // TODO(agent): Send via WebSocket
    // wsRef.current?.send(JSON.stringify({ type: 'message', content: input, assignment_id: assignmentId }));

    setInput('');
  };

  return (
    <div className="flex flex-col h-full border rounded-xl bg-white dark:bg-gray-900">
      {/* Chat header */}
      <div className="px-4 py-3 border-b flex items-center justify-between">
        <div>
          <h3 className="font-semibold">AI Tutor</h3>
          <span className={`text-xs ${connected ? 'text-success' : 'text-gray-400'}`}>
            {connected ? 'Connected' : 'Offline'}
          </span>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <p className="text-center text-gray-400 py-8">
            Ask me anything about your course materials. I&apos;ll guide you with questions!
          </p>
        )}
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`flex ${msg.role === 'student' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[80%] px-4 py-2 rounded-2xl ${
                msg.role === 'student'
                  ? 'bg-brand-600 text-white'
                  : 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100'
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="p-4 border-t">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask a question..."
            className="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-500 dark:bg-gray-800 dark:border-gray-700"
          />
          <button
            onClick={sendMessage}
            className="px-4 py-2 bg-brand-600 text-white rounded-lg hover:bg-brand-700 transition-colors"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
