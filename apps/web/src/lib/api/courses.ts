import { apiClient, uploadFile } from './client';
import type { Course, CourseCreateRequest, IngestionStatus } from '@/types/api';

export async function createCourse(data: CourseCreateRequest, token: string): Promise<Course> {
  return apiClient<Course>('/api/v1/courses', {
    method: 'POST',
    body: JSON.stringify(data),
    token,
  });
}

export async function listCourses(token: string): Promise<Course[]> {
  return apiClient<Course[]>('/api/v1/courses', { token });
}

export async function getCourse(courseId: string, token: string): Promise<Course> {
  return apiClient<Course>(`/api/v1/courses/${courseId}`, { token });
}

export async function uploadMaterials(
  courseId: string,
  file: File,
  token: string,
): Promise<Record<string, unknown>> {
  return uploadFile(`/api/v1/courses/${courseId}/upload`, file, token);
}

export async function getIngestionStatus(
  courseId: string,
  token: string,
): Promise<IngestionStatus> {
  return apiClient<IngestionStatus>(`/api/v1/courses/${courseId}/ingestion-status`, { token });
}
