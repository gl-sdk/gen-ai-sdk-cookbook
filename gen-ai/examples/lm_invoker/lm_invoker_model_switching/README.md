## ⚙️ Prerequisites

Please refer to prerequisites [here](../../../README.md).

## 🚀 Getting Started

1. **Clone the repository & open the directory**

   ```bash
   git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
   cd gen-ai-sdk-cookbook/gen-ai/examples/lm_invoker/lm_invoker_model_switching
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
    ANTHROPIC_API_KEY="..."
    GOOGLE_API_KEY="..."
    OPENAI_API_KEY="..."   
    ```

5. **Run the example**

   ```bash
   uv run lm_invoker.py
   ```

   You can try using the different model IDs to switch between model providers!

6. **Expected Output**

   You should see a response similar to the following:

   ```log
   Response: Jakarta. 
   ```

## 📚 Reference
These examples are based on the [GL SDK Gitbook documentation Tutorial page](https://gdplabs.gitbook.io/sdk/tutorials/inference/lm-invoker).
