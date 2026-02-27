// ============================================================================
// SAMPLE: Hello - Simple greeting card
// ============================================================================
export const helloSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Card: { child: "content" },
          },
        },
        {
          id: "content",
          component: {
            Column: {
              children: ["header", "description", "divider", "footer"],
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
                literalString: `
                Welcome to A2UI! Try these commands:
                  \n• "typography" - Text styles
                  • "form" - Input fields
                  • "gallery" - Images
                  • "dashboard" - Stats layout
                  • "profile" - User profile
                  • "settings" - Config panel
                  • "hitl" - Approval flow
                  • "product" - Product card
                  • "layout" - Grid layouts
                  • "delete" - Surface deletion`,
              },
              usageHint: "body",
            },
          },
        },
        {
          id: "divider",
          component: {
            Divider: { axis: "horizontal" },
          },
        },
        {
          id: "footer",
          component: {
            Text: {
              text: {
                literalString: "Type any keyword above to see the demo!",
              },
              usageHint: "caption",
            },
          },
        },
      ],
    },
  },
  {
    beginRendering: {
      surfaceId: "main",
      root: "root",
    },
  },
];
