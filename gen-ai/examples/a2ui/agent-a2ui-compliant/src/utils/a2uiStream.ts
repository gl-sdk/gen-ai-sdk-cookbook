import { ChatMessage } from "@/types/chat";

type SampleType =
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

function detectSampleType(input: string): SampleType {
  const lower = input.toLowerCase();
  if (lower.includes("typography") || lower.includes("text")) return "typography";
  if (lower.includes("form") || lower.includes("input") || lower.includes("field")) return "form";
  if (lower.includes("gallery") || lower.includes("image")) return "gallery";
  if (lower.includes("dashboard") || lower.includes("stats")) return "dashboard";
  if (lower.includes("profile") || lower.includes("user")) return "profile";
  if (lower.includes("settings") || lower.includes("config")) return "settings";
  if (lower.includes("hitl") || lower.includes("approval")) return "hitl";
  if (lower.includes("product") || lower.includes("card")) return "product";
  if (lower.includes("layout") || lower.includes("grid")) return "layout";
  if (lower.includes("delete") || lower.includes("remove")) return "delete-surface";
  return "hello";
}

export interface StreamCallbacks {
  onTextChunk: (text: string) => void;
  onA2UIMessage: (message: object) => void;
  onComplete: (finalMessage: ChatMessage) => void;
}

export async function simulateA2UIStream(
  userInput: string,
  messageId: string,
  getSampleMessages: (type: SampleType) => object[],
  getDeleteSurfaceAction: () => object[],
  callbacks: StreamCallbacks
) {
  const sampleType = detectSampleType(userInput);
  const messages = getSampleMessages(sampleType);

  const textContent = `Showing A2UI sample: ${sampleType}`;
  const words = textContent.split(" ");
  for (let i = 0; i < words.length; i++) {
    await delay(50);
    callbacks.onTextChunk(words.slice(0, i + 1).join(" "));
  }

  await delay(500);

  const allA2UIMessages: object[] = [];
  for (const message of messages) {
    allA2UIMessages.push(message);
    callbacks.onA2UIMessage(message);
    await delay(300);
  }

  if (sampleType === "delete-surface") {
    await delay(3000);
    const deleteActions = getDeleteSurfaceAction();
    for (const action of deleteActions) {
      allA2UIMessages.push(action);
      callbacks.onA2UIMessage(action);
    }
  }

  const finalMessage: ChatMessage = {
    id: messageId,
    role: "assistant",
    content: textContent,
    a2uiMessages: allA2UIMessages,
    timestamp: Date.now(),
  };

  callbacks.onComplete(finalMessage);
}

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export { detectSampleType };
export type { SampleType };
