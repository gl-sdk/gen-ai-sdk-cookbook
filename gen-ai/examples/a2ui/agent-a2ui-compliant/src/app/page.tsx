"use client";

import { useState, useCallback } from "react";
import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";import { simulateA2UIStream } from "@/utils/a2uiStream";
import { Conversation, ChatMessage } from "@/types/chat";
import { dummyConversations } from "@/data/dummyData";
import { getDeleteSurfaceAction, getSampleMessages } from "@/data/a2uiDummyResponse";

export default function Home() {
  const [conversations, setConversations] =
    useState<Conversation[]>(dummyConversations);
  const [activeConversationId, setActiveConversationId] = useState<string>(
    dummyConversations[0]?.id ?? ""
  );
  const [isLoading, setIsLoading] = useState(false);
  const [streamingText, setStreamingText] = useState("");
  const [streamingA2UIMessages, setStreamingA2UIMessages] = useState<object[]>(
    []
  );

  const activeConversation =
    conversations.find((c) => c.id === activeConversationId) ?? null;

  const handleSendMessage = useCallback(
    async (content: string) => {
      if (!activeConversationId) return;

      const userMessage: ChatMessage = {
        id: `msg-${Date.now()}`,
        role: "user",
        content,
        a2uiMessages: [],
        timestamp: Date.now(),
      };

      setConversations((prev) =>
        prev.map((conv) =>
          conv.id === activeConversationId
            ? { ...conv, messages: [...conv.messages, userMessage] }
            : conv
        )
      );

      setIsLoading(true);
      setStreamingText("");
      setStreamingA2UIMessages([]);

      const assistantMsgId = `msg-${Date.now() + 1}`;

      await simulateA2UIStream(
        content,
        assistantMsgId,
        getSampleMessages,
        getDeleteSurfaceAction,
        {
          onTextChunk: (text: string) => {
            setIsLoading(false);
            setStreamingText(text);
          },
          onA2UIMessage: (message: object) => {
            setStreamingA2UIMessages((prev) => [...prev, message]);
          },
          onComplete: (finalMessage: ChatMessage) => {
            setConversations((prev) =>
              prev.map((conv) =>
                conv.id === activeConversationId
                  ? {
                      ...conv,
                      messages: [...conv.messages, finalMessage],
                    }
                  : conv
              )
            );
            setStreamingText("");
            setStreamingA2UIMessages([]);
            setIsLoading(false);
          },
        }
      );
    },
    [activeConversationId]
  );

  const handleNewConversation = () => {
    const newConv: Conversation = {
      id: `conv-${Date.now()}`,
      title: "New Conversation",
      messages: [],
    };
    setConversations((prev) => [newConv, ...prev]);
    setActiveConversationId(newConv.id);
  };

  return (
    <main className="flex h-screen overflow-hidden">
      <Sidebar
        conversations={conversations}
        activeConversationId={activeConversationId}
        onSelectConversation={setActiveConversationId}
        onNewConversation={handleNewConversation}
      />
      <ChatWindow
        conversation={activeConversation}
        onSendMessage={handleSendMessage}
        isLoading={isLoading}
        streamingText={streamingText}
        streamingA2UIMessages={streamingA2UIMessages}
      />
    </main>
  );
}
