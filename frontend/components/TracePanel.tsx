"use client";

import { useState } from "react";

export default function TracePanel({
  logs,
  steps,
}: {
  logs: string[];
  steps: [string, string][];
}) {
  const [open, setOpen] = useState(false);

  return (
    <div className="mt-8">
      <button
        onClick={() => setOpen(!open)}
        className="text-sm text-neutral-400 underline"
      >
        {open ? "Hide agent trace" : "Show agent trace"}
      </button>

      {open && (
        <div className="mt-4 space-y-4 text-sm">
          <div>
            <h4 className="font-medium mb-1">State Log</h4>
            <ul className="list-disc list-inside text-neutral-400">
              {logs.map((l, i) => (
                <li key={i}>{l}</li>
              ))}
            </ul>
          </div>

          <div>
            <h4 className="font-medium mb-1">Past Steps</h4>
            {steps.map(([step, result], i) => (
              <div key={i} className="mb-2">
                <p className="text-neutral-300">{step}</p>
                <p className="text-neutral-500">{result}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
