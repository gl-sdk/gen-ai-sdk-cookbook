export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  a2uiMessages: object[];
  timestamp: number;
}

export type SampleType =
  | "typography"
  | "form"
  | "gallery"
  | "dashboard"
  | "profile"
  | "settings"
  | "hitl"
  | "product"
  | "layout"
  | "delete-surface"
  | "hello";