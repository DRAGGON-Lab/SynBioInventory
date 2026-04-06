import {
  AuthMeResponse,
  CollectionListResponse,
  CreateInventoryPayload,
  InventoryCreateResponse,
  InventoryTypeOption,
} from "./types";

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

async function jsonFetch<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${url}`, {
    credentials: "include",
    ...init,
  });

  if (!response.ok) {
    const detail = await response.text();
    throw new Error(detail || `Request failed (${response.status})`);
  }

  return response.json() as Promise<T>;
}

export const api = {
  login: (username: string, password: string) =>
    jsonFetch<AuthMeResponse>("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    }),

  logout: () => jsonFetch<{ authenticated: boolean }>("/api/auth/logout", { method: "POST" }),

  me: () => jsonFetch<AuthMeResponse>("/api/auth/me"),

  rootCollections: () => jsonFetch<CollectionListResponse>("/api/collections/root"),

  subcollections: (uri: string) =>
    jsonFetch<CollectionListResponse>(`/api/collections/subcollections?uri=${encodeURIComponent(uri)}`),

  inventoryTypes: () => jsonFetch<InventoryTypeOption[]>("/api/inventory/types"),

  createInventory: async (payload: CreateInventoryPayload): Promise<InventoryCreateResponse> => {
    const form = new FormData();
    form.append("destination_collection_uri", payload.destination_collection_uri);
    form.append("implementation_type", payload.implementation_type);
    if (payload.name) form.append("name", payload.name);
    if (payload.notes) form.append("notes", payload.notes);
    if (payload.barcode) form.append("barcode", payload.barcode);
    if (payload.lot_id) form.append("lot_id", payload.lot_id);
    if (payload.built_uri) form.append("built_uri", payload.built_uri);
    for (const image of payload.images) form.append("images", image);

    return jsonFetch<InventoryCreateResponse>("/api/inventory/create", {
      method: "POST",
      body: form,
    });
  },
};
