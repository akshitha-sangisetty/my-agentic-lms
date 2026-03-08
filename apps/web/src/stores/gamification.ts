'use client';

import { create } from 'zustand';

interface GamificationState {
  xp: number;
  gold: number;
  currentStreak: number;
  longestStreak: number;
  setProfile: (profile: { xp: number; gold: number; currentStreak: number; longestStreak: number }) => void;
  addXP: (amount: number) => void;
  spendGold: (amount: number) => boolean;
  earnGold: (amount: number) => void;
}

export const useGamificationStore = create<GamificationState>((set, get) => ({
  xp: 0,
  gold: 100,
  currentStreak: 0,
  longestStreak: 0,

  setProfile: (profile) =>
    set({
      xp: profile.xp,
      gold: profile.gold,
      currentStreak: profile.currentStreak,
      longestStreak: profile.longestStreak,
    }),

  addXP: (amount) => set((state) => ({ xp: state.xp + amount })),

  spendGold: (amount) => {
    const { gold } = get();
    if (gold < amount) return false;
    set({ gold: gold - amount });
    return true;
  },

  earnGold: (amount) => set((state) => ({ gold: state.gold + amount })),
}));
