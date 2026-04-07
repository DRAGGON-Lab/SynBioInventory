import type {
  AuthResponse,
  CollectionNode,
  CreateInventoryPayload,
  CreateInventoryResponse,
  InventoryType,
} from "./types";

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

async function jsonRequest<T>(input: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${input}`, {
    credentials: "include",
    ...init,
  });

  if (!response.ok) {
    const errorBody = await response.text();
    throw new Error(errorBody || `Request failed (${response.status})`);
  }

  return response.json() as Promise<T>;
}

export const api = {
  login: (username: string, password: string) =>
    jsonRequest<AuthResponse>("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    }),
  logout: () => jsonRequest<AuthResponse>("/api/auth/logout", { method: "POST" }),
  me: () => jsonRequest<AuthResponse>("/api/auth/me"),
  getRootCollections: () => jsonRequest<CollectionNode[]>("/api/collections/root"),
  getSubcollections: (uri: string) =>
    jsonRequest<CollectionNode[]>(`/api/collections/subcollections?uri=${encodeURIComponent(uri)}`),
  getInventoryTypes: () => jsonRequest<InventoryType[]>("/api/inventory/types"),
  createInventory: async (payload: CreateInventoryPayload): Promise<CreateInventoryResponse> => {
    const form = new FormData();
    form.append("destination_collection_uri", payload.destination_collection_uri);
    form.append("implementation_type", payload.implementation_type);

    if (payload.name) form.append("name", payload.name);
    if (payload.notes) form.append("notes", payload.notes);
    if (payload.built_uri) form.append("built_uri", payload.built_uri);
    if (payload.barcode) form.append("barcode", payload.barcode);
    if (payload.lot_id) form.append("lot_id", payload.lot_id);
    payload.images.forEach((file) => form.append("images", file));

    const response = await fetch(`${API_BASE}/api/inventory/create`, {
      method: "POST",
      credentials: "include",
      body: form,
    });

    if (!response.ok) {
      throw new Error(await response.text());
    }

    return response.json() as Promise<CreateInventoryResponse>;
  },
};
