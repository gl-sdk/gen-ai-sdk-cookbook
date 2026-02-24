"use client";

import { Conversation } from "@/types/chat";
import { MessageSquare, Plus } from "lucide-react";

interface SidebarProps {
  conversations: Conversation[];
  activeConversationId: string;
  onSelectConversation: (id: string) => void;
  onNewConversation: () => void;
}

export default function Sidebar({
  conversations,
  activeConversationId,
  onSelectConversation,
  onNewConversation,
}: SidebarProps) {
  return (
    <aside className="w-72 bg-gray-50 border-r border-gray-200 flex flex-col h-full">
      <div className="p-4 border-b border-gray-200">
        <button
          onClick={onNewConversation}
          className="w-full flex items-center gap-2 px-4 py-2.5 rounded-lg border border-gray-300 hover:bg-gray-100 transition-colors text-sm cursor-pointer text-gray-700"
        >
          <Plus size={16} />
          New Chat
        </button>
      </div>

      <nav className="flex-1 overflow-y-auto p-2 space-y-1">
        {conversations.map((conv) => (
          <button
            key={conv.id}
            onClick={() => onSelectConversation(conv.id)}
            className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-left transition-colors cursor-pointer ${
              activeConversationId === conv.id
                ? "bg-gray-200 text-gray-900"
                : "text-gray-500 hover:bg-gray-100 hover:text-gray-700"
            }`}
          >
            <MessageSquare size={16} className="shrink-0" />
            <span className="truncate">{conv.title}</span>
          </button>
        ))}
      </nav>

      <div className="p-4 border-t border-gray-200 text-xs text-gray-400 text-center">
        A2UI Chat Demo v1.0
      </div>
    </aside>
  );
}