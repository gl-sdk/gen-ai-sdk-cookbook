import { useState, useCallback } from "react";
import { simulateA2UIStream } from "@/utils/a2uiMockStream";
import { ChatMessage } from "@/types/chat";

export function useChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [streamingText, setStreamingText] = useState("");
  const [streamingA2UIMessages, setStreamingA2UIMessages] = useState<object[]>([]);

  const sendMessage = useCallback(async (content: string) => {
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

  return { messages, isLoading, streamingText, streamingA2UIMessages, sendMessage };
}
