"use client";

import { useRef, useEffect } from "react";
import { Conversation } from "@/types/chat";
import { A2UIContent } from "./A2UIContent";
import { A2UIMessage } from "glchat-a2ui-react-renderer";
import MessageBubble from "./MessageBubble";
import MessageInput from "./MessageInput";
import { Bot } from "lucide-react";

interface ChatWindowProps {
  conversation: Conversation | null;
  onSendMessage: (content: string) => void;
  isLoading: boolean;
  streamingText: string;
  streamingA2UIMessages: object[];
}

export default function ChatWindow({
  conversation,
  onSendMessage,
  isLoading,
  streamingText,
  streamingA2UIMessages,
}: ChatWindowProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [conversation?.messages, streamingText, streamingA2UIMessages]);

  if (!conversation) {
    return (
      <div className="flex-1 flex items-center justify-center bg-white">
        <div className="text-center space-y-4">
          <div className="w-16 h-16 rounded-2xl bg-emerald-100 flex items-center justify-center mx-auto">
            <Bot size={32} className="text-emerald-600" />
          </div>
          <h2 className="text-xl font-semibold text-gray-900">A2UI Chat Assistant</h2>
          <p className="text-gray-400 text-sm max-w-sm">
            Start a new conversation or select one from the sidebar.
          </p>
        </div>
      </div>
    );
  }

  const isStreaming = !!(streamingText || streamingA2UIMessages.length > 0);

  return (
    <div className="flex-1 flex flex-col bg-white h-full">
      <header className="border-b border-gray-200 px-6 py-3 bg-white">
        <h1 className="text-sm font-semibold truncate text-gray-900">
          {conversation.title}
        </h1>
      </header>

      <div className="flex-1 overflow-y-auto">
        <div className="max-w-3xl mx-auto">
          {conversation.messages.map((msg) => (
            <MessageBubble key={msg.id} message={msg} />
          ))}

          {isLoading && !isStreaming && (
            <div className="flex gap-4 px-4 py-6 bg-gray-50">
              <div className="w-8 h-8 rounded-full bg-emerald-600 flex items-center justify-center shrink-0">
                <Bot size={16} className="text-white" />
              </div>
              <div className="flex items-center gap-1 pt-2">
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0ms]" />
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:150ms]" />
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:300ms]" />
              </div>
            </div>
          )}

          {isStreaming && (
            <div className="flex gap-4 px-4 py-6 bg-gray-50">
              <div className="w-8 h-8 rounded-full bg-emerald-600 flex items-center justify-center shrink-0">
                <Bot size={16} className="text-white" />
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-sm font-semibold mb-1 text-gray-900">Assistant</p>

                {streamingText && (
                  <div className="text-sm text-gray-700 leading-relaxed whitespace-pre-wrap">
                    {streamingText}
                    {streamingA2UIMessages.length === 0 && (
                      <span className="animate-pulse ml-0.5 text-gray-400">▌</span>
                    )}
                  </div>
                )}

                {streamingA2UIMessages.length > 0 && (
                  <div className="mt-3">
                    <A2UIContent
                      messages={streamingA2UIMessages as A2UIMessage[]}
                      onUserAction={(event) => {
                        console.log("User action during stream:", event);
                      }}
                    />
                  </div>
                )}
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      <MessageInput
        onSendMessage={onSendMessage}
        isLoading={isLoading || isStreaming}
      />
    </div>
  );
}
