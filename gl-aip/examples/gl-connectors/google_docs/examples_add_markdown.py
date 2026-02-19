from dotenv import load_dotenv
import asyncio
import os

from glaip_sdk import Agent
from gllm_tools.mcp.client.langchain import LangchainMCPClient

load_dotenv()

DESIRED_TOOLS = {"google_docs_list_comments", "google_docs_summarize_comments", "google_docs_create_document", "google_docs_list_documents", "google_docs_get_document", "google_docs_update_document","google_docs_update_document_markdown"}

client = LangchainMCPClient({
    "google_docs": {
        "url": "https://connector.gdplabs.id/google_docs/mcp",
        "headers": {"Authorization": f"Bearer {os.getenv('GL_CONNECTORS_USER_TOKEN')}"},
    }
})

FILE_NAME= "Tech Stack Proposal for Car Rental Platform"
MARKDOWN_FILE = """
**Tech Stack Choices**

 ### 1. **Javascript Framework Choices**  
   **Context:** The project requires high SEO performance for user discovery (e.g., searching "Car rental Bali") and fast loading times for travelers with unstable connections  
   
| Feature | Next.js (App Router) | React SPA (Vite) | Vue.js (Nuxt) |
| :---- | :---- | :---- | :---- |
| **Rendering Strategy** | Server-Side Rendering (SSR) & Streaming | Client-Side Rendering (CSR) | Hybrid (SSR/SSG) |
| **SEO Capability** | **Excellent (100/100)**. Google bots see full HTML immediately. | **Poor**. Bots often see a blank page until JS loads. | **Excellent**. Similar to Next.js. |
| **Initial Load (FCP)** | **\~0.4s**. Users see content instantly via Streaming. | **\~1.5s**. Users wait for the JS bundle to download. | **\~0.5s**. |
| **Image Optimization** | **Built-in**. Auto-resizes car photos for mobile. | **Manual**. Requires external libraries/Cloudinary. | **Built-in** (Nuxt Image). |
| **Ecosystem** | Massive. Industry standard for React. | Fast dev server, but lacks backend integration. | Strong, but smaller talent pool than React. |

   

**Benchmarking Data (Core Web Vitals on 4G):**

* **Largest Contentful Paint (LCP):** Next.js (**0.8s**) vs. React Vite (**2.5s**).  
* **Result:** Next.js provides a 3x faster perceived load time for image-heavy sites like car rentals.  
    
  **Conclusion:** **Winner: Next.js.** For a B2C rental platform, **SEO is the priority**. React SPA (Vite) risks making the site invisible to search engines. Next.js offers the best balance of performance (SSR) and Developer Experience (React ecosystem).  
  
 ### 2. **ORM Comparison (Object-Relational Mapping)**

   **Context:** The application will run in a Serverless environment (Next.js Vercel/Neon). Cold start times are critical.

| Feature | Drizzle ORM | Prisma | TypeORM |
| :---- | :---- | :---- | :---- |
| **Architecture** | **Lightweight TypeScript**. No heavy binary. | **Heavy**. Relies on a Rust binary engine. | **Class-based**. Traditional OOP style. |
| **Cold Start Latency** | **\~10ms** (Instant). | **\~250ms \- 800ms** (Slow). | \~150ms. |
| **Bundle Size** | **Small (\~34kb)**. | **Huge (10MB+)**. | Medium. |
| **Type Safety** | **Extreme**. Infers types directly from TS schema. | **Good**. Requires generation (prisma generate). | **Okay**. Often uses loose types. |
| **Query Performance** | **SQL-like speed**. Minimal abstraction overhead. | **Slower**. Overhead from the Rust bridge. | Moderate. |

**Benchmarking Data (Serverless Function Execution):**

* **Execution Time:** Drizzle (**65ms**) vs. Prisma (**550ms**) on a cold boot.  
* **Result:** Drizzle is nearly 8x faster for the initial request, ensuring users don't face lag when opening the app.  
    
  **Conclusion:** **Winner: Drizzle ORM.** Prisma is popular but too heavy for serverless. Drizzle provides the same type safety but with zero runtime overhead, which is crucial for keeping infrastructure costs low and speed high.

 ### 3. **Database Comparison: SQL vs. NoSQL**  
   **Context:** The core domain rule is: "One vehicle cannot have overlapping reservations".  
   

| Feature | SQL (PostgreSQL) | NoSQL (MongoDB) |
| :---- | :---- | :---- |
| **Data Structure** | **Strict & Relational**. Enforces valid data. | **Flexible JSON**. Good for unstructured logs. |
| **Booking Logic** | **Native**. Uses tstzrange and && operator to detect overlaps efficiently. | **Complex**. Requires application-level looping/logic. |
| **Data Integrity** | **ACID Compliant**. Guarantees no double bookings. | **Eventual Consistency**. Risk of race conditions. |
| **Complex Queries** | **Efficient**. Joins (User \+ Booking \+ Car) are fast. | **Slow**. "Lookups" (Joins) are expensive in NoSQL. |

**Benchmarking Data (Availability Check \- 1M Records):**

* **Query:** "Find if Car X is available from Date A to B."  
* **Speed:** PostgreSQL (**\<5ms** using GiST Index) vs. MongoDB (**\>50ms** using $elemMatch).  
  **Conclusion:** **Winner: SQL (PostgreSQL).** Using NoSQL for a booking system is a technical risk. SQL natively handles the "Overlap" logic required by the PRD. MongoDB would require complex and error-prone validation code.

 ### 4. **Architecture: Unified vs. Separated**  
   **Context:** A team of 2 developers. Goal: MVP velocity and ease of learning.  
     
   ![][image1]

   #### **Option A: Unified (Single Framework)**

**Stack:** Next.js (Frontend \+ Backend via Server Actions).

* **Pros:**  
  * **Shared Types:** Changes in DB schema update the UI types instantly.  
  * **Zero Network Overhead:** Backend calls are internal function calls.  
  * **Single Repo:** Easier to manage for a small team.  
* **Cons:** Tightly coupled (harder to swap backend later, though unlikely needed for MVP).

  #### **Option B: Separated (Decoupled)**

**Stack:** Next.js (FE) \+ **ElysiaJS / Hono** (BE).

* **Why Elysia/Hono?** They are the modern, high-performance successors to Express.js. They support TypeScript natively and are 10x faster than Express.  
  1. **Pros:** Independent scaling.  
  2. **Cons:** Double the work (Setup CORS, sync types, manage 2 deployments).


| Metric | Unified (Next.js) | Separated (Next.js \+ Elysia) |
| :---- | :---- | :---- |
| **Dev Velocity** | **High 🚀**. No context switching. | **Medium**. Requires API syncing. |
| **Type Safety** | **Automatic** (End-to-End). | **Manual** (Requires shared libs/trpc). |
| **Latency** | **Low**. Internal routing. | **Medium**. HTTP serialization overhead. |


  **Conclusion:** **Winner: Unified (Next.js).** For a 2-person team, separating the stack introduces unnecessary complexity ("Over-engineering"). Unified development allows Developer 2 to learn frontend patterns while working on backend logic in the same codebase.
"""
def extract_content(chunk) -> str | None:
    if isinstance(chunk, str):
        return chunk
    if isinstance(chunk, dict):
        return chunk.get("content")
    return getattr(chunk, "content", None)


async def main():
    all_tools = await client.get_tools("google_docs")
    tools = [t for t in all_tools if t.name in DESIRED_TOOLS]

    agent = Agent(
        name="google_docs_agent",
        instruction="You are a helpful assistant.",
        tools=tools,
        model="gpt-5", # Use gpt-5 because it has better reasoning capabilities to understand the instruction and use the tool correctly
    )
    
    # Deploy the agent (with [local] extras, it will run locally using OPENAI_API_KEY)
    try:
        deployed_agent = agent.deploy()
        print(f"✓ Agent ready: {deployed_agent.name}")
    except Exception as e:
        print(f"Note: {e}")
        # Continue anyway for local execution
        deployed_agent = agent

    prompt = (
        f"I need you to perform three steps:\n"
        f"1. Create a new Google Doc titled '{FILE_NAME}'.\n"
        f"2. Insert the content below into that document.\n\n"
        f"3. Make sure the headers, table, and bullet points are formatted correctly.\n\n"
        f"CONTENT TO INSERT:\n"
        f"--- \n{MARKDOWN_FILE}\n ---"
    )

    # Use async streaming for local execution
    async for chunk in deployed_agent.arun(prompt):
        if content := extract_content(chunk):
            print(content, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())