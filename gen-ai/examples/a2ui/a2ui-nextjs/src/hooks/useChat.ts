import { useState, useCallback, useEffect, useRef } from "react";
import { simulateA2UIStream } from "@/utils/a2uiMockStream";
import { ChatMessage } from "@/types/chat";

const initialMessage: ChatMessage = {
  id: "msg-init",
  role: "user",
  content: "hello",
  a2uiMessages: [],
  timestamp: Date.now(),
};

export function useChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([initialMessage]);
  const [isLoading, setIsLoading] = useState(true);
  const [streamingText, setStreamingText] = useState("");
  const [streamingA2UIMessages, setStreamingA2UIMessages] = useState<object[]>([]);
  const hasInit = useRef(false);

  const streamCallbacks = useCallback(() => ({
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
  }), []);

  // Stream the initial "hello" response on mount
  useEffect(() => {
    if (hasInit.current) return;
    hasInit.current = true;

    simulateA2UIStream("hello", "msg-init-response", streamCallbacks());
  }, [streamCallbacks]);

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

    await simulateA2UIStream(content, `msg-${Date.now() + 1}`, streamCallbacks());
  }, [streamCallbacks]);

  return { messages, isLoading, streamingText, streamingA2UIMessages, sendMessage };
}
