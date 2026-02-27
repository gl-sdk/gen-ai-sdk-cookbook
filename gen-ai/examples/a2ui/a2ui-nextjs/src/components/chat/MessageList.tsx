"use client";

import { ChatMessage } from "@/types/chat";
import MessageBubble from "./MessageBubble";

export default function MessageList({ messages }: { messages: ChatMessage[] }) {
  return (
    <>
      {messages.map((msg) => (
        <MessageBubble key={msg.id} message={msg} />
      ))}
    </>
  );
}
