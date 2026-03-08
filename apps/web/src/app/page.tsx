export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">Agentic LMS</h1>
      <p className="text-lg text-gray-600 dark:text-gray-400 mb-8">
        AI-powered Learning Management System
      </p>
      <div className="flex gap-4">
        <a
          href="/faculty/dashboard"
          className="rounded-lg bg-brand-600 px-6 py-3 text-white font-medium hover:bg-brand-700 transition-colors"
        >
          Faculty Dashboard
        </a>
        <a
          href="/student/dashboard"
          className="rounded-lg border border-brand-600 px-6 py-3 text-brand-600 font-medium hover:bg-brand-50 transition-colors"
        >
          Student Portal
        </a>
      </div>
    </main>
  );
}
