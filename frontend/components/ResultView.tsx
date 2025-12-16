export default function ResultView({
  imageUrl,
  prompt,
}: {
  imageUrl: string;
  prompt: string;
}) {
  return (
    <div className="mt-10">
      <img
        src={`${process.env.NEXT_PUBLIC_API_BASE_URL}/${imageUrl}`}
        alt="Generated"
        className="rounded-md border border-neutral-800"
      />

      <div className="mt-4">
        <h3 className="text-sm text-neutral-400 mb-1">
          Final Prompt
        </h3>
        <p className="text-sm bg-neutral-900 p-3 rounded-md">
          {prompt}
        </p>
      </div>
    </div>
  );
}
