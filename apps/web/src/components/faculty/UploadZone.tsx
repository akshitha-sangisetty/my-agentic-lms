'use client';

import { useState, useCallback } from 'react';

interface UploadZoneProps {
  courseId: string;
  onUploadComplete?: (filename: string) => void;
}

export function UploadZone({ courseId, onUploadComplete }: UploadZoneProps) {
  const [isDragging, setIsDragging] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [progress, setProgress] = useState(0);

  const handleDrop = useCallback(
    async (e: React.DragEvent) => {
      e.preventDefault();
      setIsDragging(false);
      const file = e.dataTransfer.files[0];
      if (!file) return;

      // TODO(agent): Implement actual upload via uploadMaterials API
      setUploading(true);
      setProgress(0);

      // Simulated progress
      const interval = setInterval(() => {
        setProgress((prev) => {
          if (prev >= 100) {
            clearInterval(interval);
            setUploading(false);
            onUploadComplete?.(file.name);
            return 100;
          }
          return prev + 10;
        });
      }, 200);
    },
    [courseId, onUploadComplete],
  );

  return (
    <div
      onDragOver={(e) => {
        e.preventDefault();
        setIsDragging(true);
      }}
      onDragLeave={() => setIsDragging(false)}
      onDrop={handleDrop}
      className={`
        relative rounded-xl border-2 border-dashed p-12 text-center transition-colors
        ${isDragging ? 'border-brand-500 bg-brand-50 dark:bg-brand-950' : 'border-gray-300 hover:border-gray-400'}
        ${uploading ? 'pointer-events-none opacity-75' : 'cursor-pointer'}
      `}
    >
      {uploading ? (
        <div>
          <div className="w-full bg-gray-200 rounded-full h-3 mb-3">
            <div
              className="bg-brand-600 h-3 rounded-full transition-all duration-300"
              style={{ width: `${progress}%` }}
            />
          </div>
          <p className="text-sm text-gray-600">Uploading... {progress}%</p>
        </div>
      ) : (
        <>
          <p className="text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            Drag & drop course materials
          </p>
          <p className="text-sm text-gray-500">PDF, PPTX, DOCX, MP4, MP3</p>
        </>
      )}
    </div>
  );
}
