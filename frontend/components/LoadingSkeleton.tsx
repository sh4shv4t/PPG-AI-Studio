export default function LoadingSkeleton() {
  return (
    <div className="mt-8 space-y-4 animate-pulse">
      <div className="h-64 bg-neutral-800 rounded-md" />
      <div className="h-4 bg-neutral-800 rounded w-2/3" />
      <div className="h-4 bg-neutral-800 rounded w-1/2" />
    </div>
  );
}
