'use client';

import { useState } from 'react';
import { useGamificationStore } from '@/stores/gamification';

interface HintButtonProps {
  assignmentId: string;
  tier: 'NUDGE' | 'GUIDANCE' | 'SOLUTION';
  cost: number;
  onHintReceived?: (hintText: string) => void;
}

export function HintButton({ assignmentId, tier, cost, onHintReceived }: HintButtonProps) {
  const [confirming, setConfirming] = useState(false);
  const [loading, setLoading] = useState(false);
  const { gold, spendGold } = useGamificationStore();

  const tierLabels = { NUDGE: 'Nudge', GUIDANCE: 'Guidance', SOLUTION: 'Solution' };
  const canAfford = gold >= cost;

  const handlePurchase = async () => {
    if (!canAfford) return;

    setLoading(true);
    const success = spendGold(cost);

    if (success) {
      // TODO(agent): Call purchaseHint API, get actual hint text
      onHintReceived?.('Hint content will appear here.');
    }

    setLoading(false);
    setConfirming(false);
  };

  if (confirming) {
    return (
      <div className="flex items-center gap-2">
        <span className="text-sm text-gray-600">Spend {cost} Gold?</span>
        <button
          onClick={handlePurchase}
          disabled={!canAfford || loading}
          className="px-3 py-1 text-sm bg-gold text-white rounded-lg hover:bg-gold-dark disabled:opacity-50"
        >
          {loading ? '...' : 'Confirm'}
        </button>
        <button
          onClick={() => setConfirming(false)}
          className="px-3 py-1 text-sm border border-gray-300 rounded-lg hover:bg-gray-100"
        >
          Cancel
        </button>
      </div>
    );
  }

  return (
    <button
      onClick={() => setConfirming(true)}
      disabled={!canAfford}
      className={`
        flex items-center gap-2 px-4 py-2 rounded-lg font-medium text-sm transition-colors
        ${canAfford
          ? 'bg-gold/10 text-gold-dark hover:bg-gold/20 border border-gold/30'
          : 'bg-gray-100 text-gray-400 cursor-not-allowed'}
      `}
    >
      <span>{tierLabels[tier]}</span>
      <span className="flex items-center gap-1">
        <span className="text-gold">&#9679;</span>
        {cost}
      </span>
    </button>
  );
}
