// ============================================================================
// SAMPLE: Delete Surface - Multiple surfaces with deletion
// ============================================================================
export const deleteSurfaceSample = [
  // Main surface
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "main-root",
          component: { Card: { child: "main-content" } },
        },
        {
          id: "main-content",
          component: {
            Column: {
              children: ["main-header", "main-body"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "main-header",
          component: {
            Text: { text: { literalString: "Main Surface" }, usageHint: "h3" },
          },
        },
        {
          id: "main-body",
          component: {
            Text: {
              text: {
                literalString:
                  "This surface will remain after the temporary one is deleted.",
              },
              usageHint: "body",
            },
          },
        },
      ],
    },
  },
  {
    beginRendering: {
      surfaceId: "main",
      root: "main-root",
    },
  },
  // Temporary surface
  {
    surfaceUpdate: {
      surfaceId: "temporary",
      components: [
        {
          id: "temp-root",
          component: { Card: { child: "temp-content" } },
        },
        {
          id: "temp-content",
          component: {
            Column: {
              children: ["temp-header", "temp-body", "temp-countdown"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "temp-header",
          component: {
            Text: {
              text: { literalString: "⏱️ Temporary Surface" },
              usageHint: "h3",
            },
          },
        },
        {
          id: "temp-body",
          component: {
            Text: {
              text: {
                literalString:
                  "This surface will be automatically deleted in 3 seconds...",
              },
              usageHint: "body",
            },
          },
        },
        {
          id: "temp-countdown",
          component: {
            Text: {
              text: { literalString: "Watch it disappear! 👀" },
              usageHint: "caption",
            },
          },
        },
      ],
    },
  },
  {
    beginRendering: {
      surfaceId: "temporary",
      root: "temp-root",
    },
  },
];
