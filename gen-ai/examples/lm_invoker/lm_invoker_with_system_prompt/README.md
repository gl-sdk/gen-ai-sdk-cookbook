## ⚙️ Prerequisites

Please refer to prerequisites [here](../../../README.md).

## 🚀 Getting Started

1. **Clone the repository & open the directory**

   ```bash
   git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
   cd gen-ai-sdk-cookbook/gen-ai/examples/lm_invoker/lm_invoker_with_system_prompt
   ```

2. **Set UV authentication and install dependencies**  
   Run the appropriate setup script for your system:

   **For Unix-based systems (Linux, macOS):**
   ```bash
   ./setup.sh
   ```

   **For Windows:**
   ```cmd
   setup.bat
   ```

   *Alternatively, you can run these steps manually:*
   ```env
   UV_INDEX_GEN_AI_INTERNAL_USERNAME=oauth2accesstoken
   UV_INDEX_GEN_AI_INTERNAL_PASSWORD="$(gcloud auth print-access-token)"
   ```
   ```bash
   uv lock
   uv sync
   ```

3. **Prepare `.env` file**  
    Create a file called `.env`, then set the OpenAI API key as an environment variable.
    ```env
    OPENAI_API_KEY="..."      
    ```

4. **Run the example**

   ```bash
   uv run lm_invoker.py
   ```

5. **Expected Output**

   You should see a response similar to the following:

   ```log
   Response: Arrr, the capital o' Indonesia be Jakarta. Aye, there be plans to move the seat o' government to Nusantara in East Kalimantan, but for now Jakarta remains the capital.
   ```

## 📚 Reference
These examples are based on the [GL SDK Gitbook documentation Tutorial page](https://gdplabs.gitbook.io/sdk/tutorials/inference/lm-invoker).
