"use client";

import { ChatMessage } from "@/types/chat";
import { A2UIContent } from "./A2UIContent";
import { A2UIMessage } from "glchat-a2ui-react-renderer";
import { Bot, User } from "lucide-react";

interface MessageBubbleProps {
  message: ChatMessage;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <div className={`flex gap-4 px-4 py-6 ${isUser ? "" : "bg-gray-50"}`}>
      <div
        className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 ${
          isUser ? "bg-blue-600 text-white" : "bg-emerald-600 text-white"
        }`}
      >
        {isUser ? <User size={16} /> : <Bot size={16} />}
      </div>

      <div className="flex-1 min-w-0">
        <p className="text-sm font-semibold mb-1 text-gray-900">
          {isUser ? "You" : "Assistant"}
        </p>

        {message.content && (
          <div className="text-sm text-gray-700 leading-relaxed whitespace-pre-wrap">
            {message.content}
          </div>
        )}

        {message.a2uiMessages.length > 0 && (
          <div className="mt-3">
            <A2UIContent
              messages={message.a2uiMessages as A2UIMessage[]}
              onUserAction={(event) => {
                console.log("User action from history:", event);
              }}
            />
          </div>
        )}
      </div>
    </div>
  );
}