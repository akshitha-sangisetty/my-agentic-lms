export default function StudentLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-950">
      {/* Student navigation */}
      <nav className="fixed top-0 left-0 h-full w-64 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 p-6">
        <div className="text-xl font-bold text-brand-600 mb-8">Agentic LMS</div>
        <ul className="space-y-2">
          <li>
            <a href="/student/dashboard" className="block px-4 py-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 font-medium">
              Missions
            </a>
          </li>
          <li>
            <a href="/student/tutor" className="block px-4 py-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800">
              AI Tutor
            </a>
          </li>
          <li>
            <a href="/student/profile" className="block px-4 py-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800">
              Profile
            </a>
          </li>
        </ul>
      </nav>
      <main className="ml-64">{children}</main>
    </div>
  );
}
