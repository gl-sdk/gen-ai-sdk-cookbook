import { Conversation } from "@/types/chat";

export const dummyConversations: Conversation[] = [
  {
    id: "conv-1",
    title: "A2UI Hello Demo",
    messages: [
      {
        id: "msg-1",
        role: "user",
        content: "hello",
        a2uiMessages: [],
        timestamp: Date.now() - 60000,
      },
      {
        id: "msg-2",
        role: "assistant",
        content: "Showing A2UI sample: hello",
        a2uiMessages: [
          {
            surfaceUpdate: {
              surfaceId: "main",
              components: [
                {
                  id: "root",
                  component: { Card: { child: "content" } },
                },
                {
                  id: "content",
                  component: {
                    Column: {
                      children: ["header", "description"],
                      distribution: "start",
                      alignment: "stretch",
                    },
                  },
                },
                {
                  id: "header",
                  component: {
                    Text: {
                      text: { literalString: "Hello! 👋" },
                      usageHint: "h2",
                    },
                  },
                },
                {
                  id: "description",
                  component: {
                    Text: {
                      text: {
                        literalString:
                          'Welcome to A2UI! Try: "typography", "form", "gallery", "dashboard", "profile", "settings", "hitl", "product", "layout", "delete"',
                      },
                      usageHint: "body",
                    },
                  },
                },
              ],
            },
          },
          {
            beginRendering: { surfaceId: "main", root: "root" },
          },
        ],
        timestamp: Date.now() - 59000,
      },
    ],
  },
  {
    id: "conv-2",
    title: "Dashboard Demo",
    messages: [],
  },
  {
    id: "conv-3",
    title: "Form Demo",
    messages: [],
  },
];
