'use client';

interface GoldBalanceProps {
  balance: number;
}

export function GoldBalance({ balance }: GoldBalanceProps) {
  return (
    <div className="flex items-center gap-1.5">
      <span className="text-gold text-lg">&#9679;</span>
      <span className="font-bold text-gold-dark dark:text-gold-light">{balance}</span>
    </div>
  );
}
