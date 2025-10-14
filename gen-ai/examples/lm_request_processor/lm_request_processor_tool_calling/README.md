## ⚙️ Prerequisites

Please refer to prerequisites [here](../../../README.md).

## 🚀 Getting Started

1. **Clone the repository & open the directory**

   ```bash
   git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
   cd gen-ai-sdk-cookbook/gen-ai/examples/lm_request_processor/lm_request_processor_tool_calling
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

4. **Prepare `.env` file**  
    Create a file called `.env`, then set the OpenAI API key as an environment variable.
    ```env
    OPENAI_API_KEY="..."      
    ```

5. **Run the example**

   ```bash
   uv run tool_calling.py
   ```

6. **Expected Output**

   You should see a response similar to the following:

   ```log
   The result of the expression 10 + 20 * 0 - 4 is 6.
   ```

## 🚀 Reference
These examples are based on the [GL SDK Gitbook documentation How-to-Guide page](https://gdplabs.gitbook.io/sdk/how-to-guides/utilize-language-model-request-processor/extend-lm-capabilities-with-tools).
