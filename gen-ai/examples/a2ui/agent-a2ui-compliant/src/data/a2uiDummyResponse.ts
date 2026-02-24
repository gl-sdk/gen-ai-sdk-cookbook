/*
  a2uiDummyResponse.ts

  This file contains A2UI dummy response samples.
  It simulates the stream response from the backend with A2UI messages (data_type: 'a2ui').

  You can use this file to test the A2UI renderer in your local environment
  following the "How to test" section in this PR description (https://github.com/GDP-ADMIN/glchat/pull/7871).
*/
export async function sendA2UIMessage(
  controller: ReadableStreamDefaultController,
  sanitizedInput: string,
) {
  const input = sanitizedInput.toLowerCase();

  // Determine which sample to show based on input
  const sampleType = detectSampleType(input);
  const messages = getSampleMessages(sampleType);

  // Send initial text response
  controller.enqueue({
    type: "text-delta",
    textDelta: JSON.stringify({
      conversation_id: null,
      user_message_id: null,
      assistant_message_id: null,
      created_date: new Date().getTime(),
      message: `Showing A2UI sample: ${sampleType}`,
      status: "response",
    }),
  });

  await new Promise((resolve) => setTimeout(resolve, 500));

  // Send A2UI messages
  for (const message of messages) {
    controller.enqueue({
      type: "text-delta",
      textDelta: JSON.stringify({
        conversation_id: null,
        user_message_id: null,
        assistant_message_id: null,
        created_date: new Date().getTime(),
        message: JSON.stringify({
          data_type: "a2ui",
          data_value: message,
        }),
        status: "data",
      }),
    });
    await new Promise((resolve) => setTimeout(resolve, 300));
  }

  // Handle delete surface demo
  if (sampleType === "delete-surface") {
    await new Promise((resolve) => setTimeout(resolve, 3000));
    for (const message of deleteSurfaceAction) {
      controller.enqueue({
        type: "text-delta",
        textDelta: JSON.stringify({
          conversation_id: null,
          user_message_id: null,
          assistant_message_id: null,
          created_date: new Date().getTime(),
          message: JSON.stringify({
            data_type: "a2ui",
            data_value: message,
          }),
          status: "data",
        }),
      });
    }
  }
}

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
  if (input.includes("typography") || input.includes("text"))
    return "typography";
  if (
    input.includes("form") ||
    input.includes("input") ||
    input.includes("field")
  )
    return "form";
  if (input.includes("gallery") || input.includes("image")) return "gallery";
  if (input.includes("dashboard") || input.includes("stats"))
    return "dashboard";
  if (input.includes("profile") || input.includes("user")) return "profile";
  if (input.includes("settings") || input.includes("config")) return "settings";
  if (input.includes("hitl") || input.includes("approval")) return "hitl";
  if (input.includes("product") || input.includes("card")) return "product";
  if (input.includes("layout") || input.includes("grid")) return "layout";
  if (input.includes("delete") || input.includes("remove"))
    return "delete-surface";
  return "hello";
}

