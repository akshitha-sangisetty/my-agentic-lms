export default function FacultyDashboard() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Faculty Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* TODO(agent): Implement faculty dashboard with:
            1. Course cards with status (SETUP/ACTIVE/ARCHIVED)
            2. "Create New Course" button → opens Course Setup Wizard
            3. Quick stats: total students, pending reviews, at-risk alerts
            4. Recent activity feed
        */}
        <div className="rounded-xl border border-dashed border-gray-300 p-8 flex flex-col items-center justify-center text-gray-500 hover:border-brand-500 hover:text-brand-600 cursor-pointer transition-colors">
          <span className="text-4xl mb-2">+</span>
          <span className="font-medium">Create New Course</span>
        </div>
      </div>
    </div>
  );
}
