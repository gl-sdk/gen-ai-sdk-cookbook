## ⚙️ Prerequisites

Please refer to prerequisites [here](../../../README.md).

## 🚀 Getting Started

1. **Clone the repository & open the directory**

   ```bash
   git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
   cd gen-ai-sdk-cookbook/gen-ai/tutorials/lm_invoker
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
   uv run 001_quickstart.py
   ```
   

6. **Expected Output**

   You should see a response similar to the following:

   ```log
   Response: Jakarta.
   ```

## 📚 Reference
These examples are based on the [GL SDK Gitbook documentation How-to-Guide page](https://gdplabs.gitbook.io/sdk/tutorials/inference/lm-invoker).