// ============================================================================
// SAMPLE: Hello - Simple greeting card
// ============================================================================
const helloSample = [
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
                literalString:
                  'Welcome to A2UI! Try these commands:\n• "typography" - Text styles\n• "form" - Input fields\n• "gallery" - Images\n• "dashboard" - Stats layout\n• "profile" - User profile\n• "settings" - Config panel\n• "hitl" - Approval flow\n• "product" - Product card\n• "layout" - Grid layouts\n• "delete" - Surface deletion',
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

// ============================================================================
// SAMPLE: Typography - All text usage hints
// ============================================================================
const typographySample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Column: {
              children: [
                "h1-text",
                "h2-text",
                "h3-text",
                "h4-text",
                "h5-text",
                "divider-1",
                "body-text",
                "caption-text",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "h1-text",
          component: {
            Text: {
              text: { literalString: "Heading 1 - Main Title" },
              usageHint: "h1",
            },
          },
        },
        {
          id: "h2-text",
          component: {
            Text: {
              text: { literalString: "Heading 2 - Section Title" },
              usageHint: "h2",
            },
          },
        },
        {
          id: "h3-text",
          component: {
            Text: {
              text: { literalString: "Heading 3 - Subsection" },
              usageHint: "h3",
            },
          },
        },
        {
          id: "h4-text",
          component: {
            Text: {
              text: { literalString: "Heading 4 - Minor Heading" },
              usageHint: "h4",
            },
          },
        },
        {
          id: "h5-text",
          component: {
            Text: {
              text: { literalString: "Heading 5 - Small Heading" },
              usageHint: "h5",
            },
          },
        },
        {
          id: "divider-1",
          component: {
            Divider: { axis: "horizontal" },
          },
        },
        {
          id: "body-text",
          component: {
            Text: {
              text: {
                literalString:
                  "Body text is used for main content paragraphs. It provides comfortable reading for longer passages of text. This is the default style for most content.",
              },
              usageHint: "body",
            },
          },
        },
        {
          id: "caption-text",
          component: {
            Text: {
              text: {
                literalString:
                  "Caption text - Used for labels, hints, and supplementary information",
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

// ============================================================================
// SAMPLE: Form - All input field types
// ============================================================================
const formSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Card: { child: "form-content" },
          },
        },
        {
          id: "form-content",
          component: {
            Column: {
              children: [
                "form-header",
                "form-description",
                "divider-top",
                "name-field",
                "email-field",
                "password-field",
                "age-field",
                "bio-field",
                "date-field",
                "divider-mid",
                "checkbox-section",
                "divider-bottom",
                "button-row",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "form-header",
          component: {
            Text: {
              text: { literalString: "Registration Form" },
              usageHint: "h2",
            },
          },
        },
        {
          id: "form-description",
          component: {
            Text: {
              text: {
                literalString: "Complete all fields to create your account",
              },
              usageHint: "caption",
            },
          },
        },
        {
          id: "divider-top",
          component: { Divider: { axis: "horizontal" } },
        },
        {
          id: "name-field",
          component: {
            TextField: {
              label: { literalString: "Full Name" },
              text: { path: "/form/name" },
              textFieldType: "shortText",
            },
          },
        },
        {
          id: "email-field",
          component: {
            TextField: {
              label: { literalString: "Email Address" },
              text: { path: "/form/email" },
              textFieldType: "shortText",
              validationRegexp: "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$",
            },
          },
        },
        {
          id: "password-field",
          component: {
            TextField: {
              label: { literalString: "Password" },
              text: { path: "/form/password" },
              textFieldType: "obscured",
            },
          },
        },
        {
          id: "age-field",
          component: {
            TextField: {
              label: { literalString: "Age" },
              text: { path: "/form/age" },
              textFieldType: "number",
            },
          },
        },
        {
          id: "bio-field",
          component: {
            TextField: {
              label: { literalString: "Bio (Optional)" },
              text: { path: "/form/bio" },
              textFieldType: "longText",
            },
          },
        },
        {
          id: "date-field",
          component: {
            TextField: {
              label: { literalString: "Date of Birth" },
              text: { path: "/form/dob" },
              textFieldType: "date",
            },
          },
        },
        {
          id: "divider-mid",
          component: { Divider: { axis: "horizontal" } },
        },
        {
          id: "checkbox-section",
          component: {
            Column: {
              children: ["terms-checkbox", "newsletter-checkbox"],
              distribution: "start",
              alignment: "start",
            },
          },
        },
        {
          id: "terms-checkbox",
          component: {
            CheckBox: {
              label: { literalString: "I agree to the Terms of Service" },
              checked: { path: "/form/agreeTerms" },
            },
          },
        },
        {
          id: "newsletter-checkbox",
          component: {
            CheckBox: {
              label: { literalString: "Subscribe to newsletter" },
              checked: { path: "/form/newsletter" },
            },
          },
        },
        {
          id: "divider-bottom",
          component: { Divider: { axis: "horizontal" } },
        },
        {
          id: "button-row",
          component: {
            Row: {
              children: ["cancel-btn", "submit-btn"],
              distribution: "end",
              alignment: "center",
            },
          },
        },
        {
          id: "cancel-btn",
          component: {
            Button: {
              child: "cancel-text",
              action: { name: "form_cancel", context: {} },
              primary: false,
            },
          },
        },
        {
          id: "cancel-text",
          component: {
            Text: { text: { literalString: "Cancel" }, usageHint: "body" },
          },
        },
        {
          id: "submit-btn",
          component: {
            Button: {
              child: "submit-text",
              action: {
                name: "form_submit",
                context: [
                  { key: "name", value: { path: "/form/name" } },
                  { key: "email", value: { path: "/form/email" } },
                  {
                    key: "password",
                    value: { path: "/form/password" },
                  },
                  { key: "age", value: { path: "/form/age" } },
                  { key: "bio", value: { path: "/form/bio" } },
                  { key: "dob", value: { path: "/form/dob" } },
                  {
                    key: "agreeTerms",
                    value: { path: "/form/agreeTerms" },
                  },
                  {
                    key: "newsletter",
                    value: { path: "/form/newsletter" },
                  },
                ],
              },
              primary: true,
            },
          },
        },
        {
          id: "submit-text",
          component: {
            Text: {
              text: { literalString: "Create Account" },
              usageHint: "body",
            },
          },
        },
      ],
    },
  },
  {
    dataModelUpdate: {
      surfaceId: "main",
      contents: [
        {
          key: "form",
          valueMap: [
            { key: "name", valueString: "John Doe" },
            { key: "email", valueString: "john@example.com" },
            { key: "password", valueString: "" },
            { key: "age", valueInt: 25 },
            {
              key: "bio",
              valueString: "Software developer passionate about UI/UX.",
            },
            { key: "dob", valueString: "1999-01-15" },
            { key: "agreeTerms", valueBool: false },
            { key: "newsletter", valueBool: true },
          ],
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

// ============================================================================
// SAMPLE: Gallery - Image showcase with all fit types
// ============================================================================
const gallerySample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Column: {
              children: [
                "gallery-header",
                "hero-section",
                "divider-1",
                "thumbnails-section",
                "divider-2",
                "avatars-section",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "gallery-header",
          component: {
            Text: {
              text: { literalString: "Image Gallery" },
              usageHint: "h2",
            },
          },
        },
        // Hero image section
        {
          id: "hero-section",
          component: {
            Column: {
              children: ["hero-label", "hero-image"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "hero-label",
          component: {
            Text: {
              text: { literalString: "Hero Image (cover fit)" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "hero-image",
          component: {
            Image: {
              url: { path: "/gallery/heroUrl" },
              fit: "cover",
              usageHint: "hero",
            },
          },
        },
        {
          id: "divider-1",
          component: { Divider: { axis: "horizontal" } },
        },
        // Thumbnails section
        {
          id: "thumbnails-section",
          component: {
            Column: {
              children: ["thumbnails-label", "thumbnails-row"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "thumbnails-label",
          component: {
            Text: {
              text: { literalString: "Thumbnails (contain fit)" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "thumbnails-row",
          component: {
            Row: {
              children: ["thumb-1", "thumb-2", "thumb-3", "thumb-4"],
              distribution: "spaceEvenly",
              alignment: "center",
            },
          },
        },
        {
          id: "thumb-1",
          component: {
            Image: {
              url: {
                literalString: "https://picsum.photos/seed/a2ui1/150/150",
              },
              fit: "contain",
              usageHint: "thumbnail",
            },
          },
        },
        {
          id: "thumb-2",
          component: {
            Image: {
              url: {
                literalString: "https://picsum.photos/seed/a2ui2/150/150",
              },
              fit: "contain",
              usageHint: "thumbnail",
            },
          },
        },
        {
          id: "thumb-3",
          component: {
            Image: {
              url: {
                literalString: "https://picsum.photos/seed/a2ui3/150/150",
              },
              fit: "contain",
              usageHint: "thumbnail",
            },
          },
        },
        {
          id: "thumb-4",
          component: {
            Image: {
              url: {
                literalString: "https://picsum.photos/seed/a2ui4/150/150",
              },
              fit: "contain",
              usageHint: "thumbnail",
            },
          },
        },
        {
          id: "divider-2",
          component: { Divider: { axis: "horizontal" } },
        },
        // Avatars section
        {
          id: "avatars-section",
          component: {
            Column: {
              children: ["avatars-label", "avatars-row"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "avatars-label",
          component: {
            Text: {
              text: { literalString: "Avatars (avatar hint)" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "avatars-row",
          component: {
            Row: {
              children: ["avatar-1", "avatar-2", "avatar-3"],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        {
          id: "avatar-1",
          component: {
            Image: {
              url: { literalString: "https://i.pravatar.cc/100?img=1" },
              fit: "cover",
              usageHint: "avatar",
            },
          },
        },
        {
          id: "avatar-2",
          component: {
            Image: {
              url: { literalString: "https://i.pravatar.cc/100?img=2" },
              fit: "cover",
              usageHint: "avatar",
            },
          },
        },
        {
          id: "avatar-3",
          component: {
            Image: {
              url: { literalString: "https://i.pravatar.cc/100?img=3" },
              fit: "cover",
              usageHint: "avatar",
            },
          },
        },
      ],
    },
  },
  {
    dataModelUpdate: {
      surfaceId: "main",
      contents: [
        {
          key: "gallery",
          valueMap: [
            {
              key: "heroUrl",
              valueString: "https://picsum.photos/seed/hero/800/400",
            },
          ],
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

// ============================================================================
// SAMPLE: Dashboard - Stats and metrics layout
// ============================================================================
const dashboardSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Column: {
              children: [
                "dashboard-header",
                "stats-row",
                "divider",
                "details-section",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "dashboard-header",
          component: {
            Row: {
              children: ["header-text", "refresh-btn"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "header-text",
          component: {
            Text: {
              text: { literalString: "Analytics Dashboard" },
              usageHint: "h2",
            },
          },
        },
        {
          id: "refresh-btn",
          component: {
            Button: {
              child: "refresh-text",
              action: { name: "refresh_dashboard", context: {} },
              primary: false,
            },
          },
        },
        {
          id: "refresh-text",
          component: {
            Text: { text: { literalString: "Refresh" }, usageHint: "body" },
          },
        },
        // Stats cards row
        {
          id: "stats-row",
          component: {
            Row: {
              children: ["stat-card-1", "stat-card-2", "stat-card-3"],
              distribution: "spaceEvenly",
              alignment: "stretch",
            },
          },
        },
        // Stat Card 1 - Users
        {
          id: "stat-card-1",
          component: { Card: { child: "stat-1-content" } },
        },
        {
          id: "stat-1-content",
          component: {
            Column: {
              children: ["stat-1-label", "stat-1-value", "stat-1-change"],
              distribution: "center",
              alignment: "center",
            },
          },
        },
        {
          id: "stat-1-label",
          component: {
            Text: {
              text: { literalString: "Total Users" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "stat-1-value",
          component: {
            Text: { text: { path: "/stats/users" }, usageHint: "h1" },
          },
        },
        {
          id: "stat-1-change",
          component: {
            Text: {
              text: { literalString: "+12.5% from last month" },
              usageHint: "caption",
            },
          },
        },
        // Stat Card 2 - Revenue
        {
          id: "stat-card-2",
          component: { Card: { child: "stat-2-content" } },
        },
        {
          id: "stat-2-content",
          component: {
            Column: {
              children: ["stat-2-label", "stat-2-value", "stat-2-change"],
              distribution: "center",
              alignment: "center",
            },
          },
        },
        {
          id: "stat-2-label",
          component: {
            Text: { text: { literalString: "Revenue" }, usageHint: "caption" },
          },
        },
        {
          id: "stat-2-value",
          component: {
            Text: { text: { path: "/stats/revenue" }, usageHint: "h1" },
          },
        },
        {
          id: "stat-2-change",
          component: {
            Text: {
              text: { literalString: "+8.2% from last month" },
              usageHint: "caption",
            },
          },
        },
        // Stat Card 3 - Orders
        {
          id: "stat-card-3",
          component: { Card: { child: "stat-3-content" } },
        },
        {
          id: "stat-3-content",
          component: {
            Column: {
              children: ["stat-3-label", "stat-3-value", "stat-3-change"],
              distribution: "center",
              alignment: "center",
            },
          },
        },
        {
          id: "stat-3-label",
          component: {
            Text: { text: { literalString: "Orders" }, usageHint: "caption" },
          },
        },
        {
          id: "stat-3-value",
          component: {
            Text: { text: { path: "/stats/orders" }, usageHint: "h1" },
          },
        },
        {
          id: "stat-3-change",
          component: {
            Text: {
              text: { literalString: "+23.1% from last month" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "divider",
          component: { Divider: { axis: "horizontal" } },
        },
        // Details section
        {
          id: "details-section",
          component: {
            Column: {
              children: ["details-header", "details-row"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "details-header",
          component: {
            Text: { text: { literalString: "Quick Actions" }, usageHint: "h4" },
          },
        },
        {
          id: "details-row",
          component: {
            Row: {
              children: ["action-1", "action-2", "action-3"],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        {
          id: "action-1",
          component: {
            Button: {
              child: "action-1-text",
              action: { name: "view_reports", context: {} },
              primary: true,
            },
          },
        },
        {
          id: "action-1-text",
          component: {
            Text: {
              text: { literalString: "View Reports" },
              usageHint: "body",
            },
          },
        },
        {
          id: "action-2",
          component: {
            Button: {
              child: "action-2-text",
              action: { name: "export_data", context: {} },
              primary: false,
            },
          },
        },
        {
          id: "action-2-text",
          component: {
            Text: { text: { literalString: "Export Data" }, usageHint: "body" },
          },
        },
        {
          id: "action-3",
          component: {
            Button: {
              child: "action-3-text",
              action: { name: "settings", context: {} },
              primary: false,
            },
          },
        },
        {
          id: "action-3-text",
          component: {
            Text: { text: { literalString: "Settings" }, usageHint: "body" },
          },
        },
      ],
    },
  },
  {
    dataModelUpdate: {
      surfaceId: "main",
      contents: [
        {
          key: "stats",
          valueMap: [
            { key: "users", valueString: "12,847" },
            { key: "revenue", valueString: "$84,230" },
            { key: "orders", valueString: "1,429" },
          ],
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

// ============================================================================
// SAMPLE: Profile - User profile card
// ============================================================================
const profileSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: { Card: { child: "profile-content" } },
        },
        {
          id: "profile-content",
          component: {
            Column: {
              children: [
                "profile-header",
                "divider-1",
                "profile-details",
                "divider-2",
                "profile-actions",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        // Header with avatar and name
        {
          id: "profile-header",
          component: {
            Row: {
              children: ["profile-avatar", "profile-info"],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        {
          id: "profile-avatar",
          component: {
            Image: {
              url: { path: "/user/avatar" },
              fit: "cover",
              usageHint: "avatar",
            },
          },
        },
        {
          id: "profile-info",
          component: {
            Column: {
              children: ["profile-name", "profile-role", "profile-status"],
              distribution: "start",
              alignment: "start",
            },
          },
        },
        {
          id: "profile-name",
          component: {
            Text: { text: { path: "/user/name" }, usageHint: "h3" },
          },
        },
        {
          id: "profile-role",
          component: {
            Text: { text: { path: "/user/role" }, usageHint: "body" },
          },
        },
        {
          id: "profile-status",
          component: {
            Text: {
              text: { literalString: "🟢 Online", path: "/user/status" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "divider-1",
          component: { Divider: { axis: "horizontal" } },
        },
        // Profile details
        {
          id: "profile-details",
          component: {
            Column: {
              children: ["detail-email", "detail-location", "detail-joined"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "detail-email",
          component: {
            Row: {
              children: ["email-label", "email-value"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "email-label",
          component: {
            Text: { text: { literalString: "Email" }, usageHint: "caption" },
          },
        },
        {
          id: "email-value",
          component: {
            Text: { text: { path: "/user/email" }, usageHint: "body" },
          },
        },
        {
          id: "detail-location",
          component: {
            Row: {
              children: ["location-label", "location-value"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "location-label",
          component: {
            Text: { text: { literalString: "Location" }, usageHint: "caption" },
          },
        },
        {
          id: "location-value",
          component: {
            Text: { text: { path: "/user/location" }, usageHint: "body" },
          },
        },
        {
          id: "detail-joined",
          component: {
            Row: {
              children: ["joined-label", "joined-value"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "joined-label",
          component: {
            Text: { text: { literalString: "Joined" }, usageHint: "caption" },
          },
        },
        {
          id: "joined-value",
          component: {
            Text: { text: { path: "/user/joined" }, usageHint: "body" },
          },
        },
        {
          id: "divider-2",
          component: { Divider: { axis: "horizontal" } },
        },
        // Actions
        {
          id: "profile-actions",
          component: {
            Row: {
              children: ["edit-btn", "message-btn", "more-btn"],
              distribution: "spaceEvenly",
              alignment: "center",
            },
          },
        },
        {
          id: "edit-btn",
          component: {
            Button: {
              child: "edit-text",
              action: { name: "edit_profile", context: {} },
              primary: true,
            },
          },
        },
        {
          id: "edit-text",
          component: {
            Text: {
              text: { literalString: "Edit Profile" },
              usageHint: "body",
            },
          },
        },
        {
          id: "message-btn",
          component: {
            Button: {
              child: "message-text",
              action: { name: "send_message", context: {} },
              primary: false,
            },
          },
        },
        {
          id: "message-text",
          component: {
            Text: { text: { literalString: "Message" }, usageHint: "body" },
          },
        },
        {
          id: "more-btn",
          component: {
            Button: {
              child: "more-text",
              action: { name: "more_options", context: {} },
              primary: false,
            },
          },
        },
        {
          id: "more-text",
          component: {
            Text: { text: { literalString: "..." }, usageHint: "body" },
          },
        },
      ],
    },
  },
  {
    dataModelUpdate: {
      surfaceId: "main",
      contents: [
        {
          key: "user",
          valueMap: [
            { key: "avatar", valueString: "https://i.pravatar.cc/200?img=8" },
            { key: "name", valueString: "Sarah Chen" },
            { key: "role", valueString: "Senior Product Designer" },
            { key: "status", valueString: "🟢 Online" },
            { key: "email", valueString: "sarah.chen@company.com" },
            { key: "location", valueString: "San Francisco, CA" },
            { key: "joined", valueString: "January 2023" },
          ],
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

// ============================================================================
// SAMPLE: Settings - Configuration panel with checkboxes
// ============================================================================
const settingsSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Column: {
              children: [
                "settings-header",
                "divider-top",
                "notifications-section",
                "divider-mid",
                "privacy-section",
                "divider-bottom",
                "save-row",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "settings-header",
          component: {
            Text: { text: { literalString: "⚙️ Settings" }, usageHint: "h2" },
          },
        },
        {
          id: "divider-top",
          component: { Divider: { axis: "horizontal" } },
        },
        // Notifications section
        {
          id: "notifications-section",
          component: {
            Column: {
              children: [
                "notifications-header",
                "email-notif",
                "push-notif",
                "sms-notif",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "notifications-header",
          component: {
            Text: { text: { literalString: "Notifications" }, usageHint: "h4" },
          },
        },
        {
          id: "email-notif",
          component: {
            CheckBox: {
              label: { literalString: "Email notifications" },
              checked: { path: "/settings/emailNotif" },
            },
          },
        },
        {
          id: "push-notif",
          component: {
            CheckBox: {
              label: { literalString: "Push notifications" },
              checked: { path: "/settings/pushNotif" },
            },
          },
        },
        {
          id: "sms-notif",
          component: {
            CheckBox: {
              label: { literalString: "SMS notifications" },
              checked: { path: "/settings/smsNotif" },
            },
          },
        },
        {
          id: "divider-mid",
          component: { Divider: { axis: "horizontal" } },
        },
        // Privacy section
        {
          id: "privacy-section",
          component: {
            Column: {
              children: [
                "privacy-header",
                "public-profile",
                "show-email",
                "show-activity",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "privacy-header",
          component: {
            Text: { text: { literalString: "Privacy" }, usageHint: "h4" },
          },
        },
        {
          id: "public-profile",
          component: {
            CheckBox: {
              label: { literalString: "Make profile public" },
              checked: { path: "/settings/publicProfile" },
            },
          },
        },
        {
          id: "show-email",
          component: {
            CheckBox: {
              label: { literalString: "Show email on profile" },
              checked: { path: "/settings/showEmail" },
            },
          },
        },
        {
          id: "show-activity",
          component: {
            CheckBox: {
              label: { literalString: "Show activity status" },
              checked: { path: "/settings/showActivity" },
            },
          },
        },
        {
          id: "divider-bottom",
          component: { Divider: { axis: "horizontal" } },
        },
        // Save row
        {
          id: "save-row",
          component: {
            Row: {
              children: ["reset-btn", "save-btn"],
              distribution: "end",
              alignment: "center",
            },
          },
        },
        {
          id: "reset-btn",
          component: {
            Button: {
              child: "reset-text",
              action: { name: "reset_settings", context: {} },
              primary: false,
            },
          },
        },
        {
          id: "reset-text",
          component: {
            Text: {
              text: { literalString: "Reset to Default" },
              usageHint: "body",
            },
          },
        },
        {
          id: "save-btn",
          component: {
            Button: {
              child: "save-text",
              action: {
                name: "save_settings",
                context: {
                  emailNotif: { path: "/settings/emailNotif" },
                  pushNotif: { path: "/settings/pushNotif" },
                  smsNotif: { path: "/settings/smsNotif" },
                  publicProfile: { path: "/settings/publicProfile" },
                  showEmail: { path: "/settings/showEmail" },
                  showActivity: { path: "/settings/showActivity" },
                },
              },
              primary: true,
            },
          },
        },
        {
          id: "save-text",
          component: {
            Text: {
              text: { literalString: "Save Changes" },
              usageHint: "body",
            },
          },
        },
      ],
    },
  },
  {
    dataModelUpdate: {
      surfaceId: "main",
      contents: [
        {
          key: "settings",
          valueMap: [
            { key: "emailNotif", valueBool: true },
            { key: "pushNotif", valueBool: true },
            { key: "smsNotif", valueBool: false },
            { key: "publicProfile", valueBool: true },
            { key: "showEmail", valueBool: false },
            { key: "showActivity", valueBool: true },
          ],
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

// ============================================================================
// SAMPLE: HITL - Human-in-the-loop approval workflow
// ============================================================================
const hitlSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Column: {
              children: ["hitl-header", "hitl-card", "action-card"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "hitl-header",
          component: {
            Row: {
              children: ["header-icon", "header-text"],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        {
          id: "header-icon",
          component: {
            Text: { text: { literalString: "⚠️" }, usageHint: "h2" },
          },
        },
        {
          id: "header-text",
          component: {
            Text: {
              text: { literalString: "Approval Required" },
              usageHint: "h2",
            },
          },
        },
        // Request details card
        {
          id: "hitl-card",
          component: { Card: { child: "hitl-card-content" } },
        },
        {
          id: "hitl-card-content",
          component: {
            Column: {
              children: [
                "request-title",
                "request-id",
                "divider-1",
                "request-details",
                "divider-2",
                "request-reason",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "request-title",
          component: {
            Text: { text: { path: "/hitl/title" }, usageHint: "h4" },
          },
        },
        {
          id: "request-id",
          component: {
            Text: { text: { path: "/hitl/requestId" }, usageHint: "caption" },
          },
        },
        {
          id: "divider-1",
          component: { Divider: { axis: "horizontal" } },
        },
        {
          id: "request-details",
          component: {
            Column: {
              children: [
                "detail-amount",
                "detail-from",
                "detail-to",
                "detail-time",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "detail-amount",
          component: {
            Row: {
              children: ["amount-label", "amount-value"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "amount-label",
          component: {
            Text: { text: { literalString: "Amount" }, usageHint: "caption" },
          },
        },
        {
          id: "amount-value",
          component: {
            Text: { text: { path: "/hitl/amount" }, usageHint: "body" },
          },
        },
        {
          id: "detail-from",
          component: {
            Row: {
              children: ["from-label", "from-value"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "from-label",
          component: {
            Text: { text: { literalString: "From" }, usageHint: "caption" },
          },
        },
        {
          id: "from-value",
          component: {
            Text: { text: { path: "/hitl/from" }, usageHint: "body" },
          },
        },
        {
          id: "detail-to",
          component: {
            Row: {
              children: ["to-label", "to-value"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "to-label",
          component: {
            Text: { text: { literalString: "To" }, usageHint: "caption" },
          },
        },
        {
          id: "to-value",
          component: {
            Text: { text: { path: "/hitl/to" }, usageHint: "body" },
          },
        },
        {
          id: "detail-time",
          component: {
            Row: {
              children: ["time-label", "time-value"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "time-label",
          component: {
            Text: {
              text: { literalString: "Expires in" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "time-value",
          component: {
            Text: { text: { path: "/hitl/timeLeft" }, usageHint: "body" },
          },
        },
        {
          id: "divider-2",
          component: { Divider: { axis: "horizontal" } },
        },
        {
          id: "request-reason",
          component: {
            Text: { text: { path: "/hitl/reason" }, usageHint: "body" },
          },
        },
        // Action card
        {
          id: "action-card",
          component: { Card: { child: "action-content" } },
        },
        {
          id: "action-content",
          component: {
            Column: {
              children: ["action-label-row", "action-buttons"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "action-label-row",
          component: {
            Row: {
              children: ["action-label", "hitl-timeout"],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        {
          id: "action-label",
          component: {
            Text: {
              text: { literalString: "Please review and take action:" },
              usageHint: "body",
            },
          },
        },
        {
          id: "hitl-timeout",
          component: {
            Timeout: {
              targetTimeUtc: { path: "/hitl/expiresAt" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "action-buttons",
          component: {
            Row: {
              children: ["approve-btn", "reject-btn", "escalate-btn"],
              distribution: "spaceEvenly",
              alignment: "center",
            },
          },
        },
        {
          id: "approve-btn",
          component: {
            Button: {
              child: "approve-text",
              action: {
                name: "hitl_decision",
                context: {
                  decision: { literalString: "approved" },
                  requestId: { path: "/hitl/requestId" },
                },
              },
              primary: true,
            },
          },
        },
        {
          id: "approve-text",
          component: {
            Text: { text: { literalString: "✓ Approve" }, usageHint: "body" },
          },
        },
        {
          id: "reject-btn",
          component: {
            Button: {
              child: "reject-text",
              action: {
                name: "hitl_decision",
                context: {
                  decision: { literalString: "rejected" },
                  requestId: { path: "/hitl/requestId" },
                },
              },
              primary: false,
              destructive: true,
            },
          },
        },
        {
          id: "reject-text",
          component: {
            Text: { text: { literalString: "✗ Reject" }, usageHint: "body" },
          },
        },
        {
          id: "escalate-btn",
          component: {
            Button: {
              child: "escalate-text",
              action: {
                name: "hitl_decision",
                context: {
                  decision: { literalString: "escalated" },
                  requestId: { path: "/hitl/requestId" },
                },
              },
              primary: false,
            },
          },
        },
        {
          id: "escalate-text",
          component: {
            Text: { text: { literalString: "↑ Escalate" }, usageHint: "body" },
          },
        },
      ],
    },
  },
  {
    dataModelUpdate: {
      surfaceId: "main",
      contents: [
        {
          key: "hitl",
          valueMap: [
            { key: "title", valueString: "Wire Transfer Request" },
            { key: "requestId", valueString: "REQ-2024-00847" },
            { key: "amount", valueString: "$15,000.00 USD" },
            { key: "from", valueString: "Operations Account (*4521)" },
            { key: "to", valueString: "Vendor Payment Account" },
            { key: "timeLeft", valueString: "4 minutes 32 seconds" },
            {
              key: "expiresAt",
              valueString: "2026-02-13T15:00:00.000Z",
            },
            {
              key: "reason",
              valueString:
                "This transfer exceeds the automatic approval limit of $10,000. Manual review required per company policy.",
            },
          ],
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

// ============================================================================
// SAMPLE: Product - E-commerce product card
// ============================================================================
const productSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: { Card: { child: "product-content" } },
        },
        {
          id: "product-content",
          component: {
            Column: {
              children: ["product-image", "product-details", "product-actions"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "product-image",
          component: {
            Image: {
              url: { path: "/product/image" },
              fit: "contain",
              usageHint: "hero",
            },
          },
        },
        {
          id: "product-details",
          component: {
            Column: {
              children: [
                "product-category",
                "product-name",
                "product-rating",
                "product-price",
                "product-description",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "product-category",
          component: {
            Text: { text: { path: "/product/category" }, usageHint: "caption" },
          },
        },
        {
          id: "product-name",
          component: {
            Text: { text: { path: "/product/name" }, usageHint: "h3" },
          },
        },
        {
          id: "product-rating",
          component: {
            Text: { text: { path: "/product/rating" }, usageHint: "caption" },
          },
        },
        {
          id: "product-price",
          component: {
            Row: {
              children: ["current-price", "original-price"],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        {
          id: "current-price",
          component: {
            Text: { text: { path: "/product/price" }, usageHint: "h2" },
          },
        },
        {
          id: "original-price",
          component: {
            Text: {
              text: { path: "/product/originalPrice" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "product-description",
          component: {
            Text: { text: { path: "/product/description" }, usageHint: "body" },
          },
        },
        // Quantity and actions
        {
          id: "product-actions",
          component: {
            Column: {
              children: ["quantity-row", "divider", "button-row"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "quantity-row",
          component: {
            Row: {
              children: ["quantity-label", "quantity-field"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        {
          id: "quantity-label",
          component: {
            Text: { text: { literalString: "Quantity" }, usageHint: "body" },
          },
        },
        {
          id: "quantity-field",
          component: {
            TextField: {
              text: { path: "/product/quantity" },
              textFieldType: "number",
            },
          },
        },
        {
          id: "divider",
          component: { Divider: { axis: "horizontal" } },
        },
        {
          id: "button-row",
          component: {
            Row: {
              children: ["wishlist-btn", "cart-btn"],
              distribution: "spaceEvenly",
              alignment: "center",
            },
          },
        },
        {
          id: "wishlist-btn",
          component: {
            Button: {
              child: "wishlist-text",
              action: {
                name: "add_to_wishlist",
                context: { productId: { path: "/product/id" } },
              },
              primary: false,
            },
          },
        },
        {
          id: "wishlist-text",
          component: {
            Text: { text: { literalString: "♡ Wishlist" }, usageHint: "body" },
          },
        },
        {
          id: "cart-btn",
          component: {
            Button: {
              child: "cart-text",
              action: {
                name: "add_to_cart",
                context: {
                  productId: { path: "/product/id" },
                  quantity: { path: "/product/quantity" },
                },
              },
              primary: true,
            },
          },
        },
        {
          id: "cart-text",
          component: {
            Text: {
              text: { literalString: "🛒 Add to Cart" },
              usageHint: "body",
            },
          },
        },
      ],
    },
  },
  {
    dataModelUpdate: {
      surfaceId: "main",
      contents: [
        {
          key: "product",
          valueMap: [
            { key: "id", valueString: "PRD-12345" },
            {
              key: "image",
              valueString: "https://picsum.photos/seed/product/400/300",
            },
            { key: "category", valueString: "Electronics > Audio" },
            { key: "name", valueString: "Premium Wireless Headphones" },
            { key: "rating", valueString: "★★★★☆ 4.5 (128 reviews)" },
            { key: "price", valueString: "$199.99" },
            { key: "originalPrice", valueString: "$249.99 (-20%)" },
            {
              key: "description",
              valueString:
                "Experience crystal-clear audio with active noise cancellation, 30-hour battery life, and premium comfort for all-day listening.",
            },
            { key: "quantity", valueInt: 1 },
          ],
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

// ============================================================================
// SAMPLE: Layout - Demonstrating Row/Column distribution and alignment
// ============================================================================
const layoutSample = [
  {
    surfaceUpdate: {
      surfaceId: "main",
      components: [
        {
          id: "root",
          component: {
            Column: {
              children: ["layout-header", "row-demos", "column-demos"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "layout-header",
          component: {
            Text: {
              text: { literalString: "Layout Examples" },
              usageHint: "h2",
            },
          },
        },
        // Row distribution demos
        {
          id: "row-demos",
          component: {
            Column: {
              children: [
                "row-header",
                "row-start",
                "row-center",
                "row-end",
                "row-between",
                "row-evenly",
              ],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "row-header",
          component: {
            Text: {
              text: { literalString: "Row Distribution" },
              usageHint: "h4",
            },
          },
        },
        // Row start
        {
          id: "row-start",
          component: {
            Card: { child: "row-start-content" },
          },
        },
        {
          id: "row-start-content",
          component: {
            Column: {
              children: ["row-start-label", "row-start-demo"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "row-start-label",
          component: {
            Text: {
              text: { literalString: "distribution: start" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "row-start-demo",
          component: {
            Row: {
              children: ["box-1a", "box-1b", "box-1c"],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        // Row center
        {
          id: "row-center",
          component: {
            Card: { child: "row-center-content" },
          },
        },
        {
          id: "row-center-content",
          component: {
            Column: {
              children: ["row-center-label", "row-center-demo"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "row-center-label",
          component: {
            Text: {
              text: { literalString: "distribution: center" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "row-center-demo",
          component: {
            Row: {
              children: ["box-2a", "box-2b", "box-2c"],
              distribution: "center",
              alignment: "center",
            },
          },
        },
        // Row end
        {
          id: "row-end",
          component: {
            Card: { child: "row-end-content" },
          },
        },
        {
          id: "row-end-content",
          component: {
            Column: {
              children: ["row-end-label", "row-end-demo"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "row-end-label",
          component: {
            Text: {
              text: { literalString: "distribution: end" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "row-end-demo",
          component: {
            Row: {
              children: ["box-3a", "box-3b", "box-3c"],
              distribution: "end",
              alignment: "center",
            },
          },
        },
        // Row spaceBetween
        {
          id: "row-between",
          component: {
            Card: { child: "row-between-content" },
          },
        },
        {
          id: "row-between-content",
          component: {
            Column: {
              children: ["row-between-label", "row-between-demo"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "row-between-label",
          component: {
            Text: {
              text: { literalString: "distribution: spaceBetween" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "row-between-demo",
          component: {
            Row: {
              children: ["box-4a", "box-4b", "box-4c"],
              distribution: "spaceBetween",
              alignment: "center",
            },
          },
        },
        // Row spaceEvenly
        {
          id: "row-evenly",
          component: {
            Card: { child: "row-evenly-content" },
          },
        },
        {
          id: "row-evenly-content",
          component: {
            Column: {
              children: ["row-evenly-label", "row-evenly-demo"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "row-evenly-label",
          component: {
            Text: {
              text: { literalString: "distribution: spaceEvenly" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "row-evenly-demo",
          component: {
            Row: {
              children: ["box-5a", "box-5b", "box-5c"],
              distribution: "spaceEvenly",
              alignment: "center",
            },
          },
        },
        // Box components for demos
        ...[
          "1a",
          "1b",
          "1c",
          "2a",
          "2b",
          "2c",
          "3a",
          "3b",
          "3c",
          "4a",
          "4b",
          "4c",
          "5a",
          "5b",
          "5c",
        ].map((id) => ({
          id: `box-${id}`,
          component: {
            Button: {
              child: `box-${id}-text`,
              primary: false,
            },
          },
        })),
        ...[
          "1a",
          "1b",
          "1c",
          "2a",
          "2b",
          "2c",
          "3a",
          "3b",
          "3c",
          "4a",
          "4b",
          "4c",
          "5a",
          "5b",
          "5c",
        ].map((id) => ({
          id: `box-${id}-text`,
          component: {
            Text: { text: { literalString: `[${id}]` }, usageHint: "caption" },
          },
        })),
        // Column demos
        {
          id: "column-demos",
          component: {
            Column: {
              children: ["col-header", "col-demos-row"],
              distribution: "start",
              alignment: "stretch",
            },
          },
        },
        {
          id: "col-header",
          component: {
            Text: {
              text: { literalString: "Column Alignment" },
              usageHint: "h4",
            },
          },
        },
        {
          id: "col-demos-row",
          component: {
            Row: {
              children: ["col-start-card", "col-center-card", "col-end-card"],
              distribution: "spaceEvenly",
              alignment: "stretch",
            },
          },
        },
        {
          id: "col-start-card",
          component: { Card: { child: "col-start-content" } },
        },
        {
          id: "col-start-content",
          component: {
            Column: {
              children: [
                "col-start-label",
                "col-start-item-1",
                "col-start-item-2",
              ],
              distribution: "start",
              alignment: "start",
            },
          },
        },
        {
          id: "col-start-label",
          component: {
            Text: {
              text: { literalString: "align: start" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "col-start-item-1",
          component: {
            Text: { text: { literalString: "Item 1" }, usageHint: "body" },
          },
        },
        {
          id: "col-start-item-2",
          component: {
            Text: { text: { literalString: "Item 2" }, usageHint: "body" },
          },
        },
        {
          id: "col-center-card",
          component: { Card: { child: "col-center-content" } },
        },
        {
          id: "col-center-content",
          component: {
            Column: {
              children: [
                "col-center-label",
                "col-center-item-1",
                "col-center-item-2",
              ],
              distribution: "start",
              alignment: "center",
            },
          },
        },
        {
          id: "col-center-label",
          component: {
            Text: {
              text: { literalString: "align: center" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "col-center-item-1",
          component: {
            Text: { text: { literalString: "Item 1" }, usageHint: "body" },
          },
        },
        {
          id: "col-center-item-2",
          component: {
            Text: { text: { literalString: "Item 2" }, usageHint: "body" },
          },
        },
        {
          id: "col-end-card",
          component: { Card: { child: "col-end-content" } },
        },
        {
          id: "col-end-content",
          component: {
            Column: {
              children: ["col-end-label", "col-end-item-1", "col-end-item-2"],
              distribution: "start",
              alignment: "end",
            },
          },
        },
        {
          id: "col-end-label",
          component: {
            Text: {
              text: { literalString: "align: end" },
              usageHint: "caption",
            },
          },
        },
        {
          id: "col-end-item-1",
          component: {
            Text: { text: { literalString: "Item 1" }, usageHint: "body" },
          },
        },
        {
          id: "col-end-item-2",
          component: {
            Text: { text: { literalString: "Item 2" }, usageHint: "body" },
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

// ============================================================================
// SAMPLE: Delete Surface - Multiple surfaces with deletion
// ============================================================================
const deleteSurfaceSample = [
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

const deleteSurfaceAction = [
  {
    deleteSurface: {
      surfaceId: "temporary",
    },
  },
];

const samples: Record<SampleType, object[]> = {
  typography: typographySample,
  form: formSample,
  gallery: gallerySample,
  dashboard: dashboardSample,
  profile: profileSample,
  settings: settingsSample,
  hitl: hitlSample,
  product: productSample,
  layout: layoutSample,
  "delete-surface": deleteSurfaceSample,
  hello: helloSample,
};

export function getSampleMessages(type: SampleType): object[] {
  return samples[type] ?? helloSample;
}

export function getDeleteSurfaceAction(): object[] {
  return deleteSurfaceAction;
}
