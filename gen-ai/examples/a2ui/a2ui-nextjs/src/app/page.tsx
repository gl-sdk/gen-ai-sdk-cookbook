"use client";

import { useState, useCallback } from "react";
import ChatWindow from "@/components/ChatWindow";
import { simulateA2UIStream } from "@/utils/a2uiMockStream";
import { ChatMessage } from "@/types/chat";

export default function Home() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [streamingText, setStreamingText] = useState("");
  const [streamingA2UIMessages, setStreamingA2UIMessages] = useState<object[]>(
    [],
  );

  const handleSendMessage = useCallback(async (content: string) => {
    const userMessage: ChatMessage = {
      id: `msg-${Date.now()}`,
      role: "user",
      content,
      a2uiMessages: [],
      timestamp: Date.now(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);
    setStreamingText("");
    setStreamingA2UIMessages([]);

    await simulateA2UIStream(content, `msg-${Date.now() + 1}`, {
      onTextChunk: (text: string) => {
        setStreamingText(text);
      },
      onA2UIMessage: (message: object) => {
        setStreamingA2UIMessages((prev) => [...prev, message]);
      },
      onComplete: (finalMessage: ChatMessage) => {
        setMessages((prev) => [...prev, finalMessage]);
        setStreamingText("");
        setStreamingA2UIMessages([]);
        setIsLoading(false);
      },
    });
  }, []);

  return (
    <main className="h-screen overflow-hidden">
      <ChatWindow
        messages={messages}
        onSendMessage={handleSendMessage}
        isLoading={isLoading}
        streamingText={streamingText}
        streamingA2UIMessages={streamingA2UIMessages}
      />
    </main>
  );
}
