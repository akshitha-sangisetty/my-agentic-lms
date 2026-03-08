import { apiClient } from './client';
import type { Assignment, AssignmentGenerationConfig } from '@/types/api';

export async function generateAssignments(
  courseId: string,
  config: AssignmentGenerationConfig,
  token: string,
): Promise<{ course_id: string; generated_count: number; assignments: Assignment[] }> {
  return apiClient(`/api/v1/courses/${courseId}/generate-assignments`, {
    method: 'POST',
    body: JSON.stringify(config),
    token,
  });
}

export async function listAssignments(courseId: string, token: string): Promise<Assignment[]> {
  return apiClient<Assignment[]>(`/api/v1/courses/${courseId}/assignments`, { token });
}

export async function getAssignment(assignmentId: string, token: string): Promise<Assignment> {
  return apiClient<Assignment>(`/api/v1/assignments/${assignmentId}`, { token });
}

export async function publishAssignment(
  assignmentId: string,
  token: string,
): Promise<Assignment> {
  return apiClient<Assignment>(`/api/v1/assignments/${assignmentId}/publish`, {
    method: 'POST',
    token,
  });
}
