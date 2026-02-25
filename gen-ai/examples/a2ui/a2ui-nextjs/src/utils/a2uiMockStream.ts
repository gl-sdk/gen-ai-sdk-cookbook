import { ChatMessage } from "@/types/chat";
import { detectSampleType, getDeleteSurfaceAction, getMockMessage } from "./a2uiMockMessage";

export interface StreamCallbacks {
  onTextChunk: (text: string) => void;
  onA2UIMessage: (message: object) => void;
  onComplete: (finalMessage: ChatMessage) => void;
}

export async function simulateA2UIStream(
  userInput: string,
  messageId: string,
  callbacks: StreamCallbacks,
) {
  const sampleType = detectSampleType(userInput);
  const messages = getMockMessage(sampleType);

  const textContent = `Showing A2UI sample: ${userInput}`;
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
