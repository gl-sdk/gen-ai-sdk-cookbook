## ⚙️ Prerequisites

Please refer to prerequisites [here](../../../README.md).

## 🚀 Getting Started

1. **Clone the repository & open the directory**

   ```bash
   git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
   cd gen-ai-sdk-cookbook/gen-ai/examples/custom_component/
   ```

2. **Set UV authentication**  
   Since UV will need to be able to access our private registry to download the required packages, please also set the following environment variables:

   ```env
   UV_INDEX_GEN_AI_INTERNAL_USERNAME=oauth2accesstoken
   UV_INDEX_GEN_AI_INTERNAL_PASSWORD="$(gcloud auth print-access-token)"
   ```

3. **Install dependency via UV**

   ```bash
   uv lock
   uv sync
   ```

4. **Run the example**

   ```bash
   uv run custom_component.py
   ```

## 🚀 Reference

These examples are based on the [GL SDK Gitbook documentation How-to-Guide page](https://gdplabs.gitbook.io/sdk/how-to-guides/extend-lm-capabilities-with-custom-components).
