// ---- Value types ----
export interface LiteralStringValue {
  literalString: string;
}

export interface PathValue {
  path: string;
}

export type A2UIValue = LiteralStringValue | PathValue | (LiteralStringValue & PathValue);

// ---- Component types ----
export interface A2UITextComponent {
  Text: {
    text: A2UIValue;
    usageHint: "h1" | "h2" | "h3" | "h4" | "h5" | "body" | "caption";
  };
}

export interface A2UICardComponent {
  Card: {
    child: string;
  };
}

export interface A2UIColumnComponent {
  Column: {
    children: string[];
    distribution: "start" | "center" | "end" | "spaceBetween" | "spaceEvenly";
    alignment: "start" | "center" | "end" | "stretch";
  };
}

export interface A2UIRowComponent {
  Row: {
    children: string[];
    distribution: "start" | "center" | "end" | "spaceBetween" | "spaceEvenly";
    alignment: "start" | "center" | "end" | "stretch";
  };
}

export interface A2UIDividerComponent {
  Divider: {
    axis: "horizontal" | "vertical";
  };
}

export interface A2UIButtonComponent {
  Button: {
    child: string;
    action?: {
      name: string;
      context: Record<string, A2UIValue> | Array<{ key: string; value: A2UIValue }>;
    };
    primary: boolean;
    destructive?: boolean;
  };
}

export interface A2UITextFieldComponent {
  TextField: {
    label?: A2UIValue;
    text: A2UIValue;
    textFieldType: "shortText" | "longText" | "obscured" | "number" | "date";
    validationRegexp?: string;
  };
}

export interface A2UICheckBoxComponent {
  CheckBox: {
    label: A2UIValue;
    checked: A2UIValue;
  };
}

export interface A2UIImageComponent {
  Image: {
    url: A2UIValue;
    fit: "cover" | "contain" | "fill";
    usageHint: "hero" | "thumbnail" | "avatar";
  };
}

export interface A2UITimeoutComponent {
  Timeout: {
    targetTimeUtc: A2UIValue;
    usageHint: string;
  };
}

export type A2UIComponent =
  | A2UITextComponent
  | A2UICardComponent
  | A2UIColumnComponent
  | A2UIRowComponent
  | A2UIDividerComponent
  | A2UIButtonComponent
  | A2UITextFieldComponent
  | A2UICheckBoxComponent
  | A2UIImageComponent
  | A2UITimeoutComponent;

export interface A2UIComponentEntry {
  id: string;
  component: A2UIComponent;
}

// ---- Message types ----
export interface SurfaceUpdate {
  surfaceUpdate: {
    surfaceId: string;
    components: A2UIComponentEntry[];
  };
}

export interface DataModelUpdate {
  dataModelUpdate: {
    surfaceId: string;
    contents: Array<{
      key: string;
      valueMap: Array<{
        key: string;
        valueString?: string;
        valueInt?: number;
        valueBool?: boolean;
      }>;
    }>;
  };
}

export interface BeginRendering {
  beginRendering: {
    surfaceId: string;
    root: string;
  };
}

export interface DeleteSurface {
  deleteSurface: {
    surfaceId: string;
  };
}

export type A2UIMessage = SurfaceUpdate | DataModelUpdate | BeginRendering | DeleteSurface;

// ---- Surface state ----
export interface SurfaceState {
  surfaceId: string;
  components: Map<string, A2UIComponent>;
  dataModel: Map<string, Record<string, string | number | boolean>>;
  rootId: string | null;
  isRendering: boolean;
}