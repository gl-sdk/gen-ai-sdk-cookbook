"use client";

import { useRef, useEffect } from "react";
import { ChatMessage } from "@/types/chat";
import MessageBubble from "./MessageBubble";
import MessageInput from "./MessageInput";

interface ChatWindowProps {
  messages: ChatMessage[];
  onSendMessage: (content: string) => void;
  isLoading: boolean;
  streamingText: string;
  streamingA2UIMessages: object[];
}

// ---- Message List ----
function MessageList({ messages }: { messages: ChatMessage[] }) {
  return (
    <>
      {messages.map((msg) => (
        <MessageBubble key={msg.id} message={msg} />
      ))}
    </>
  );
}

// ---- Streaming Bubble ----
function StreamingBubble({
  streamingText,
  streamingA2UIMessages,
}: {
  streamingText: string;
  streamingA2UIMessages: object[];
}) {
  const isStreaming = !!(streamingText || streamingA2UIMessages.length > 0);
  if (!isStreaming) return null;

  return (
    <MessageBubble
      streamingText={streamingText}
      streamingA2UIMessages={streamingA2UIMessages}
    />
  );
}

// ---- Main ChatWindow ----
export default function ChatWindow({
  messages,
  onSendMessage,
  isLoading,
  streamingText,
  streamingA2UIMessages,
}: ChatWindowProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, streamingText, streamingA2UIMessages]);

  const isStreaming = !!(streamingText || streamingA2UIMessages.length > 0);

  return (
    <div className="flex flex-col bg-white h-full">
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-3xl mx-auto">
          <MessageList messages={messages} />

          <StreamingBubble
            streamingText={streamingText}
            streamingA2UIMessages={streamingA2UIMessages}
          />

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