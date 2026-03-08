'use client';

import { create } from 'zustand';

interface AuthState {
  token: string | null;
  role: 'faculty' | 'student' | 'admin' | 'ta' | null;
  userId: string | null;
  setAuth: (token: string, role: AuthState['role'], userId: string) => void;
  clearAuth: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: null,
  role: null,
  userId: null,

  setAuth: (token, role, userId) => set({ token, role, userId }),
  clearAuth: () => set({ token: null, role: null, userId: null }),
}));
