'use client';

interface StreakCounterProps {
  days: number;
}

export function StreakCounter({ days }: StreakCounterProps) {
  return (
    <div className="flex items-center gap-1.5">
      <span className={`text-lg ${days > 0 ? 'text-streak' : 'text-gray-400'}`}>
        &#128293;
      </span>
      <span className={`font-bold ${days > 0 ? 'text-streak-dark' : 'text-gray-400'}`}>
        {days}
      </span>
    </div>
  );
}
