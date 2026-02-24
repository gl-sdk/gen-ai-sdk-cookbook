export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  a2uiMessages: object[];
  timestamp: number;
}

export interface Conversation {
  id: string;
  title: string;
  messages: ChatMessage[];
}
