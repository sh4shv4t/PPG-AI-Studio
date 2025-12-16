"use client";

import { useState } from "react";
import PromptInput from "@/components/PromptInput";
import ResultView from "@/components/ResultView";
import TracePanel from "@/components/TracePanel";
import LoadingSkeleton from "@/components/LoadingSkeleton";

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const generate = async (idea: string) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_BASE_URL}/api/generate`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ idea }),
        }
      );

      if (!res.ok) throw new Error("Generation failed");

      const data = await res.json();
      setResult(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="max-w-4xl mx-auto px-6 py-12">
      <h1 className="text-3xl font-semibold mb-2">
        PPG AI Studio
      </h1>
      <p className="text-neutral-400 mb-8">
        Prompt → Plan → Generate using LangGraph + Flux
      </p>

      <PromptInput onSubmit={generate} disabled={loading} />

      {loading && <LoadingSkeleton />}

      {error && (
        <p className="text-red-400 mt-6">{error}</p>
      )}

      {result && (
        <>
          <ResultView
            imageUrl={result.image_url}
            prompt={result.final_prompt}
          />
          <TracePanel
            logs={result.state_log}
            steps={result.past_steps}
          />
        </>
      )}
    </main>
  );
}
