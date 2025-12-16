"use client";

import { useState } from "react";

export default function PromptInput({
  onSubmit,
  disabled,
}: {
  onSubmit: (idea: string) => void;
  disabled: boolean;
}) {
  const [idea, setIdea] = useState("");

  return (
    <div className="mb-6">
      <textarea
        className="w-full p-4 rounded-md bg-neutral-900 border border-neutral-800 resize-none"
        rows={4}
        placeholder="Describe your idea..."
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
      />
      <button
        disabled={disabled || !idea}
        onClick={() => onSubmit(idea)}
        className="mt-3 px-6 py-2 rounded-md bg-white text-black font-medium disabled:opacity-40"
      >
        Generate
      </button>
    </div>
  );
}
