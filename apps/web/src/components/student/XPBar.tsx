'use client';

interface XPBarProps {
  current: number;
  nextLevel: number;
  level: number;
}

export function XPBar({ current, nextLevel, level }: XPBarProps) {
  const progress = Math.min((current / nextLevel) * 100, 100);

  return (
    <div className="flex items-center gap-3">
      <span className="text-sm font-bold text-xp">Lv {level}</span>
      <div className="flex-1 bg-gray-200 dark:bg-gray-700 rounded-full h-2.5">
        <div
          className="bg-xp h-2.5 rounded-full transition-all duration-500"
          style={{ width: `${progress}%` }}
        />
      </div>
      <span className="text-xs text-gray-500">
        {current}/{nextLevel} XP
      </span>
    </div>
  );
}
