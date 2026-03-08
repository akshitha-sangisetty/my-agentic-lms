export default function StudentDashboard() {
  return (
    <div className="p-8">
      {/* Gamification top bar */}
      <div className="flex items-center justify-between mb-8">
        <h1 className="text-3xl font-bold">My Missions</h1>
        <div className="flex items-center gap-6">
          {/* TODO(agent): Wire these to useGamificationStore */}
          <div className="flex items-center gap-2">
            <span className="text-xp font-bold">0 XP</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-gold font-bold">100 Gold</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-streak font-bold">0 day streak</span>
          </div>
        </div>
      </div>

      {/* Mission Map */}
      <div className="space-y-4">
        {/* TODO(agent): Implement MissionMap component:
            1. Vertically scrolling map with nodes for each assignment
            2. Visual states: Completed (green) → Current (pulsing) → Locked (gray)
            3. Click completed nodes to review feedback
            4. Prerequisite-based unlocking via Knowledge Graph
        */}
        <div className="text-center text-gray-500 py-20">
          <p className="text-lg">No missions available yet.</p>
          <p className="text-sm">Your instructor will publish assignments soon.</p>
        </div>
      </div>
    </div>
  );
}
